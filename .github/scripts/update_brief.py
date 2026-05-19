#!/usr/bin/env python3
"""Daily updater for the Force Majeure Tracker.

Reads the current state of the repo (HTML pages, methodology, sources,
knowledge base, backtest log, last archived brief), calls the Claude API
with the web-search tool, parses delimiter-bracketed output blocks, and
rewrites BRIEF:* sections in index.html and brief.html. Archives
yesterday's brief, appends today's predictions to the backtest log, and
sanity-checks BRIEF:* marker balance before exit.

Output format from Claude is delimiter blocks, not JSON — JSON-escape
errors fail at scale on large embedded HTML. Streaming is required because
max_tokens >= 24000 triggers SDK timeout in non-streaming mode.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import os
import re
import sys
from pathlib import Path

from anthropic import Anthropic


REPO = Path(__file__).resolve().parents[2]

INDEX = REPO / "index.html"
BRIEF = REPO / "brief.html"
METHODOLOGY = REPO / "methodology.md"
SOURCES = REPO / "sources.md"
KNOWLEDGE = REPO / "knowledge-base.md"
BACKTEST = REPO / "backtest-log.md"
REFLECTION = REPO / "reflection-log.md"
HYPOTHESIS = REPO / "hypothesis-log.md"
SOURCE_RELIABILITY = REPO / "source-reliability.md"
AUDIT = REPO / "methodology-audit.md"
EVENTS_CSV = REPO / "events.csv"
ARCHIVE_DIR = REPO / "daily-briefs"

# Canonical events.csv schema. Matches the Felsberger Day-55 dataset.
EVENTS_COLUMNS = [
    "day", "entity", "country", "chain", "wave", "fm_type",
    "volume_kt", "is_eu_direct", "source", "notes", "date",
]

# fm_type integer -> (display name, color) for TYPE_DATA chart.
FM_TYPE_LABELS = [
    ("1", "Production (physical)", "#1e3a5f"),
    ("3", "Downstream feedstock", "#b67a08"),
    ("2", "Shipping / logistics", "#2c4d6f"),
    ("6", "Cascade / derivative", "#c1272d"),
    ("5", "Restart / forward-coverage", "#7a3a8c"),
    ("4", "Distribution", "#2c7a4a"),
]

ANCHOR_DATE = dt.date(2026, 2, 28)  # Day 1 = 28 Feb 2026
TITLE_PREFIX_INDEX = "Force Majeure Tracker — Supply Chain Crisis · "
TITLE_PREFIX_BRIEF = "Deep brief — Force Majeure Tracker · "

MODEL = os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5-20251001")
# Haiku 4.5 has a much higher Tier-1 ITPM ceiling than Sonnet 4.6 (Sonnet
# is 30k ITPM on this key, which can't fit one tool-use cycle). Haiku
# handles the structured-block output cleanly and supports web_search.
# Last run hit max_tokens at 20k just before REFLECTION (block 34/35) — so
# bumping to 24k plus reordering REFLECTION before the long ARCHIVE_BODY.
MAX_OUTPUT_TOKENS = int(os.environ.get("CLAUDE_MAX_TOKENS", "24000"))
# Tier-1 rate limit on this API key is 30k input tokens/min. Each tool-use
# round-trip with web_search re-sends the full conversation context, so
# 6 searches across 1 run × ~5k tokens each ≈ 30k cumulative — the ceiling.
# When the key tiers up (auto, with usage), bump to 15.
MAX_WEB_SEARCHES = int(os.environ.get("CLAUDE_MAX_SEARCHES", "6"))

# Trim aggressively. Per-request input ≈ system + user + tool_results so far.
# Target single-request input ≤ 8k tokens (~32k chars).
MAX_BACKTEST_CHARS = 2500
MAX_LAST_ARCHIVE_CHARS = 2000
MAX_METHODOLOGY_CHARS = 2000
MAX_SOURCES_CHARS = 800
MAX_KNOWLEDGE_CHARS = 3500
MAX_HTML_PER_FILE_CHARS = 5000

# Critical keys — if any of these are missing, the run fails (the dashboard
# would show stale headline indicators). All other block keys are best-effort:
# missing ones leave the previous HTML content in place.
CRITICAL_KEYS = [
    "DATE", "DAY", "TREND", "WAVE_INTENSITY", "ONELINER", "SUMMARY",
]

# Full list of blocks the model is asked to produce.
ALL_KEYS = [
    "DAY", "DATE", "LAST_UPDATED", "MAP_TS",
    "TREND", "WAVE_INTENSITY", "LEAD_INDICATOR",
    "ONELINER", "SUMMARY",
    "TILE_1", "TILE_2", "TILE_3", "TILE_4", "TILE_5", "TILE_6",
    "ACTIONS", "WATCHLIST", "SCENARIOS",
    "CATEGORY_1", "CATEGORY_2", "CATEGORY_3",
    "CATEGORY_4", "CATEGORY_5", "CATEGORY_6",
    "FM_TABLE", "WAVE_GRID",
    "MAP_PINS", "WAVE_DATA", "CHAIN_DATA", "TYPE_DATA",
    "INDUSTRY_DATA", "GOLDEN_SCREW_DATA", "RECENT_EVENTS_DATA",
    "VOLUME_INDEX",
    "NEW_EVENTS",
    "BACKTEST_ENTRY", "REFLECTION", "ARCHIVE_BODY",
    "HYPOTHESIS_DELTA", "SOURCE_RELIABILITY_DELTA", "METHODOLOGY_DELTA",
]


# ---------- helpers ----------

def read_text(p: Path) -> str:
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


def write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def trim(s: str, n: int) -> str:
    if len(s) <= n:
        return s
    return s[: n - 80] + "\n\n[... truncated for context budget ...]\n"


def compress_html_for_context(html: str) -> str:
    """Strip <style>, <script> (except MAP_PINS/WAVE_DATA arrays), long style attrs."""
    s = re.sub(r"<style[^>]*>.*?</style>", "<!-- styles omitted -->", html, flags=re.DOTALL)

    def script_repl(m: re.Match) -> str:
        body = m.group(0)
        if any(k in body for k in (
            "BRIEF:MAP_PINS", "BRIEF:WAVE_DATA", "BRIEF:CHAIN_DATA",
            "BRIEF:TYPE_DATA", "BRIEF:INDUSTRY_DATA", "BRIEF:GOLDEN_SCREW_DATA",
            "BRIEF:RECENT_EVENTS_DATA",
        )):
            return body
        return "<!-- script omitted -->"

    s = re.sub(r"<script[^>]*>.*?</script>", script_repl, s, flags=re.DOTALL)
    s = re.sub(r'\s+style="[^"]{120,}"', "", s)
    s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
    return s


_BLOCK_RE = re.compile(r"###BEGIN:([A-Z0-9_]+)###\s*\n(.*?)\n\s*###END:\1###", re.DOTALL)


def parse_delimited(text: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in _BLOCK_RE.finditer(text)}


def replace_block(html: str, key: str, content: str) -> tuple[str, int]:
    pattern = re.compile(
        rf"(<!-- BRIEF:{re.escape(key)}_START -->)(.*?)(<!-- BRIEF:{re.escape(key)}_END -->)",
        re.DOTALL,
    )
    return pattern.subn(
        lambda m: m.group(1) + "\n" + content.strip() + "\n" + m.group(3),
        html,
    )


def update_title(html: str, prefix: str, date_human: str) -> str:
    return re.sub(
        rf"(<title>{re.escape(prefix)}).*?(</title>)",
        lambda m: m.group(1) + date_human + m.group(2),
        html,
        count=1,
    )


def count_markers(html: str) -> tuple[int, int]:
    starts = len(re.findall(r"<!-- BRIEF:[A-Z0-9_]+_START -->", html))
    ends = len(re.findall(r"<!-- BRIEF:[A-Z0-9_]+_END -->", html))
    return starts, ends


def replace_js_array(html: str, marker_name: str, content: str) -> tuple[str, int]:
    """Replace JS array contents between // BRIEF:NAME_START and // BRIEF:NAME_END."""
    pattern = re.compile(
        rf"(// BRIEF:{re.escape(marker_name)}_START\n)(.*?)(\n// BRIEF:{re.escape(marker_name)}_END)",
        re.DOTALL,
    )
    return pattern.subn(
        lambda m: m.group(1) + content.strip() + m.group(3),
        html,
    )


