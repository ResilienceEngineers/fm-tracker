#!/usr/bin/env python3
"""One-shot Day-81 events.csv schema migration.

Adds two columns:
  - indicator_class: FM | Restart | NOTAM | NAVTEX | Sanction | Insurance |
    Reserve | Regulatory | Industry | Geopolitical
  - tier: 1 (strong signal) | 2 (confirmatory)

Backfills the 128 existing rows with indicator_class=FM and tier=1 (they
all passed the original force-majeure admissibility test under the legacy
methodology). Appends 28 new rows from the Day-81 research pass — formal
NOTAMs, NAVTEX/MSCI advisories, OFAC actions, IEA emergency releases,
Lloyd's JWC listing changes, EU regulatory actions, named industry
statements.

Tier assignment per `methodology.md` Section 5b two-tier framework:
- Tier 1: First-party authority + stable document ID + concrete content +
  empirical predictive lead. All four conditions hold.
- Tier 2: Confirmatory / market-reactive / advisory — fewer than four T1
  conditions but passes admissibility (named source, reproducible
  publication, topical relevance).

Run once, then delete or keep as audit artefact.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EVENTS = REPO / "events.csv"

OLD_COLUMNS = [
    "day", "entity", "country", "chain", "wave", "fm_type",
    "volume_kt", "is_eu_direct", "source", "notes", "date",
]
NEW_COLUMNS = OLD_COLUMNS + ["indicator_class", "tier"]


# Day-81 new events. Day numbers computed from anchor 2026-02-28 = Day 1.
# Pre-anchor events get day <= 0 and are kept for context; they don't enter
# the Three-Waves cumulative time series (wave field blank for non-FM rows).
NEW_EVENTS = [
    # ---------- Sanctions (Tier 1) ----------
    {"day": "-22", "entity": "OFAC (US Treasury)", "country": "USA",
     "chain": "Iran shadow fleet · crude+LPG",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "OFAC recent actions 20260206; Treasury press SB0341",
     "notes": "Initial Iran shadow-fleet designations targeting crude and LPG tankers (pre-crisis)",
     "date": "2026-02-06",
     "indicator_class": "Sanction", "tier": "1"},
    {"day": "-1", "entity": "OFAC (US Treasury)", "country": "USA",
     "chain": "Iranian oil trade",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Federal Register 2026-03988",
     "notes": "OFAC sanctions action including LUMA and NIBA tankers (pre-crisis)",
     "date": "2026-02-27",
     "indicator_class": "Sanction", "tier": "1"},
    {"day": "56", "entity": "OFAC (US Treasury)", "country": "USA",
     "chain": "Iranian petroleum exports",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Treasury press; GovPing 2026-04-24",
     "notes": "19 entities + 19 vessels designated under EO 13902; targets Hengli Petrochemical (Dalian) refinery",
     "date": "2026-04-24",
     "indicator_class": "Sanction", "tier": "1"},
    {"day": "56", "entity": "OFAC (US Treasury)", "country": "USA",
     "chain": "Iranian petroleum exports",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Treasury press 2026-04-24",
     "notes": "General License V — 30-day wind-down for transactions with Hengli Petrochemical (Dalian)",
     "date": "2026-04-24",
     "indicator_class": "Sanction", "tier": "1"},

    # ---------- NOTAM aviation (Tier 1) ----------
    {"day": "1", "entity": "Iran Civil Aviation Organization", "country": "Iran",
     "chain": "Aviation / airspace",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Iran CAO NOTAM; Liveuamap",
     "notes": "Emergency NOTAM closing all Iranian airspace (Tehran FIR / OIIX) to commercial aviation",
     "date": "2026-02-28",
     "indicator_class": "NOTAM", "tier": "1"},
    {"day": "1", "entity": "EASA", "country": "EU",
     "chain": "Aviation / airspace",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "True",
     "source": "EASA CZIB 2026-03 initial issue",
     "notes": "Conflict Zone Information Bulletin for Middle East and Persian Gulf airspace — initial issue",
     "date": "2026-02-28",
     "indicator_class": "NOTAM", "tier": "1"},
    {"day": "54", "entity": "Iran Civil Aviation Organization", "country": "Iran",
     "chain": "Aviation / airspace",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Safe Airspace 22 Apr",
     "notes": "Iranian domestic flights resumed; international routes remain suspended (Tehran FIR partial)",
     "date": "2026-04-22",
     "indicator_class": "NOTAM", "tier": "1"},
    {"day": "62", "entity": "EASA", "country": "EU",
     "chain": "Aviation / airspace",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "True",
     "source": "EASA CZIB 2026-03-R8; Ops Group",
     "notes": "CZIB 2026-03 revision R8 issued; validity extended to 5 May 2026",
     "date": "2026-04-30",
     "indicator_class": "NOTAM", "tier": "1"},
    {"day": "64", "entity": "UAE GCAA + Qatar/Bahrain/Kuwait CAAs", "country": "UAE/GCC",
     "chain": "Aviation / airspace",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Gulf Business 2 May; UAE GCAA",
     "notes": "Full resumption of air traffic operations in UAE; Qatar/Bahrain/Kuwait reopen airspace after large-scale closures",
     "date": "2026-05-02",
     "indicator_class": "NOTAM", "tier": "1"},
    {"day": "74", "entity": "EASA", "country": "EU",
     "chain": "Aviation / airspace",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "True",
     "source": "EASA CZIB 2026-03-R10",
     "notes": "CZIB 2026-03 revised (R10); validity extended to 27 May 2026; recommendations amended",
     "date": "2026-05-12",
     "indicator_class": "NOTAM", "tier": "1"},

    # ---------- NAVTEX / Maritime (Tier 1) ----------
    {"day": "1", "entity": "MARAD (US DOT)", "country": "USA",
     "chain": "Maritime / Hormuz",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "MARAD MSCI 2026-001A",
     "notes": "MSCI Advisory 2026-001A — Strait of Hormuz / Persian Gulf — Iranian military operations and potential retaliatory strikes",
     "date": "2026-02-28",
     "indicator_class": "NAVTEX", "tier": "1"},
    {"day": "16", "entity": "MARAD (US DOT)", "country": "USA",
     "chain": "Maritime / Hormuz",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "MARAD MSCI 2026-001B (date approx)",
     "notes": "MSCI 2026-001B revision — ongoing risk environment; updates to 001A",
     "date": "2026-03-15",
     "indicator_class": "NAVTEX", "tier": "1"},
    {"day": "47", "entity": "MARAD (US DOT)", "country": "USA",
     "chain": "Maritime / Hormuz",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "MARAD MSCI 2026-004 (date approx)",
     "notes": "MSCI 2026-004 — Iranian attacks on commercial vessels (Persian Gulf / Hormuz / Gulf of Oman)",
     "date": "2026-04-15",
     "indicator_class": "NAVTEX", "tier": "1"},
    {"day": "65", "entity": "UKMTO", "country": "UK",
     "chain": "Maritime / Hormuz",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "UKMTO Advisory 040 (JMIC 03 May)",
     "notes": "Bulk carrier attacked by multiple small craft 11nm west of Sirik, Iran; crew safe",
     "date": "2026-05-03",
     "indicator_class": "NAVTEX", "tier": "1"},
    {"day": "67", "entity": "UKMTO", "country": "UK",
     "chain": "Maritime / Hormuz",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "UKMTO Advisory 041 (JMIC 05 May)",
     "notes": "US naval units in Hormuz repel threats; aggressive Iranian hailing noted; mines possible in/near TSS; GNSS interference sporadic",
     "date": "2026-05-05",
     "indicator_class": "NAVTEX", "tier": "1"},
    {"day": "76", "entity": "UKMTO", "country": "UK",
     "chain": "Maritime / Fujairah",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "UKMTO; gCaptain 14 May",
     "notes": "Vessel boarded by unauthorized personnel 38nm NE of Fujairah; taken toward Iranian territorial waters",
     "date": "2026-05-14",
     "indicator_class": "NAVTEX", "tier": "1"},

    # ---------- Insurance (Tier 1 for JWC formal listing, Tier 2 for premium quotes) ----------
    {"day": "3", "entity": "Lloyd's market", "country": "UK",
     "chain": "War-risk insurance / Hormuz",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Lloyd's List LL1156586",
     "notes": "Additional War Risk Premium surged 5× to 1-5% of hull value within 48h of 28 Feb airstrikes; VLCC quotes $10-14M per Hormuz transit",
     "date": "2026-03-02",
     "indicator_class": "Insurance", "tier": "2"},
    {"day": "4", "entity": "Lloyd's Joint War Committee", "country": "UK",
     "chain": "War-risk insurance",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Lloyd's List; LMA",
     "notes": "JWC Listed Areas expanded — Bahrain, Djibouti, Kuwait, Oman, Qatar added; entire Arabian Gulf designated conflict zone",
     "date": "2026-03-03",
     "indicator_class": "Insurance", "tier": "1"},
    {"day": "20", "entity": "Lloyd's CEO", "country": "UK",
     "chain": "Insurance market",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Insurance Journal 19 Mar",
     "notes": "Public statement: critical that Mideast war cover remains available; warns of structural market withdrawal",
     "date": "2026-03-19",
     "indicator_class": "Insurance", "tier": "2"},

    # ---------- Reserve / IEA (Tier 1) ----------
    {"day": "12", "entity": "IEA", "country": "Global",
     "chain": "Crude oil / emergency reserves",
     "wave": "", "fm_type": "", "volume_kt": "400000", "is_eu_direct": "False",
     "source": "IEA news 11 Mar",
     "notes": "Largest-ever coordinated emergency oil stock release — 400 million barrels across IEA member countries",
     "date": "2026-03-11",
     "indicator_class": "Reserve", "tier": "1"},
    {"day": "12", "entity": "US Treasury / DOE", "country": "USA",
     "chain": "Crude oil / SPR",
     "wave": "", "fm_type": "", "volume_kt": "172000", "is_eu_direct": "False",
     "source": "US Treasury; CNBC",
     "notes": "US SPR release of 172 Mbbl announced — 43% of IEA coordinated draw; 41% of pre-release SPR",
     "date": "2026-03-11",
     "indicator_class": "Reserve", "tier": "1"},
    {"day": "70", "entity": "IEA", "country": "Global",
     "chain": "Crude oil / emergency reserves",
     "wave": "", "fm_type": "", "volume_kt": "164000", "is_eu_direct": "False",
     "source": "IEA update; Discovery Alert 8 May",
     "notes": "~164 Mbbl deployed (41% of commitment); adds ~2.5 Mbpd to effective market supply during drawdown",
     "date": "2026-05-08",
     "indicator_class": "Reserve", "tier": "1"},

    # ---------- Regulatory (Tier 1) ----------
    {"day": "7", "entity": "GAIL India", "country": "India",
     "chain": "LNG / gas",
     "wave": "3", "fm_type": "4", "volume_kt": "", "is_eu_direct": "False",
     "source": "Indian Chemical News",
     "notes": "RLNG allocation restriction effective 6 March; impacts Neem Urea downstream production",
     "date": "2026-03-06",
     "indicator_class": "FM", "tier": "1"},
    {"day": "59", "entity": "EU Commission (Roswall)", "country": "EU",
     "chain": "Chemical regulation",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "True",
     "source": "CIRS Group; EU Commission press",
     "notes": "REACH 2.0 comprehensive revision cancelled; cited energy-crisis impact on EU chemical industry",
     "date": "2026-04-27",
     "indicator_class": "Regulatory", "tier": "1"},

    # ---------- Industry association (Tier 2) ----------
    {"day": "26", "entity": "Morgan Stanley", "country": "USA",
     "chain": "Petchem PE / PP",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "Morgan Stanley research note (cited via ChemAnalyst)",
     "notes": "Sell-side quantification: 1.4% of global PE capacity and 1.0% of global PP capacity under FM",
     "date": "2026-03-25",
     "indicator_class": "Industry", "tier": "2"},
    {"day": "55", "entity": "Cefic", "country": "EU",
     "chain": "Chemical industry energy",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "True",
     "source": "Cefic news; EU policy briefing",
     "notes": "Public statement: EU chemical industry 'approaching point of no return'; first plant closures already underway",
     "date": "2026-04-23",
     "indicator_class": "Industry", "tier": "2"},

    # ---------- Geopolitical (Tier 2) ----------
    {"day": "55", "entity": "Fatih Birol (IEA Executive Director)", "country": "Global",
     "chain": "Energy security",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "CNBC 23 Apr interview",
     "notes": "Public statement: 'biggest energy security threat in history'",
     "date": "2026-04-23",
     "indicator_class": "Geopolitical", "tier": "2"},

    # ---------- Airline / carrier advisories (Tier 2 — carrier-issued, not regulator NOTAM) ----------
    {"day": "74", "entity": "Lufthansa Group", "country": "Germany",
     "chain": "Aviation / routes",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "True",
     "source": "The National 12 May",
     "notes": "Suspensions extended: TLV→30 Jun · DXB→11 Jul · AUH/AMM/BEY/DMM/RUH/EBL/MCT/IKA→24 Oct",
     "date": "2026-05-12",
     "indicator_class": "Industry", "tier": "2"},
    {"day": "74", "entity": "KLM", "country": "Netherlands",
     "chain": "Aviation / routes",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "True",
     "source": "The National 12 May",
     "notes": "RUH / DMM / DXB suspended until 28 June; continues avoiding Iran / Iraq / Israel airspace",
     "date": "2026-05-12",
     "indicator_class": "Industry", "tier": "2"},
    {"day": "74", "entity": "Qatar Airways", "country": "Qatar",
     "chain": "Aviation / routes",
     "wave": "", "fm_type": "", "volume_kt": "", "is_eu_direct": "False",
     "source": "The National 12 May",
     "notes": "Iran flight suspensions extended to 30 June 2026",
     "date": "2026-05-12",
     "indicator_class": "Industry", "tier": "2"},
]


def main() -> int:
    if not EVENTS.exists():
        print(f"ERROR: {EVENTS} does not exist", file=sys.stderr)
        return 1

    # Read existing rows in OLD_COLUMNS schema
    with open(EVENTS, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        existing = list(reader)
    print(f"Read {len(existing)} existing rows")

    # Detect whether migration has already been applied
    if existing and "indicator_class" in existing[0]:
        print("Schema already migrated — no-op")
        return 0

    # Backfill existing rows with indicator_class=FM, tier=1
    for row in existing:
        row["indicator_class"] = "FM"
        row["tier"] = "1"

    # Dedupe new events against existing (by entity+chain+date hash)
    import hashlib

    def eid(operator: str, chain: str, date_str: str) -> str:
        key = f"{operator.strip().lower()}|{chain.strip().lower()}|{date_str.strip()}"
        return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]

    seen = {eid(r.get("entity", ""), r.get("chain", ""), r.get("date", ""))
            for r in existing}
    appended = 0
    for ev in NEW_EVENTS:
        h = eid(ev["entity"], ev["chain"], ev["date"])
        if h in seen:
            print(f"SKIP (dupe): {ev['date']} · {ev['entity']} · {ev['chain']}")
            continue
        seen.add(h)
        existing.append(ev)
        appended += 1

    print(f"Appended {appended} new rows (total now {len(existing)})")

    # Write back with new schema
    with open(EVENTS, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=NEW_COLUMNS)
        writer.writeheader()
        for row in existing:
            writer.writerow({k: row.get(k, "") for k in NEW_COLUMNS})
    print(f"Wrote {EVENTS} with schema: {NEW_COLUMNS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
