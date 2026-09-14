"""One-shot ledger audit, 14 Sep 2026 (Day 199).

Applies the findings of the Day-198 audit to events.csv and writes an
itemised entry to count-log.md so every count change is traceable:

  1. remove 19 near-duplicate / status-reading / corrupted rows
  2. reclassify 2 rows, merge one note
  3. backfill 20 sourced events that the cron missed or rejected
     (10 non-Hormuz global events, 8 Hormuz-linked, 2 replacements)
  4. rewrite events.csv with the bot's quoting convention
  5. set run-state.json to the audited count so the next run's delta ribbon
     is measured from here, and patch the baked ribbon in index.html

Idempotent: re-running after success is a no-op for removals/backfills.
Self-contained (no anthropic dependency).
"""
import csv
import datetime as dt
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
EVENTS = REPO / "events.csv"
COUNT_LOG = REPO / "count-log.md"
RUN_STATE = REPO / "run-state.json"
INDEX = REPO / "index.html"
ANCHOR = dt.date(2026, 2, 28)
COLS = ["day", "entity", "country", "chain", "wave", "fm_type", "volume_kt",
        "is_eu_direct", "source", "notes", "date", "indicator_class", "tier", "hormuz_linked"]


def load():
    with open(EVENTS, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(EVENTS, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") or "" for k in COLS})


def key(r):
    return (r.get("date", "").strip(), r.get("entity", "").strip(), r.get("chain", "").strip())


# ---------------------------------------------------------------- 1. removals
REMOVE = [
    # (date, entity, chain, reason)
    ("2026-08-04", "Rhine River transport", "Inland shipping (chemical/fuel)",
     "duplicate of `2026-08-04 · Rhine River` (same Kaub 21 cm reading)"),
    ("2026-08-05", "BfG / Rhine Federal Institute", "EU inland shipping / chemical / fuel",
     "status reading (Kaub 20 cm) — §5c.2, no threshold crossing beyond the 4 Aug record row"),
    ("2026-08-16", "Rhine River transport", "Inland shipping (chemical/fuel)",
     "status reading (Kaub 14 cm) — §5c.2; the 13 Aug row already carries the trough-phase signal"),
    ("2026-08-25", "Rhine Federal Institute of Hydrology", "Inland shipping / chemical / fuel",
     "corrupted (unquoted comma split source/notes) AND contradicted by source record: Ports Europe reports Kaub 75 cm on 25 Aug; the ~6 cm minimum was 14 Aug"),
    ("2026-05-12", "QatarEnergy (mid-June FM extension)", "LNG / gas",
     "duplicate of `2026-05-12 · QatarEnergy · LNG / gas` (Tadawul filing); the +12 Edison cargoes detail merged into the kept row"),
    ("2026-05-12", "EIA", "Strait of Hormuz / Policy",
     "EIA outlook misclassified as FM; same STEO release as the kept `EIA STEO` row"),
    ("2026-05-15", "Iran IRGC", "Strait / operational control",
     "duplicate (Windward imagery) of `2026-05-15 · Iran IRGC · Strait of Hormuz / Operational` (IRGC statement)"),
    ("2026-05-18", "Iran (PGSA)", "Maritime / Strait toll",
     "duplicate of `2026-05-18 · Iran PGSA · Hormuz Strait / transit toll` (PGSA first-party)"),
    ("2026-05-18", "Iran PGSA", "Maritime / Strait",
     "duplicate of `2026-05-18 · Iran PGSA · Hormuz Strait / transit toll`"),
    ("2026-07-09", "QatarEnergy CEO", "LNG production / Ras Laffan ramp-up",
     "duplicate of `2026-07-09 · QatarEnergy CEO halt · LNG production / Ras Laffan`"),
    ("2026-07-09", "QatarEnergy", "LNG production ramp",
     "duplicate of `2026-07-09 · QatarEnergy CEO halt · LNG production / Ras Laffan`"),
    ("2026-07-14", "Stolt Line (Stolt Magnesium)", "Chemical tanker / Persian Gulf",
     "duplicate (Kpler/Windward) of `2026-07-14 · Stolt Line (Stolt Magnesium) · Chemical tanker` (UKMTO/Reuters)"),
    ("2026-08-05", "Houthis", "Red Sea / tanker shipping",
     "duplicate of `2026-08-05 · Houthi forces · Container / tanker shipping` (NCC WAFA strike)"),
    ("2026-08-08", "Iran Foreign Ministry", "Strait of Hormuz / Shipping",
     "duplicate of `2026-08-08 · Iran / Oman · Strait of Hormuz / shipping routes negotiation`"),
    ("2026-08-08", "Iran Ministry of Foreign Affairs", "Strait of Hormuz shipping coordination",
     "duplicate of `2026-08-08 · Iran / Oman · Strait of Hormuz / shipping routes negotiation`"),
    ("2026-08-22", "Houthis", "Red Sea tanker shipping",
     "cross-date duplicate of `2026-08-18 · Houthi Forces · Refined products / Red Sea shipping` (third Jazan strike, restart to 30 Aug)"),
    ("2026-08-24", "Houthis", "Red Sea / crude oil tanker",
     "duplicate of `2026-08-24 · Houthi Forces · Crude oil tanker / Red Sea shipping` (tanker Amzan)"),
    ("2026-08-24", "Houthis", "Red Sea tanker shipping",
     "duplicate of `2026-08-24 · Houthi Forces · Crude oil tanker / Red Sea shipping` (tanker Amzan)"),
    ("2026-08-24", "Panama Canal Authority", "Container and dry-bulk shipping",
     "corrupted row (advisory text sat in the source column; advisory actually dated 20 Aug) — replaced by the backfilled `2026-08-20 · Panama Canal Authority` row"),
]

# ---------------------------------------------------------- 2. corrections
def apply_corrections(rows):
    log = []
    for r in rows:
        k = key(r)
        if k == ("2026-05-12", "EIA STEO", "Middle East crude production"):
            r["indicator_class"] = "Regulatory"
            log.append("`2026-05-12 · EIA STEO` indicator_class Reserve → Regulatory (agency publication with stable doc ID; not an SPR action). Tier 1 unchanged.")
        elif k == ("2026-05-15", "Iran IRGC", "Strait of Hormuz / Operational"):
            r["indicator_class"] = "Geopolitical"
            r["tier"] = "2"
            r["wave"] = ""
            r["fm_type"] = ""
            log.append("`2026-05-15 · Iran IRGC · Strait of Hormuz / Operational` FM/T1 → Geopolitical/T2 (an IRGC statement is a sovereign signal, not an operator FM).")
        elif k == ("2026-05-12", "QatarEnergy", "LNG / gas"):
            if "Edison" not in r.get("notes", ""):
                r["notes"] = (r.get("notes", "").rstrip(". ") +
                              "; +12 additional cargoes cancelled to Edison (AGBI/CNBC 12 May)")
                log.append("`2026-05-12 · QatarEnergy · LNG / gas` notes merged with the removed duplicate (+12 Edison cargoes).")
    return log


# ------------------------------------------------------------ 3. backfill
# date, entity, country, chain, wave, fm_type, volume_kt, is_eu, source, notes, class, tier, hormuz
BACKFILL = [
    ("2026-05-08", "PT Freeport Indonesia (Grasberg)", "Indonesia", "Copper / gold (Grasberg)", "1", "5", "", "False",
     "PTFI statement 8 May 2026 (Reuters via MINING.COM); FCX quarterly filing reiterates end-2027 (Mining Weekly 12 May)",
     "Full Grasberg ramp-up guided to early 2028 by PTFI (from end-2027) citing ore-handling/logistics rework after groundwater ingress; parent FCX filing the same week stands by end-2027. Output ~40-50% of pre-incident; targets 65% H2 2026 and 80% mid-2027. FM in force since 24 Sep 2025 (8 Sep mud rush, 7 fatalities); 2026 guidance cut by 600 Mlb Cu / 560 koz Au (FCX, Sep 2025)",
     "Restart", "1", "False"),
    ("2026-07-16", "BASF", "Germany", "Plasticizers (DINP / DPHP) / Ludwigshafen", "1", "1", "", "True",
     "Chemical Week 17/24 Aug 2026; chemicalsblog.com",
     "FM on DINP and DPHP plasticizers at Ludwigshafen - first Rhine-season FM of 2026, preceding the surfactants declaration",
     "FM", "1", "False"),
    ("2026-08-05", "BASF", "Germany", "Surfactants / European sites", "1", "3", "", "True",
     "BASF customer notice (dated 29 Jul per Chemical Week); C&EN Business Watch 5 Aug 2026",
     "FM on several surfactants from European sites; raw-material deliveries disrupted by Rhine low water plus extreme heat and drought; BASF deploying low-water vessels and shifting volumes to rail and road",
     "FM", "1", "False"),
    ("2026-08-07", "Covestro", "Germany", "Polyether polyols / Dormagen", "1", "3", "", "True",
     "Covestro statement 7 Aug 2026 (C&EN; PUdaily; Investing.com)",
     "FM on selected polyether polyols at Dormagen: propylene oxide feedstock reaches the site only by barge; reduced-load vessels plus truck and rail could not offset the gap; Covestro moves ~75% of European raw materials and >30% of finished goods on the Rhine",
     "FM", "1", "False"),
    ("2026-08-14", "CMA CGM", "Brazil", "Container shipping / Amazon River (Manaus)", "", "", "", "False",
     "CMA CGM customer advisory (Gazeta da Amazonia 14 Aug 2026; Container News)",
     "Low Water Surcharge US$753/TEU on long-haul Manaus cargo - effective 6 Sep inbound and 5 Oct outbound; Negro/Amazon levels falling faster in August than any recent year except 2024, approaching the 2023 critical levels",
     "Carrier-advisory", "2", "False"),
    ("2026-08-18", "UKMTO", "Strait of Hormuz", "Shipping (all)", "", "", "", "False",
     "UKMTO incident ec569681-62a5-4bed-a639-a939d6363fb9 (Al Jazeera 18 Aug 2026)",
     "Vessel struck by an 'unknown projectile' while transiting the Strait early 18 Aug; engine-room damage; one crew member killed",
     "NAVTEX", "1", "True"),
    ("2026-08-20", "Panama Canal Authority", "Panama", "Container / dry-bulk shipping", "", "", "", "False",
     "ACP Advisory to Shipping 20 Aug 2026 (DTN 2 Sep; WorldCargo News 7 Sep)",
     "Daily slots cut to 9 Neopanamax + 25 Panamax from 3 Sep (34 vs ~36 normal) and 23 Panamax from 15 Sep (32 total); Neopanamax draft 14.63 m TFW from 2 Sep with 14.48 m planned for 1 Oct; cause: below-expected watershed rainfall (El Nino). Replaces the corrupted 24 Aug row",
     "Regulatory", "1", "False"),
    ("2026-08-26", "Ningbo-Zhoushan Port", "China", "Container shipping / port operations", "", "", "", "False",
     "Kuehne+Nagel operational advisory 26-28 Aug 2026",
     "Typhoon Saudel: all Ningbo terminal operations suspended 20:00 26 Aug (empties from 16:00), resumed 15:00 28 Aug (~43 h); highest-level typhoon response; by 1 Sep average vessel wait ~3.45 days and yard occupancy 92-95%",
     "Carrier-advisory", "2", "False"),
    ("2026-08-27", "Port of Shanghai (Yangshan / Waigaoqiao)", "China", "Container shipping / port operations", "", "", "", "False",
     "Kuehne+Nagel operational advisory 27-28 Aug 2026",
     "Typhoon Saudel: Yangshan suspended 06:00 27 Aug to 14:00 28 Aug; Waigaoqiao 14:00 27 Aug to 12:00 28 Aug; landfall southern Zhejiang midday 28 Aug; by 1 Sep average vessel wait ~5.21 days",
     "Carrier-advisory", "2", "False"),
    ("2026-09-01", "Valero Port Arthur refinery", "USA", "Crude refining (385 kb/d)", "", "", "", "False",
     "Hydrocarbon Processing 2 Sep 2026 (people familiar with operations)",
     "Partial power outage on the night of 1 Sep after Tropical Storm Edouard made landfall at Johnson Bayou LA (14:20 CT, 60 mph; 90 mph gust at Port Arthur): AVU-147 CDU shut, AVU-146 at minimum rate. Motiva's 656 kb/d plant ran normally but reported weather-caused equipment interruptions to TCEQ",
     "Industry", "2", "False"),
    ("2026-09-01", "JMIC", "Strait of Hormuz", "Shipping (all)", "", "", "", "False",
     "JMIC Advisory Note 1 Sep 2026 (Al Jazeera 3 Sep; JMIC August statistics)",
     "Threat level severe; traffic 'far below baseline' despite a 'modest uptick from recent lows'; continued risk of drifting or uncharted mines despite US clearance claims. August: 131 open recorded transits (65 eastbound / 66 westbound) plus 611 US-facilitated transits",
     "NAVTEX", "1", "True"),
    ("2026-09-02", "ver.di (German seaports)", "Germany", "Container shipping / port operations", "", "", "", "True",
     "ver.di strike call; Kuehne+Nagel and Bertling client notices 2 Sep 2026",
     "48-hour warning strike from the late shift on 2 Sep (~22:00) to 4 Sep at Hamburg, Bremerhaven, Wilhelmshaven, Bremen, Brake and Emden (Eurogate and NTB at Bremerhaven); wage dispute - ZDS offer 5.1% over 18 months vs ver.di demand 8.2% or EUR 2.50/h over 12 months",
     "Industry", "2", "False"),
    ("2026-09-04", "FNV Havens (Dutch ports)", "Netherlands", "Container shipping / port operations", "", "", "", "True",
     "FNV Havens; Port of Rotterdam Authority via WorldCargo News 4 Sep 2026",
     "Eight-hour stoppage 11:15-19:00 at Rotterdam, Amsterdam and Zeeland; lashing, towage (Svitzer), inspection and cargo handling delayed on water and road; protest against EUR 6.5 bn social-security cuts",
     "Industry", "2", "False"),
    ("2026-09-04", "CMA CGM", "Brazil", "Container shipping / Amazon River (Manaus)", "", "", "", "False",
     "CMA CGM customer advisory 4 Sep 2026 (Container News)",
     "Manaus Low Water Surcharge raised to US$2,315/TEU effective 2 Oct (all equipment types); authorities expect Maximum Recommended Draft restrictions from mid-September; floating pier and barge/storage/pilotage adjustments planned",
     "Carrier-advisory", "2", "False"),
    ("2026-09-05", "US CENTCOM", "Iran / Gulf of Oman", "Crude oil tankers (Iranian)", "", "", "", "False",
     "CENTCOM statement 5 Sep 2026 (CNBC; Washington Post; Al Jazeera)",
     "US fighters and drones struck three Iranian tankers after IRGC ballistic missiles targeted two US Navy warships: M/T Downy (near Kharg) and M/T Stark 1 (near Jask) 'permanently disabled'; M/T Kylo destroyed in the Gulf of Oman and later sank",
     "Geopolitical", "2", "True"),
    ("2026-09-07", "Panama Canal Authority", "Panama", "Container / dry-bulk shipping", "", "", "", "False",
     "ACP announcement 7 Sep 2026 (WorldCargo News)",
     "Planned Neopanamax draft cut to 14.48 m on 1 Oct postponed; 14.63 m TFW maintained for 'continuity of voyage planning'; slot caps unchanged (9 Neopanamax + 25 then 23 Panamax); ACP worst case 27 transits/day",
     "Regulatory", "1", "False"),
    ("2026-09-09", "US CENTCOM / IRGC", "Iran / Gulf of Oman", "Crude oil tankers (Iranian) + Gulf of Oman shipping", "", "", "", "False",
     "CENTCOM and IRGC statements 9 Sep 2026 (Al Jazeera)",
     "Overnight 8-9 Sep the US struck five Iranian tankers (Kaviz, Charminar, Horizon 1, Riesco in the Gulf of Oman; Derya near Kharg) after IRGC attempts on a US warship over two days; Iran claimed strikes on two US vessels and 8 tankers plus 20 missiles at Al-Azraq (Jordan, 18 intercepted); IRGC declared a 'maritime restricted area' from Chabahar into the Gulf of Oman/Arabian Sea; oil above $100/bbl",
     "Geopolitical", "2", "True"),
    ("2026-09-13", "UKMTO", "Strait of Hormuz", "Shipping (all)", "", "", "", "False",
     "UKMTO incident report 13 Sep 2026 (CNBC; CNN; Deccan Herald)",
     "Vessel struck by an unknown projectile while transiting the Strait; fire on board; crew evacuated with the assistance of local authorities",
     "NAVTEX", "1", "True"),
    ("2026-09-13", "Iranian commercial vessel (Qeshm)", "Iran", "Shipping (all)", "", "", "", "False",
     "Iranian state media via CNN / CNBC 13 Sep 2026",
     "Iranian commercial ship hit by a projectile near Qeshm Island early 13 Sep; one dead, three injured (Iranian claim, no Tier-1 confirmation)",
     "Geopolitical", "2", "True"),
    ("2026-09-13", "Iran-Gulf states Oman talks", "Oman", "Strait of Hormuz governance", "", "", "", "False",
     "CNN / CNBC 13 Sep 2026",
     "Oman meeting on managing Strait traffic (set for 14 Sep) postponed 'in the interests of consensus' after the Qeshm strike",
     "Geopolitical", "2", "True"),
]


def main():
    rows = load()
    before = len(rows)
    print(f"events.csv before: {before} rows")

    # 1. removals
    removed = []
    remaining = []
    remove_keys = {(d, e, c): reason for d, e, c, reason in REMOVE}
    for r in rows:
        k = key(r)
        if k in remove_keys:
            removed.append((r, remove_keys[k]))
        else:
            remaining.append(r)
    rows = remaining
    missing = [k for k in remove_keys if k not in {key(r) for r, _ in removed}]
    if missing:
        print(f"  warn: {len(missing)} removal targets not found (already removed?): {missing}")
    print(f"  removed {len(removed)} rows")

    # 2. corrections
    corr_log = apply_corrections(rows)
    print(f"  corrections applied: {len(corr_log)}")

    # 3. backfill
    existing_keys = {key(r) for r in rows}
    added = []
    for d, ent, ctry, chain, wave, fmt, vol, eu, src, notes, cls, tier, hz in BACKFILL:
        if (d, ent, chain) in existing_keys:
            continue
        day_n = (dt.date.fromisoformat(d) - ANCHOR).days + 1
        row = {"day": str(day_n), "entity": ent, "country": ctry, "chain": chain, "wave": wave,
               "fm_type": fmt, "volume_kt": vol, "is_eu_direct": eu, "source": src, "notes": notes,
               "date": d, "indicator_class": cls, "tier": tier, "hormuz_linked": hz}
        rows.append(row)
        added.append(row)
    print(f"  backfilled {len(added)} rows")

    # normalise hormuz_linked casing
    for r in rows:
        r["hormuz_linked"] = "False" if (r.get("hormuz_linked") or "True").strip().lower() == "false" else "True"

    rows.sort(key=lambda r: (r.get("date", ""), int(r.get("day") or 0)))
    save(rows)
    after = len(rows)
    t1 = sum(1 for r in rows if (r.get("tier") or "").strip() == "1")
    t2 = sum(1 for r in rows if (r.get("tier") or "").strip() == "2")
    nonh = sum(1 for r in rows if r.get("hormuz_linked") == "False")
    print(f"events.csv after: {after} rows (T1={t1} · T2={t2} · non-Hormuz={nonh})")

    if not removed and not added and not corr_log:
        print("nothing changed — audit already applied")
        return

    # 4. count-log entry
    body = [
        "\n## 14 Sep · audit · Day 199\n",
        f"**Count:** {before} → {after} ({after - before:+d}) — one-time ledger audit (methodology §5c). "
        "Context: API credit balance exhausted on 7 and 10 Sep (both cadence runs failed all hourly attempts; 9-day gap 4→13 Sep); "
        "13 Sep run added 0 events.\n",
    ]
    if removed:
        body.append(f"\n**Rows removed ({len(removed)}) — duplicates, status readings, corrupted:**")
        for r, reason in removed:
            body.append(f"- `{r.get('date')}` · {r.get('entity')} · {r.get('chain')} · {r.get('indicator_class')}/T{r.get('tier')} — {reason}")
    if corr_log:
        body.append(f"\n\n**Rows corrected ({len(corr_log)}):**")
        for line in corr_log:
            body.append(f"- {line}")
    if added:
        body.append(f"\n\n**Events backfilled ({len(added)}) with provenance (missed or rejected by the cron):**")
        for e in added:
            body.append(
                f"- `{e['date']}` · {e['entity']} · {e['chain']} · {e['indicator_class']}/T{e['tier']} · "
                f"hormuz_linked={e['hormuz_linked']} · source: {e['source']}"
            )
    body.append(
        "\n\n**Process changes shipped with this entry:** tail-anchored NEW_EVENTS parser + `events-quarantine.csv` "
        "(rejected rows re-presented to the model); §5c near-duplicate guard (logged here from now on); full-ledger "
        "dashboard feed (tier tiles previously computed from a 220-row cap: page showed T1=176 vs ledger 215); "
        "rotating non-Hormuz search theme with a script-computed quota; workflow catch-up when a cadence day is missed.\n"
    )
    with open(COUNT_LOG, "a", encoding="utf-8") as f:
        f.write("\n".join(body))
    print("  count-log.md entry appended")

    # 5. run-state + ribbon
    state = {"count": after, "date": "14 September 2026", "ts": "14 Sep · audit", "day": 199}
    RUN_STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    html = INDEX.read_text(encoding="utf-8")
    ribbon = (
        f'<span class="delta-flat">Ledger audited 14 Sep</span> <span class="delta-since">· {before} → {after} '
        f'(−{len(removed)} duplicates/status rows, +{len(added)} backfilled events, {len(corr_log)} reclassified — see count-log.md) '
        f'· {after} total tracked</span>'
    )
    new_html, n = re.subn(
        r"(<!-- BRIEF:EVENTS_DELTA_START -->)(.*?)(<!-- BRIEF:EVENTS_DELTA_END -->)",
        lambda m: m.group(1) + "\n" + ribbon + "\n" + m.group(3),
        html, count=1, flags=re.DOTALL,
    )
    if n:
        INDEX.write_text(new_html, encoding="utf-8", newline="\n")
        print("  index.html delta ribbon patched")
    else:
        print("  warn: EVENTS_DELTA markers not found in index.html")
    print("  run-state.json set to audited count")


if __name__ == "__main__":
    main()