def extract_js_array(html: str, marker_name: str) -> str:
    """Read the current contents of a BRIEF:NAME_START/END js-array block."""
    m = re.search(
        rf"// BRIEF:{re.escape(marker_name)}_START\n(.*?)\n// BRIEF:{re.escape(marker_name)}_END",
        html,
        re.DOTALL,
    )
    return m.group(1) if m else ""


# ---------- events.csv — the canonical FM event ledger ----------

def event_id(operator: str, chain: str, date_str: str) -> str:
    """Stable 12-char hash for dedupe. Same operator+chain+date → same id."""
    key = f"{operator.strip().lower()}|{chain.strip().lower()}|{date_str.strip()}"
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


def load_events() -> list[dict]:
    if not EVENTS_CSV.exists():
        return []
    with open(EVENTS_CSV, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_events(rows: list[dict]) -> None:
    with open(EVENTS_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=EVENTS_COLUMNS)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in EVENTS_COLUMNS})


def parse_new_events_block(block: str, anchor_date: dt.date) -> list[dict]:
    """Parse model-emitted NEW_EVENTS CSV-like text into event dicts.

    Format per line: date,operator,country,chain,wave,fm_type,volume_kt,is_eu_direct,source,summary
    Lines beginning with `#`, blank lines, header lines, and `none` are ignored.
    """
    if not block or block.strip().lower() in {"none", "n/a", "no change", ""}:
        return []
    events: list[dict] = []
    for raw in block.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("date,"):
            continue  # header row
        if line.lower() in {"none", "n/a"}:
            continue
        try:
            parts = next(csv.reader([line]))
        except StopIteration:
            continue
        if len(parts) < 5:
            continue
        date_str = parts[0].strip()
        try:
            event_date = dt.date.fromisoformat(date_str)
            day_n = (event_date - anchor_date).days + 1
        except (ValueError, TypeError):
            continue
        def at(i: int, default: str = "") -> str:
            return parts[i].strip() if i < len(parts) else default
        events.append({
            "day": str(day_n),
            "entity": at(1),
            "country": at(2),
            "chain": at(3),
            "wave": at(4, "1"),
            "fm_type": at(5, "1"),
            "volume_kt": at(6),
            "is_eu_direct": at(7, "False"),
            "source": at(8),
            "notes": at(9),
            "date": date_str,
        })
    return events


def merge_new_events(existing: list[dict], new: list[dict]) -> tuple[list[dict], list[dict]]:
    """Append new events to existing, dedup by event_id. Returns (merged, added)."""
    seen = {event_id(e.get("entity", ""), e.get("chain", ""), e.get("date", ""))
            for e in existing}
    added: list[dict] = []
    for e in new:
        eid = event_id(e.get("entity", ""), e.get("chain", ""), e.get("date", ""))
        if eid in seen:
            continue
        seen.add(eid)
        existing.append(e)
        added.append(e)
    return existing, added


def compute_wave_data_from_events(events: list[dict], current_day_n: int) -> list[tuple[int, int, int, int]]:
    """Cumulative WAVE_DATA derived from events. One row per day with new events, plus today's row."""
    per_day: dict[int, list[int]] = {}
    for e in events:
        try:
            day = int(str(e.get("day", "")).strip())
            wave = int(str(e.get("wave", "")).strip())
        except (ValueError, TypeError):
            continue
        if wave not in (1, 2, 3):
            continue
        per_day.setdefault(day, [0, 0, 0])
        per_day[day][wave - 1] += 1
    if not per_day:
        return []
    rows: list[tuple[int, int, int, int]] = []
    cum = [0, 0, 0]
    for d in sorted(per_day.keys()):
        cum[0] += per_day[d][0]
        cum[1] += per_day[d][1]
        cum[2] += per_day[d][2]
        rows.append((d, cum[0], cum[1], cum[2]))
    if rows[-1][0] < current_day_n:
        rows.append((current_day_n, cum[0], cum[1], cum[2]))
    return rows


def render_wave_data_block(rows: list[tuple[int, int, int, int]]) -> str:
    items = [f"[{d},{w1},{w2},{w3}]" for d, w1, w2, w3 in rows]
    # 10 per line for readability
    lines = [",".join(items[i:i + 10]) for i in range(0, len(items), 10)]
    return ",\n".join(lines)


