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

import datetime as dt
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
ARCHIVE_DIR = REPO / "daily-briefs"

ANCHOR_DATE = dt.date(2026, 2, 28)  # Day 1 = 28 Feb 2026
TITLE_PREFIX_INDEX = "Force Majeure Tracker — Supply Chain Crisis · "
TITLE_PREFIX_BRIEF = "Deep brief — Force Majeure Tracker · "

MODEL = os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5-20251001")
# Haiku 4.5 has a much higher Tier-1 ITPM ceiling than Sonnet 4.6 (Sonnet
# is 30k ITPM on this key, which can't fit one tool-use cycle). Haiku
# handles the structured-block output cleanly and supports web_search.
MAX_OUTPUT_TOKENS = int(os.environ.get("CLAUDE_MAX_TOKENS", "16000"))
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
    "TREND", "WAVE_INTENSITY",
    "ONELINER", "SUMMARY",
    "TILE_1", "TILE_2", "TILE_3", "TILE_4", "TILE_5", "TILE_6",
    "ACTIONS", "WATCHLIST", "SCENARIOS",
    "CATEGORY_1", "CATEGORY_2", "CATEGORY_3",
    "CATEGORY_4", "CATEGORY_5", "CATEGORY_6",
    "FM_TABLE", "WAVE_GRID",
    "MAP_PINS", "WAVE_DATA", "CHAIN_DATA", "TYPE_DATA",
    "BACKTEST_ENTRY", "ARCHIVE_BODY",
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
        if "BRIEF:MAP_PINS" in body or "BRIEF:WAVE_DATA" in body or "BRIEF:CHAIN_DATA" in body or "BRIEF:TYPE_DATA" in body:
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

   **(d) Stock-exchange filings** — Tadawul / Bursa Saudi / BSE / NSE / KOSPI / SGX / TSE / LSE / NYSE for FM-related disclosures from the operators in (a).

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

**HARD RULE:** After web-search calls complete, your visible text response must contain ONLY delimiter blocks. No preamble. No "Let me compile...". No "Key findings:". No bullet lists outside blocks. No commentary, EVER, outside ###BEGIN/###END markers. The first non-tool-call character of your text response must be `###BEGIN:`. The last must be `###`.

You MUST emit every block in the list below in this exact order. Missing CATEGORY blocks have caused build failures previously — produce them all even if content repeats yesterday's where nothing changed.

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
22. **WATCHLIST** — full `<div class="watch">...</div>` with five `<div class="row">` children (n / body / when).
23. **SCENARIOS** — three `<div class="sc">` children only (no outer wrapper). Probabilities sum to 100.
24. **FM_TABLE** — full `<table class="fmtable">...</table>` for the last 14 days; columns: Operator, Site/Chain, Wave, Type, Status, Date, Source.
25. **WAVE_GRID** — full `<div class="wave">...</div>` with four `<div class="wcell">` children (T+0 / T+7 / T+30 / T+90).
26. **MAP_PINS** — JS array contents (no surrounding `[` / `]`), one object per line, format: `{ name: "...", lat: NN, lon: NN, status: "red"|"amber"|"green", note: "...", chain: "..." },`.
27. **WAVE_DATA** — JS array contents (no surrounding `[` / `]`), format: `[day, w1_cum, w2_cum, w3_cum]`. Append today's row to whatever was provided; do not regenerate history.
28. **CHAIN_DATA** — JS array contents (no surrounding `[` / `]`), format: `{ name: "...", n: NN },` — top 12 chains by cumulative count.
29. **TYPE_DATA** — JS array contents (no surrounding `[` / `]`), format: `{ name: "...", n: NN, color: "#hex" },` — six categories.
30. **BACKTEST_ENTRY** — markdown block to append to backtest-log.md. Header `## YYYY-MM-DD (Day N)`, prior-prediction scoring, today's Trend/Wave with confidence, today's Actions/Watchlist/Scenarios in scorable form, Surprise factor.
31. **ARCHIVE_BODY** — markdown body for daily-briefs/YYYY-MM-DD.md. Mirror the template: trend / wave intensity / oneliner / summary / 6 categories / actions / watchlist / FM table / wave grid.

Output ONLY the 31 delimiter blocks above, in order. No preamble. No postamble. No commentary anywhere outside ###BEGIN/###END markers.
"""


def build_user_message(today: dt.date, day_n: int) -> str:
    methodology = trim(read_text(METHODOLOGY), MAX_METHODOLOGY_CHARS)
    sources = trim(read_text(SOURCES), MAX_SOURCES_CHARS)
    knowledge = trim(read_text(KNOWLEDGE), MAX_KNOWLEDGE_CHARS)
    backtest = trim(read_text(BACKTEST), MAX_BACKTEST_CHARS)

    archives = sorted(ARCHIVE_DIR.glob("2026-*.md")) if ARCHIVE_DIR.exists() else []
    last_archive = trim(read_text(archives[-1]), MAX_LAST_ARCHIVE_CHARS) if archives else "(no prior archive — first run)"

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

    today = dt.datetime.now(dt.timezone.utc).date()
    day_n = (today - ANCHOR_DATE).days + 1
    date_human = f"{today.day} {today.strftime('%B %Y')}"
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
        "TREND", "WAVE_INTENSITY", "ONELINER", "SUMMARY",
        "TILE_1", "TILE_2", "TILE_3", "TILE_4", "TILE_5", "TILE_6",
        "ACTIONS", "WATCHLIST", "SCENARIOS",
        "CATEGORY_1", "CATEGORY_2", "CATEGORY_3",
        "CATEGORY_4", "CATEGORY_5", "CATEGORY_6",
        "FM_TABLE", "WAVE_GRID",
    ]
    js_blocks = ["MAP_PINS", "WAVE_DATA", "CHAIN_DATA", "TYPE_DATA"]

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

    print(f"[update_brief] DONE", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
