# Count change log — events.csv

**Status:** Append-only audit trail. Every change to the canonical event count is logged here with the specific events that drove the delta. The dashboard total at any moment equals the row count of `events.csv`; this file explains how that number got there.

Schema per entry:
- Run timestamp (UTC)
- Day N
- Prior count → new count (delta)
- Events added this run (one bullet each, with source)
- Events rejected this run (with validation reason)

For the full forensic explanation of why this ledger exists (and why the dashboard total moved from 160 to 124 on Day 81), see [`count-audit.md`](count-audit.md).

---

## 2026-05-19 · Day 81 · Architectural transition

**Count:** legacy 160 (model-asserted, unverifiable) → 114 (Day-55 dataset seed) → 124 (with 10 backfilled post-Day-55 events).

**Reason for transition.** The legacy `WAVE_DATA` total was the model's running estimate of cumulative events, with a monotonic-merge guard that prevented decreases but did not validate against an event-level ledger. There was no row-by-row audit trail. Inflation drift could not be detected.

Today the architecture flipped: `events.csv` is the canonical ledger. The dashboard total is computed as `row_count(events.csv)`. The model can no longer write counts directly — it proposes new events via the `NEW_EVENTS` block, the script validates each row (required fields: entity, chain, date, wave 1–3, fm_type 1–6, source attribution), dedupes by hash of `operator|chain|date`, and appends only validated rows. Every count change is logged here.

**Events seeded into events.csv on Day 81:**
- 114 rows from `Felsberger_FM_dataset_Day55.csv` (Marco's hand-curated Day-1 to Day-55 dataset).
- 10 post-Day-55 events the bot had been tracking in `RECENT_EVENTS_DATA` but which never appeared in the count:
  - Day 58 (25 Apr) · Saudi Aramco · Crude oil · W1T5 · +$19.50/bbl May Arab Light premium (sovereign signal) · Bloomberg; Daily News Egypt
  - Day 64 (2 May) · KAFCO · Urea/fertilizer · W1T5 · First Hard restart, 1800 t/day ammonia + urea · Operator statement; Reuters
  - Day 65 (3 May) · Lotte Chemical · Naphtha/petchem · W3T5 · Yeosu restart delayed 18 May → 29 May · Seoul Economic Daily; Maybank IB
  - Day 66 (4 May) · US Project Freedom · Crude oil · W1T6 · US Navy escorting merchants through Strait · NPR; AP
  - Day 68 (6 May) · US Navy · Crude oil · W1T6 · Project Freedom paused for nuclear talks · NPR; AP
  - Day 69 (7 May) · EGA · Aluminium · W1T5 · Rehabilitation start confirmed end-May; 12-month recovery · EGA CEO; Al Bayan
  - Day 73 (11 May) · Trump administration · Industrial/other · W1T6 · Ceasefire "on massive life support" · CNN; Reuters
  - Day 74 (12 May) · QatarEnergy · LNG/gas · W1T5 · FM extended through early July; +12 cargoes cancelled · AGBI; CNBC
  - Day 74 (12 May) · Maritime industry · Maritime/port · W3T4 · First explicit Type 4 Distribution signal; Singapore bunker $800/t · WFSB; WaPo; Euronews
  - Day 75 (13 May) · Saudi Aramco · Crude oil · W1T5 · +$15.50/bbl June Arab Light premium · Reuters

**The unaccounted-for 36 events (160 − 124).** No row-level record. These were the model's running estimate accumulating across runs without provenance. The legacy number is retired. Going forward, every count change appears below this entry with the events that drove it.

---

## 19 May · 08:37 UTC · Day 81

**Count:** 124 → 128 (+4)


**Events added (with provenance):**
- `2026-05-15` · Iran IRGC · Strait of Hormuz / Operational · W1T6 · source: IRGC statement
- `2026-05-12` · EIA · Strait of Hormuz / Policy · W1T6 · source: EIA STEO May 2026
- `2026-05-11` · Lotte Chemical · Naphtha / petchem · W1T5 · source: Seoul Economic Daily KOSPI filing
- `2026-05-06` · Maritime industry · Bunker fuel / Type 4 Distribution · W3T4 · source: S&P Global Platts