def compute_chain_data_from_events(events: list[dict]) -> str:
    """Top-12 commodity chains by event count."""
    counts: dict[str, int] = {}
    for e in events:
        chain = (e.get("chain") or "").strip()
        if chain:
            counts[chain] = counts.get(chain, 0) + 1
    top = sorted(counts.items(), key=lambda x: -x[1])[:12]
    lines = [f'{{ name: "{name}", n: {n} }}' for name, n in top]
    return ",\n".join(lines)


def compute_type_data_from_events(events: list[dict]) -> str:
    """Six-category FM-type breakdown."""
    counts: dict[str, int] = {k: 0 for k, _, _ in FM_TYPE_LABELS}
    for e in events:
        t = (e.get("fm_type") or "").strip()
        if t in counts:
            counts[t] += 1
    lines = []
    for key, name, color in FM_TYPE_LABELS:
        lines.append(f'{{ name: "{name}", n: {counts[key]}, color: "{color}" }}')
    return ",\n".join(lines)


def events_summary_for_prompt(events: list[dict], max_recent: int = 14) -> str:
    """Compact summary the script injects into the user prompt — keeps token cost low."""
    if not events:
        return "events.csv: empty (no events seeded yet)."
    n = len(events)
    by_wave = {"1": 0, "2": 0, "3": 0}
    by_chain: dict[str, int] = {}
    for e in events:
        w = (e.get("wave") or "").strip()
        if w in by_wave:
            by_wave[w] += 1
        c = (e.get("chain") or "").strip()
        if c:
            by_chain[c] = by_chain.get(c, 0) + 1
    top_chains = sorted(by_chain.items(), key=lambda x: -x[1])[:6]
    # Recent events (last `max_recent` by date)
    sortable = sorted(events, key=lambda e: e.get("date", ""), reverse=True)[:max_recent]
    recent_lines = []
    for e in sortable:
        recent_lines.append(
            f"  {e.get('date', '')} · D{e.get('day', '')} · {e.get('entity', '')} · {e.get('chain', '')} · W{e.get('wave', '')}T{e.get('fm_type', '')}"
        )
    return (
        f"events.csv: {n} canonical FM events.\n"
        f"By wave: W1={by_wave['1']} · W2={by_wave['2']} · W3={by_wave['3']}.\n"
        f"Top chains: {', '.join(f'{c}={n}' for c, n in top_chains)}.\n"
        f"Last {len(sortable)} events:\n" + "\n".join(recent_lines)
    )


def merge_wave_data(existing_block: str, new_block: str) -> str:
    """Merge WAVE_DATA blocks with cumulative-monotonicity enforcement.

    WAVE_DATA rows are `[day, w1_cum, w2_cum, w3_cum]`. Cumulative counts
    can only stay flat or increase across days — a regression would mean
    historical FMs were retracted, which never happens in this model.
    The model has been observed writing smaller cumulative values; this
    function takes per-day MAX across existing and new, then enforces
    non-decreasing values walking forward in day order.
    """
    row_re = re.compile(r"\[\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\]")

    def parse_rows(block: str) -> list[tuple[int, int, int, int]]:
        return [
            (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
            for m in row_re.finditer(block)
        ]

    existing_rows = parse_rows(existing_block)
    new_rows = parse_rows(new_block)

    by_day: dict[int, tuple[int, int, int]] = {}
    for d, w1, w2, w3 in existing_rows + new_rows:
        if d in by_day:
            p = by_day[d]
            by_day[d] = (max(p[0], w1), max(p[1], w2), max(p[2], w3))
        else:
            by_day[d] = (w1, w2, w3)

    # Walk days in order, enforce monotonicity (cumulative never decreases)
    out_rows: list[str] = []
    max_so_far = (0, 0, 0)
    for d in sorted(by_day.keys()):
        v = by_day[d]
        v = (max(v[0], max_so_far[0]), max(v[1], max_so_far[1]), max(v[2], max_so_far[2]))
        max_so_far = v
        out_rows.append(f"[{d},{v[0]},{v[1]},{v[2]}]")

    preserved = len(by_day) - len(parse_rows(new_block))
    if preserved > 0:
        print(f"[update_brief] WAVE_DATA merge preserved {preserved} historical day-points", flush=True)

    # Pack 10 per line for readability
    lines = [",".join(out_rows[i:i + 10]) for i in range(0, len(out_rows), 10)]
    return ",\n".join(lines)


def merge_additive_array(existing_block: str, model_block: str) -> str:
    """Merge two JS-array blocks by the first quoted string in each entry
    (typically the `name` or `component` field). Entries the model omits
    are preserved from the existing list. This enforces the additive-only
    rule in code rather than relying on prompt discipline.

    Both blocks are expected to contain one JS object literal per line
    (lines like `{ name: "X", ... },`). Lines not matching that shape
    are passed through verbatim from the model block.
    """
    def normalize(s: str) -> str:
        # Lowercase + strip everything that isn't a letter or digit, so that
        # "QatarEnergy · Ras Laffan", "QatarEnergy Ras Laffan", and
        # "Qatarenergy-Ras-Laffan" all hash to the same key.
        return re.sub(r"[^a-z0-9]", "", s.lower())

    def parse(block: str) -> list[tuple[str, str]]:
        out = []
        for raw in block.splitlines():
            stripped = raw.strip().rstrip(",").strip()
            if not (stripped.startswith("{") and stripped.endswith("}")):
                continue
            m = re.search(r'"([^"]+)"', stripped)
            if m:
                out.append((normalize(m.group(1)), raw.rstrip().rstrip(",")))
        return out

    model_entries = parse(model_block)
    existing_entries = parse(existing_block)
    model_keys = {k for k, _ in model_entries}

    merged_lines: list[str] = [line for _, line in model_entries]
    preserved = 0
    for key, line in existing_entries:
        if key not in model_keys:
            merged_lines.append(line)
            preserved += 1

    if preserved:
        print(f"[update_brief] Merge preserved {preserved} existing entries the model omitted", flush=True)

    return ",\n".join(merged_lines)


# ---------- prompts ----------

SYSTEM_PROMPT = """You are the Resilience Engineers Force Majeure Tracker — daily updater.

You produce the Day-N brief for a global supply-chain force-majeure tracker anchored on Day 1 = 28 February 2026 (the Hormuz / Iran crisis onset). The brief is read by supply-chain executives at 08:00 CEST. Every claim must be testable.

# Cadence and scope

This brief updates **every 3 days**, not daily. Each run covers a 72-hour window. Search comprehensively — you have a budget of up to 30 web searches per run. Quality over quantity, but do not shortchange coverage. The trailing-72h-vs-prior-72h trend rule aligns naturally with the cycle.

# Procedure (every run)

0. **Score the prior brief first.** Open the recent backtest log entries provided. Mark each Action / Watchlist / Scenario as Hit / Miss / False alarm / Surprise / pending. Do this BEFORE drafting today.

1. Read methodology, sources, knowledge base, last archive, current HTML.

2. **Comprehensive web search across the full Tier 1–3 set.** Run searches in this order:

   **(a) Active operator status — search each by name** for new FM declarations or restart confirmations in the last 72h:
   QatarEnergy · Saudi Aramco · SABIC · Sadara · KPC · KNPC · BAPCO · ALBA · EGA · Qatalum · Borouge · ADNOC · Methanex · Ar-Razi · Hindalco · Yeochun NCC · LG Chem · Lotte Chemical · Hanwha Solutions · Hanwha TotalEnergies · Mitsui Chemicals · Mitsubishi Chemical · ENEOS · Wanhua Chemical · Formosa Petrochemical · Formosa Plastics · TPC Singapore · Chandra Asri · Aster Chemicals · OMV · Orlen · Orlen Unipetrol · LyondellBasell · Inovyn · INEOS Styrolution · Trinseo · Vynova · Sasol · Invista · Radici · Excelerate Energy · OQ Trading · Petronet LNG · GAIL India · Targa Resources · Chevron Phillips Chemical · Dow · Mitsubishi Gas Chemical · Shell · TotalEnergies · MRPL · Lufthansa · KLM.

   **(b) Commodity chain searches** — last 72h, FM-related, on each:
   naphtha / petchem · LNG / gas · crude oil · jet fuel / refined · aluminium · methanol · helium · urea / fertilizer · ethylene glycol / PET · container shipping · bunker fuel · pharma excipients.

   **(c) Tier-1 / Tier-2 outlets** — search the last 72h for FM declarations and operator filings:
   Argus Media · ICIS · S&P Global Platts · OPIS · Chemical Week · C&EN · Hydrocarbon Processing · Polymerupdate · ChemAnalyst · Plasteurope · Kunststoffweb · Lloyd's List · Baird Maritime · Ship & Bunker · TradeWinds · Splash247 · Mining Weekly · alcircle · Reuters · Bloomberg.

   **(d) Stock-exchange filings** — Tadawul / Bursa Saudi / BSE / NSE / KOSPI / SGX / TSE / LSE / NYSE for FM-related disclosures from the operators in (a). **Also: SEC EDGAR 8-K full-text search** for US-listed operators (LyondellBasell, Chevron Phillips Chemical, Olin, Trinseo, Westlake, Dow). Material events file within 4 business days — often the first-party source.

   **(d2) Asia-language primary sources** when a Chinese / Korean / Japanese operator is the topic — the English wires lag by 12–48h:
   - **Chinese:** 21st Century Business Herald (二十一世纪经济报道), Caixin (财新), China Chemical Reporter, Sina Finance, Eastmoney.
   - **Korean:** KRX (Korean Exchange) regulated disclosures portal, Maeil Business, ETNews chemicals desk.
   - **Japanese:** Mainichi commercial wire, Iyaku Shokai (pharma), Nikkei (primary, not Nikkei Asia digest).
   Query in the operator's home language when feasible; cite the original outlet plus an English summary.

   **(d3) Regulatory / safety notices.** EU REACH and ECHA capacity-change filings; FDA / EMA shortage lists; ANSM (France) drug-shortage alerts; FAA / EASA airworthiness directives if aviation is in scope.

   **(e) Sovereign and regulator signals** — Saudi Aramco OSP, OPEC+ communiqués, Iranian state media, US Treasury OFAC, EMA / FDA / ANSM shortage lists, central-bank commodity statements.

   **(f) Geographic spread checks** — search for newly affected geographies: West Africa crude substitution, Eastern Med refining, Caribbean methanol, Australian / NZ fertilizer, African aviation.

   Run **5–6 high-quality searches** total — the rate limit caps cumulative input tokens per minute. Pick the broadest queries that surface the most operator names per call (e.g. "force majeure declared May 2026 chemical OR petrochemical OR LNG", "force majeure 2026 Hormuz crude refining"). Pull from Tier 6 (anonymous OSINT, op-eds, AI summaries) ONLY if independently corroborated by Tier 1–3.

3. Classify every signal: Tier (Hard / Medium / Soft / Noise), FM type (1=Production, 2=Shipping, 3=Downstream feedstock, 4=Distribution, 5=Restart, 6=Cascade), Wave (1/2/3), commodity chain, operator+site, source name.

4. Set Trend (Worse / Same / Better) by trailing-72h-vs-prior-72h Hard-signal rule.

5. Set Wave Intensity (L1 Watch / L2 Elevated / L3 Cascade / L4 Systemic / L5 Regime) by operative test on Hard signals only. Wave Intensity does NOT move on Soft input.

6. Draft six categories, six tiles, three actions, five watchlist items, three scenarios.

7. Sync map pins, recent FM table, cascade timeline if status changed.

# Tone

- Practitioner not narrator. Reader is a supply-chain executive at 8 AM.
- Lead with fact, then why, then so-what.
- No AI tells: no "delve", no "elegant", no "comprehensive landscape", no copula avoidance. Say "is", not "represents" or "serves as".
- Numbers when available, ranges when not, "unknown" when unknown.
- Don't generalise from one source to "many experts". Name the source.
- No hindsight reframing.

# Stop conditions

- Tier 1–3 input insufficient → set Trend=Same, write thin brief, flag at top of SUMMARY with "INTERIM —" prefix. Don't pad.
- Tier-1 contradicts Tier-2 → publish Tier-1 reading, name both sources.
- Wave Intensity move without Hard signal → don't publish move; explain Soft signals in WATCHLIST.

# Output format — DELIMITER BLOCKS, NEVER JSON

**HARD RULE 1 — no preamble.** After web-search calls complete, your visible text response must contain ONLY delimiter blocks. No preamble. No "Let me compile...". No "Key findings:". No bullet lists outside blocks. No commentary, EVER, outside ###BEGIN/###END markers. The first non-tool-call character of your text response must be `###BEGIN:`. The last must be `###`.

**HARD RULE 2 — additive arrays NEVER LOSE ENTRIES.** The following blocks are ADDITIVE-ONLY: `MAP_PINS`, `INDUSTRY_DATA`, `GOLDEN_SCREW_DATA`, `RECENT_EVENTS_DATA`. The current contents are provided in the input HTML. Your output MUST include EVERY entry from the input. (Note: `WAVE_DATA`, `CHAIN_DATA`, `TYPE_DATA` are now SCRIPT-DERIVED from `events.csv` — your output for those is discarded; add events via `NEW_EVENTS` instead.) You may:
- Add new entries (new operator, new industry, new chokepoint)
- Update an existing entry's `status`, `note`, `severity`, `risk`, `fm`, `pathway`, or `nonobvious` fields
- Reorder entries
You may NOT remove any entry. The previous brief's pins, industries, and golden-screw items stay forever — once an FM is declared, the historical pin remains on the map even after restart (status=green). This rule exists because a prior run dropped 16 of 24 pins, including all EU sites, which destroyed analytical continuity.

**HARD RULE 3 — produce every block.** You MUST emit every block in the list below in this exact order. Missing CATEGORY blocks have caused build failures previously — produce them all even if content repeats yesterday's where nothing changed.

Each block is wrapped in:

###BEGIN:KEY###
[raw HTML / JS / markdown — any characters allowed, no escaping]
###END:KEY###

Block order (produce in this order):

1. **DAY** — integer N (today minus 28 Feb 2026 + 1).
2. **DATE** — human date, e.g., "10 May 2026".
3. **LAST_UPDATED** — "06:00 UTC".
4. **MAP_TS** — "Day N".
5. **TREND** — HTML: `<div class="val up"><span class="arrow">↑</span>Worse</div><div class="conf">...</div>` (use `up` class for Worse, `down` for Better, no class for Same; arrow ↑ / ↓ / →).
6. **WAVE_INTENSITY** — HTML: `<div class="val">L4 · Systemic <span class="pips"><span class="pip on high"></span>...</span></div><div class="conf">...</div>` (N pips on for LN).
6b. **LEAD_INDICATOR** — HTML for the dashboard's "strongest leading indicator" card. Format: `<div class="v">Restart-type FM count · N</div><div class="desc">One-sentence reason this metric leads the others.</div>`. Default to restart-type FM count (KPC FM2 / SABIC "cannot estimate" / 5-yr long-term FMs) — these mark the L4→L5 boundary. Update value when this count changes; replace metric only if you have evidence a different one now leads (e.g., active site count, cumulative Wave 3 FMs, EU-converter Wave 3 FMs).
7. **ONELINER** — single `<p class="one">...</p>` tag, ≤25 words.
8. **SUMMARY** — 2–4 sentence paragraph in plain text (no tags).
9. **TILE_1** — full `<div class="tile">...</div>` element with badge + h3 + p + .sub. (One-pager status board.)
10. **TILE_2** — same shape.
11. **TILE_3** — same shape.
12. **TILE_4** — same shape.
13. **TILE_5** — same shape.
14. **TILE_6** — same shape.
15. **CATEGORY_1** — full `<article class="cat">...</article>` for the deep brief: head with num/h2/badge, `<ul class="signals">` with 3 li, `<div class="why"><strong>Why this matters</strong>...</div>`, `<div class="impl"><strong>Implication</strong>...</div>`, `<div class="src">Sources · ... · Tier N</div>`. Title: "New FM declarations".
16. **CATEGORY_2** — same shape. Title: "Kinetic / facility damage".
17. **CATEGORY_3** — same shape. Title: "Cascade through downstream chains".
18. **CATEGORY_4** — same shape. Title: "Restart / forward-coverage signals".
19. **CATEGORY_5** — same shape. Title: "Substitution / alternative sourcing".
20. **CATEGORY_6** — same shape. Title: "Outlook scenarios". Body restates the three SCENARIOS in narrative form.
21. **ACTIONS** — full `<div class="actions">...</div>` with three `<div class="action">` children.
22. **WATCHLIST** — full `<div class="watch">...</div>` with EXACTLY this row structure for each of five items:
    ```
    <div class="watch">
      <div class="row">
        <div class="n">01</div>
        <div class="body">Watchlist item description — what to watch and why.</div>
        <div class="when dir-up">By 17 May · escalation</div>
      </div>
      ...four more rows...
    </div>
    ```
    The three child divs (`.n`, `.body`, `.when`) are MANDATORY — the CSS 3-col grid breaks without them. Use class `dir-up` on `.when` for escalation signals (renders red), `dir-down` for de-escalation (green), or no extra class for neutral. Do NOT write `<div class="row"><strong>1. ...</strong> ...</div>` — the strong-bold-prefix pattern collapses the grid.
23. **SCENARIOS** — three `<div class="sc">` children only (no outer wrapper). Probabilities sum to 100.
24. **FM_TABLE** — full `<table class="fmtable">...</table>` for the last 14 days; columns: Operator, Site/Chain, Wave, Type, Status, Date, Source.
25. **WAVE_GRID** — full `<div class="wave">...</div>` with four `<div class="wcell">` children (T+0 / T+7 / T+30 / T+90).
26. **MAP_PINS** — JS array contents (no surrounding `[` / `]`), one object per line, format: `{ name: "...", lat: NN, lon: NN, status: "red"|"amber"|"green", note: "...", chain: "..." },`.
27. **WAVE_DATA** — emit anything (e.g. `auto`); the script DISCARDS your value and recomputes from `events.csv` (the canonical ledger). The total count, by-wave counts, and time-series are all derived from the file. Inflating counts here is impossible because the script ignores you. Add events via the `NEW_EVENTS` block instead — the counts follow automatically.
27b. **NEW_EVENTS** — CSV-formatted rows for every new force-majeure event surfaced this run (or `none` if there are no new ones). The script appends each row to `events.csv` after deduping by hash of `operator|chain|date`. Re-mentioning an existing event is silently ignored — better to err on the side of including. **Format per line** (no header, one event per line):
    ```
    YYYY-MM-DD,Operator name,Country,Commodity chain,wave_number,fm_type_number,volume_kt_or_blank,is_eu_direct,Source attribution,One-line summary
    ```
    - `wave_number`: `1` (production-side / kinetic) · `2` (allocation / shipping) · `3` (downstream feedstock / physical absence)
    - `fm_type_number`: `1` Production (physical) · `2` Shipping/logistics · `3` Downstream feedstock · `4` Distribution · `5` Restart/forward-coverage · `6` Cascade/derivative
    - `volume_kt`: kilotonnes/year of affected capacity; numeric or blank if unknown
    - `is_eu_direct`: `True` if the FM hits an EU-located operator directly, else `False`
    - `Source`: short attribution like `Reuters` or `Tadawul · 8K filing`
    - `summary`: ≤ 30 words, single line, no commas-without-quoting (if your summary contains commas, wrap the whole field in double quotes)

    Example correct lines:
    ```
    2026-05-19,Maersk,Denmark,Container shipping,2,4,,False,Lloyd's List,Suspended all ME bookings effective 25 May after bunker shortage spiked
    2026-05-18,LG Chem,South Korea,Naphtha / petchem,3,5,1200,False,Seoul Economic Daily,Restart pushed to mid-June; naphtha visibility extended
    ```
28. **CHAIN_DATA** — emit anything; script DISCARDS and recomputes from `events.csv` (top-12 chains by event count).
29. **TYPE_DATA** — emit anything; script DISCARDS and recomputes from `events.csv` (six FM-type categories).
30. **INDUSTRY_DATA** — JS array contents (no surrounding `[` / `]`), additive. **Compact format — short sentences only:** `{ name: "Industry name", severity: "Critical|High|Medium|Low", commodities: ["c1", "c2", "c3"], pathway: "ONE sentence on the direct chain to the industry — ≤30 words.", hidden: "ONE sentence on the non-obvious second-order effect — what most analysts miss. ≤30 words." }`. Hard rule: each field is one sentence. The card view renders short prose only; multi-sentence text breaks the layout. Add new industries; revise severity/commodities/text on existing entries; never remove an entry.
31. **GOLDEN_SCREW_DATA** — JS array contents (no surrounding `[` / `]`), additive. **Compact format:** `{ component: "Specific part / grade", industry: "Sector that depends on it", severity: "Critical|High|Medium", sub_time: "Short label like 'No substitute · 6-mo rebuild' or '4–6 mo requalification' or 'Years for new capacity'", risk: "ONE sentence on why ordinary substitution fails — ≤30 words.", fm: "Active FM driver(s), 1–3 names joined by ' + '" }`. Add a row when a component meets the test: small in volume, large in dependency, no drop-in substitute. The test is "would a 30-day outage of this single thing break a major industry."
31b. **RECENT_EVENTS_DATA** — JS array contents (no surrounding `[` / `]`), additive. Chronological feed of FM declarations, NOTAMs, OSP signals, restart announcements, sovereign moves. Format per entry: `{ date: "YYYY-MM-DD", operator: "Name", country: "Country", kind: "FM|NOTAM|Restart|Signal", tier: "Tier 1|Tier 2|Tier 3", tags: ["Commodity", "Industry", ...] (3–5 chips), summary: "ONE sentence describing what changed — ≤25 words.", source: "Outlet · date" }`. Newest at top of the array. **Add every new event you find this run** (typically 2–5 per 3-day cycle). Never remove existing entries — historical events stay forever (the feed shows the last 18 by recency).
32. **BACKTEST_ENTRY** — markdown block to append to backtest-log.md. Header `## YYYY-MM-DD (Day N)`, prior-prediction scoring, today's Trend/Wave with confidence, today's Actions/Watchlist/Scenarios in scorable form, Surprise factor.
31c. **VOLUME_INDEX** — HTML for a new dashboard tile (replaces the previously hardcoded "Restarts confirmed"-only metric on the stats strip if you prefer; or sits alongside). Format: `<div class="num acc">N</div><div class="delta">vol-weighted FM index</div>` where N is the volume-weighted FM index computed from `Σ (volume_kt × confidence_factor)` over all active FMs in MAP_PINS for which volume is known. Use `1.0` for red status, `0.5` for amber, `0.0` for green. Round to integer kilotonnes-equivalent. If you can't compute (insufficient volume data), output `<div class="num">—</div><div class="delta">vol data incomplete</div>`.
32. **BACKTEST_ENTRY** — markdown to append to backtest-log.md. Header `## YYYY-MM-DD (Day N)`, prior-prediction scoring, today's Trend/Wave with confidence, today's Actions/Watchlist/Scenarios in scorable form, Surprise factor.
33. **REFLECTION** — markdown to append to reflection-log.md. Header `## YYYY-MM-DD (Day N) · Reflection`. Three subsections: **What surprised me this run** (one paragraph naming the specific signal that broke an assumption); **Methodology rule that was tested** (which tier-weight, trend-rule, or wave-test was put under stress, and whether it held); **What to change next run** (concrete, testable change). Keep it short.
33b. **HYPOTHESIS_DELTA** — markdown to append to hypothesis-log.md. Two parts:
   - **New hypotheses for this run.** Format per hypothesis: `## H-NNN · Created YYYY-MM-DD (Day N) · Stop-out YYYY-MM-DD (Day N+k)` then **Hypothesis** (≤25 words, declarative), **Discriminating observable** (specific data point + source + threshold), **Prior probability** (0.NN), **Status** (Open). Generate 2–4 hypotheses per run. Reject any hypothesis that lacks a stop-out date or a falsifying observable.
   - **Resolutions for hypotheses whose stop-out passed.** Format: `### H-NNN resolved: [Hit | Miss | False alarm | Surprise]` followed by a one-paragraph note including the posterior probability.
   - If neither new hypotheses nor resolutions apply (rare), output `none`.
33c. **SOURCE_RELIABILITY_DELTA** — markdown to append to source-reliability.md. Two parts:
   - **Sources cited this run.** For each named source that appeared in this run's content, add a row to the current-scoreboard table with the current 4-week stats. Use the existing format.
   - **Tier-change proposals (if any).** If a 4-week rolling hit rate or lead rate crosses a threshold (see source-reliability.md scoring rules), propose a tier change. Format: `**Proposed:** Demote SourceName from Tier 2 to Tier 3 — 4w hit rate 0.55 over 7 citations` etc. Mark `Status: Pending review`.
   - If no changes warranted, output `none`.
33d. **METHODOLOGY_DELTA** — markdown to append to methodology.md. The system MUST propose a methodology delta when ANY of these conditions hold: (a) Miss rate > 30% in any category (Actions / Watchlist / Scenarios) over the last 4 backtest entries; (b) A prior reflection's recommendation has been outstanding ≥ 2 runs without being applied; (c) An audit finding (see methodology-audit.md) has a Status of "implementing today" that has not been reflected in methodology.md. Format: `**Methodology delta YYYY-MM-DD (Day N).** Section X, rule Y: [old] → [new]. Reason: [provenance — backtest miss pattern, reflection recommendation, or audit finding].`. If none of the trigger conditions hold, output `none` — do not pad.
34. **ARCHIVE_BODY** — markdown body for daily-briefs/YYYY-MM-DD.md. Mirror the template: trend / wave intensity / oneliner / summary / 6 categories / actions / watchlist / FM table / wave grid. (Placed last because it is the longest block.)

Output ONLY the 35 delimiter blocks above (1, 2, 3, 4, 5, 6, 6b, 7 ... 34), in order. No preamble. No postamble. No commentary anywhere outside ###BEGIN/###END markers.
"""


def build_user_message(today: dt.date, day_n: int) -> str:
    methodology = trim(read_text(METHODOLOGY), MAX_METHODOLOGY_CHARS)
    sources = trim(read_text(SOURCES), MAX_SOURCES_CHARS)
    knowledge = trim(read_text(KNOWLEDGE), MAX_KNOWLEDGE_CHARS)
    backtest = trim(read_text(BACKTEST), MAX_BACKTEST_CHARS)

    archives = sorted(ARCHIVE_DIR.glob("2026-*.md")) if ARCHIVE_DIR.exists() else []
    last_archive = trim(read_text(archives[-1]), MAX_LAST_ARCHIVE_CHARS) if archives else "(no prior archive — first run)"

    # events.csv canonical ledger — summary only goes to the prompt.
    events_for_context = load_events()
    events_context = events_summary_for_prompt(events_for_context)

    index_html = trim(compress_html_for_context(read_text(INDEX)), MAX_HTML_PER_FILE_CHARS)
    brief_html = trim(compress_html_for_context(read_text(BRIEF)), MAX_HTML_PER_FILE_CHARS)

    date_human = f"{today.day} {today.strftime('%B %Y')}"

    return f"""# Today

Date: {today.isoformat()}
Date (human): {date_human}
Day N: {day_n}
Anchor: Day 1 = 28 February 2026 (Hormuz crisis onset, QatarEnergy Ras Laffan FM)

# Procedure
(See system prompt — full procedure encoded there. Score yesterday's predictions before drafting today's.)

# Methodology (current)

{methodology}

# Sources (tier list)

{sources}

# Knowledge base

{knowledge}

# Backtest log (recent)

{backtest}

# Last archived brief

{last_archive}

# Events database summary (events.csv is the canonical ledger; total count derives from it)

{events_context}

# Current index.html (compressed)

{index_html}

# Current brief.html (compressed)

{brief_html}

---

Now produce today's brief. Score yesterday's predictions before drafting today's. Output only the delimiter blocks listed in the system prompt — nothing else."""


# ---------- main ----------

def main() -> int:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 2

    now_utc = dt.datetime.now(dt.timezone.utc)
    today = now_utc.date()
    day_n = (today - ANCHOR_DATE).days + 1
    date_human = f"{today.day} {today.strftime('%B %Y')}"
    time_utc = now_utc.strftime("%H:%M UTC")
    last_updated_str = f"{today.day} {today.strftime('%b')} · {time_utc}"
    yesterday = today - dt.timedelta(days=1)

    print(f"[update_brief] Today UTC: {today.isoformat()} (Day {day_n})", flush=True)
    print(f"[update_brief] Model: {MODEL} · max_tokens: {MAX_OUTPUT_TOKENS}", flush=True)

    # max_retries=5 with exponential backoff handles transient 429s from the
    # 30k ITPM rate limit; the SDK respects retry-after headers.
    client = Anthropic(api_key=api_key, max_retries=5, timeout=600)
    user_msg = build_user_message(today, day_n)

    print(f"[update_brief] User message length: {len(user_msg):,} chars", flush=True)

    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": MAX_WEB_SEARCHES}],
    ) as stream:
        final = stream.get_final_message()
    text = "\n".join(
        b.text for b in final.content if getattr(b, "type", None) == "text"
    ).strip()

    print(f"[update_brief] Got {len(text):,} chars from model · stop: {final.stop_reason}", flush=True)

    blocks = parse_delimited(text)
    print(f"[update_brief] Parsed {len(blocks)}/{len(ALL_KEYS)} blocks: {sorted(blocks.keys())}", flush=True)

    # Force date/day/timestamp fields from the actual run clock. The model has
    # been observed writing tomorrow's date even when explicitly told today's;
    # script-side override guarantees the masthead always reflects the real
    # last-update moment.
    blocks["DAY"] = str(day_n)
    blocks["DATE"] = date_human
    blocks["LAST_UPDATED"] = last_updated_str
    blocks["MAP_TS"] = f"Day {day_n}"
    print(f"[update_brief] Forced DAY={day_n} DATE='{date_human}' LAST_UPDATED='{last_updated_str}'", flush=True)

    # ---------- events.csv ingest + override of derived blocks ----------
    # events.csv is the canonical ledger. Total counts and chain/type/wave
    # breakdowns are computed from it — the model cannot inflate counts
    # without naming the events that justify them.
    events = load_events()
    new_events = parse_new_events_block(blocks.get("NEW_EVENTS", ""), ANCHOR_DATE)
    events, added = merge_new_events(events, new_events)
    if added:
        write_events(events)
        print(f"[update_brief] events.csv: +{len(added)} new (total: {len(events)})", flush=True)
        for e in added:
            print(f"    + {e.get('date')} · {e.get('entity')} · {e.get('chain')} · W{e.get('wave')}T{e.get('fm_type')}", flush=True)
    else:
        print(f"[update_brief] events.csv: no new events this run (total: {len(events)})", flush=True)

    # OVERRIDE WAVE_DATA, CHAIN_DATA, TYPE_DATA with values derived from events.csv.
    # The model's output for these blocks is discarded — the file is the truth.
    wave_rows = compute_wave_data_from_events(events, day_n)
    if wave_rows:
        blocks["WAVE_DATA"] = render_wave_data_block(wave_rows)
        print(f"[update_brief] WAVE_DATA derived from events.csv · last row: {wave_rows[-1]}", flush=True)
    chain_block = compute_chain_data_from_events(events)
    if chain_block:
        blocks["CHAIN_DATA"] = chain_block
    type_block = compute_type_data_from_events(events)
    if type_block:
        blocks["TYPE_DATA"] = type_block

    missing_critical = [k for k in CRITICAL_KEYS if k not in blocks]
    missing_other = [k for k in ALL_KEYS if k not in blocks and k not in CRITICAL_KEYS]

    if missing_critical:
        print(f"[update_brief] FAIL — missing CRITICAL keys: {missing_critical}", file=sys.stderr)
        print("---- response head ----", file=sys.stderr)
        print(text[:1500], file=sys.stderr)
        print("---- response tail ----", file=sys.stderr)
        print(text[-1500:], file=sys.stderr)
        return 3

    if missing_other:
        print(f"[update_brief] WARN — missing non-critical keys (prior content kept): {missing_other}", flush=True)

    # ---------- apply to HTML ----------
    index_html = read_text(INDEX)
    brief_html = read_text(BRIEF)

    html_blocks = [
        "DAY", "DATE", "LAST_UPDATED", "MAP_TS",
        "TREND", "WAVE_INTENSITY", "LEAD_INDICATOR", "VOLUME_INDEX",
        "ONELINER", "SUMMARY",
        "TILE_1", "TILE_2", "TILE_3", "TILE_4", "TILE_5", "TILE_6",
        "ACTIONS", "WATCHLIST", "SCENARIOS",
        "CATEGORY_1", "CATEGORY_2", "CATEGORY_3",
        "CATEGORY_4", "CATEGORY_5", "CATEGORY_6",
        "FM_TABLE", "WAVE_GRID",
    ]
    js_blocks = [
        "MAP_PINS", "WAVE_DATA", "CHAIN_DATA", "TYPE_DATA",
        "INDUSTRY_DATA", "GOLDEN_SCREW_DATA", "RECENT_EVENTS_DATA",
    ]
    # These arrays are additive-only — script-side merge preserves entries
    # the model omits. Prompt asks for additive behavior too, but defence-in-depth.
    additive_arrays = {"MAP_PINS", "INDUSTRY_DATA", "GOLDEN_SCREW_DATA", "RECENT_EVENTS_DATA"}

    total_replacements = 0
    for k in html_blocks:
        if k not in blocks:
            continue
        content = blocks[k]
        i_html, i_n = replace_block(index_html, k, content)
        b_html, b_n = replace_block(brief_html, k, content)
        index_html, brief_html = i_html, b_html
        total_replacements += i_n + b_n

    for k in js_blocks:
        if k not in blocks:
            continue
        content = blocks[k]
        if k in {"WAVE_DATA", "CHAIN_DATA", "TYPE_DATA"}:
            # These are script-derived from events.csv earlier in main();
            # write directly without merge so events.csv stays authoritative.
            pass
        elif k in additive_arrays:
            existing = extract_js_array(index_html, k)
            content = merge_additive_array(existing, content)
            print(f"[update_brief] Merged {k} (additive)", flush=True)
        i_html, i_n = replace_js_array(index_html, k, content)
        index_html = i_html
        total_replacements += i_n

    # Title updates (use lambda — date_human starts with digits)
    index_html = update_title(index_html, TITLE_PREFIX_INDEX, date_human)
    brief_html = update_title(brief_html, TITLE_PREFIX_BRIEF, date_human)

    # Sanity-check marker balance
    for label, html in [("index.html", index_html), ("brief.html", brief_html)]:
        s, e = count_markers(html)
        if s != e:
            print(f"[update_brief] FAIL — {label} markers unbalanced: {s} START vs {e} END", file=sys.stderr)
            return 4

    write_text(INDEX, index_html)
    write_text(BRIEF, brief_html)
    print(f"[update_brief] Applied {total_replacements} block replacements to HTML", flush=True)

    # ---------- archive yesterday ----------
    archive_path = ARCHIVE_DIR / f"{yesterday.isoformat()}.md"
    if not archive_path.exists() and "ARCHIVE_BODY" in blocks:
        write_text(archive_path, blocks["ARCHIVE_BODY"].strip() + "\n")
        print(f"[update_brief] Archived yesterday: {archive_path.relative_to(REPO)}", flush=True)
    else:
        print(f"[update_brief] Archive skipped (exists or no body)", flush=True)

    # ---------- append backtest entry ----------
    if "BACKTEST_ENTRY" in blocks:
        existing = read_text(BACKTEST)
        new_entry = "\n\n" + blocks["BACKTEST_ENTRY"].strip() + "\n"
        write_text(BACKTEST, existing.rstrip() + new_entry)
        print(f"[update_brief] Appended backtest entry", flush=True)

    # ---------- append reflection entry ----------
    if "REFLECTION" in blocks:
        existing = read_text(REFLECTION)
        new_entry = "\n\n" + blocks["REFLECTION"].strip() + "\n"
        write_text(REFLECTION, existing.rstrip() + new_entry)
        print(f"[update_brief] Appended reflection entry", flush=True)

    # ---------- self-learning log appends ----------
    # Each of these is a markdown delta the script appends to the corresponding
    # log file. The model produces the delta as a normal text block; the script
    # appends rather than overwrites, so history is preserved.
    if "HYPOTHESIS_DELTA" in blocks:
        existing = read_text(HYPOTHESIS)
        delta = blocks["HYPOTHESIS_DELTA"].strip()
        if delta and delta.lower() not in {"none", "n/a", "no change"}:
            write_text(HYPOTHESIS, existing.rstrip() + "\n\n" + delta + "\n")
            print(f"[update_brief] Appended hypothesis delta", flush=True)

    if "SOURCE_RELIABILITY_DELTA" in blocks:
        existing = read_text(SOURCE_RELIABILITY)
        delta = blocks["SOURCE_RELIABILITY_DELTA"].strip()
        if delta and delta.lower() not in {"none", "n/a", "no change"}:
            write_text(SOURCE_RELIABILITY, existing.rstrip() + "\n\n" + delta + "\n")
            print(f"[update_brief] Appended source-reliability delta", flush=True)

    if "METHODOLOGY_DELTA" in blocks:
        existing = read_text(METHODOLOGY)
        delta = blocks["METHODOLOGY_DELTA"].strip()
        if delta and delta.lower() not in {"none", "n/a", "no change"}:
            # Methodology deltas append to the bottom of methodology.md
            # under the delta log header. We don't restructure the rule book;
            # we record the proposed change with provenance.
            write_text(METHODOLOGY, existing.rstrip() + "\n\n" + delta + "\n")
            print(f"[update_brief] Appended methodology delta — RULE CHANGE PROPOSED", flush=True)

    print(f"[update_brief] DONE", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
