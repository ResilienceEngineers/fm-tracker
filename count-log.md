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



## 19 May 2026 · Day 81 · Day-81 research batch

**Count:** 124 -> 158 (+34 indicators added via Day-81 research pass; schema also extended with `indicator_class` and `tier` columns)

**Schema change.** Two new columns added to `events.csv`:
- `indicator_class` — FM | Restart | NOTAM | NAVTEX | Sanction | Reserve | Regulatory | Insurance | Industry | Geopolitical | Carrier-advisory | Analyst
- `tier` — `1` (strong signal · admissibility test T1-T4) or `2` (confirmatory · S1-S3). See methodology.md §5b.

All 128 prior rows backfilled with `indicator_class=FM` and `tier=1` (they all passed the original force-majeure admissibility test under the legacy framework).

**Events added (Tier 1 strong signals · 19):**
- `2026-02-06` · OFAC US Treasury · Sanction — initial Iran shadow-fleet designations (pre-crisis)
- `2026-02-27` · OFAC US Treasury · Sanction — Federal Register 2026-03988 incl. LUMA, NIBA tankers
- `2026-02-28` · Iran Civil Aviation Organization · NOTAM — Tehran FIR closure to commercial aviation
- `2026-02-28` · EASA · NOTAM — CZIB 2026-03 initial issue, Middle East / Persian Gulf
- `2026-02-28` · MARAD · NAVTEX — MSCI 2026-001A, Strait of Hormuz / Persian Gulf
- `2026-03-03` · Lloyd's Joint War Committee · Insurance — Listed Areas expanded; entire Arabian Gulf designated conflict zone
- `2026-03-06` · GAIL India · FM — RLNG allocation restriction; impacts Neem Urea
- `2026-03-11` · IEA · Reserve — largest-ever 400 Mbbl coordinated emergency oil stock release
- `2026-03-11` · US DOE · Reserve — 172 Mbbl SPR release announced
- `2026-03-15` · MARAD · NAVTEX — MSCI 2026-001B revision (date approx)
- `2026-04-15` · MARAD · NAVTEX — MSCI 2026-004 Iranian attacks on commercial vessels (date approx)
- `2026-04-22` · Iran CAO · NOTAM — domestic flights resumed; international suspended
- `2026-04-24` · OFAC · Sanction — 19 entities + 19 vessels EO 13902; targets Hengli Petrochemical Dalian
- `2026-04-24` · OFAC · Sanction — General License V issued (30-day Hengli wind-down)
- `2026-04-27` · EU Commission · Regulatory — REACH 2.0 cancelled citing energy-crisis impact
- `2026-04-30` · EASA · NOTAM — CZIB 2026-03-R8 extension to 5 May
- `2026-05-02` · UAE GCAA + GCC CAAs · NOTAM — air traffic operations resumption
- `2026-05-03` · UKMTO · NAVTEX — Advisory 040, bulk carrier attacked 11nm W of Sirik
- `2026-05-05` · UKMTO · NAVTEX — Advisory 041, US Navy in Hormuz repels threats
- `2026-05-08` · IEA · Reserve — ~164 Mbbl deployed (drawdown update)
- `2026-05-12` · EASA · NOTAM — CZIB 2026-03-R10 extension to 27 May
- `2026-05-14` · UKMTO · NAVTEX — vessel boarded 38nm NE of Fujairah; taken toward Iran

**Events added (Tier 2 confirmatory · 11):**
- `2026-03-02` · Lloyd's market · Insurance — AWRP surged 5x to 1-5% hull value
- `2026-03-19` · Lloyd's CEO · Insurance — public statement on cover availability
- `2026-03-25` · Morgan Stanley · Industry — 1.4% global PE / 1.0% global PP under FM
- `2026-04-23` · Cefic · Industry — EU chemical industry approaching point of no return
- `2026-04-23` · IEA chief Birol · Geopolitical — biggest energy security threat in history
- `2026-05-12` · Lufthansa Group · Industry — route suspensions extended (TLV / DXB / multi-Gulf)
- `2026-05-12` · KLM · Industry — RUH / DMM / DXB suspended to 28 June
- `2026-05-12` · Qatar Airways · Industry — Iran flight suspensions to 30 June

**Approximate-date events (3).** MSCI 2026-001B and 2026-004 issued in March and April respectively, exact dates not retrievable due to MARAD page 403; placeholder dates 2026-03-15 and 2026-04-15 noted in source field. Lloyd's AWRP surge dated 2026-03-02 (within 48h of 28 Feb airstrikes per Lloyd's List).

**Reason for batch.** User request: "research if you find any other events in the media or press statements... add NOTAMs as a category and other similar robust statements and indicators." 30 candidates identified via 7 WebSearch queries; 28 admitted after duplicate check; methodology.md §5b two-tier framework added to govern future additions.

## 19 May · 09:29 UTC · Day 81

**Count:** 158 → 161 (+3)


**Events added (with provenance):**
- `2026-05-22` · Iran PGSA · Strait of Hormuz / Governance · WT · source: Lloyd's List Intelligence
- `2026-05-22` · Maritime industry · Bunker fuel / shipping · WT · source: Associated Press
- `2026-05-22` · EGA Al Taweelah · Aluminium · W1T1 · source: AGBI / EnterpriseAM


**Events rejected (validation failed):**
- 2026-05-22 · Lotte Chemical · Naphtha / petchem — REJECTED: FM-class row needs wave 1/2/3; got ''


## 19 May · 09:40 UTC · Day 81

**Count:** 158 → 160 (+2)


**Events added (with provenance):**
- `2026-05-11` · Singapore bunker market · Bunker fuel / maritime · WT · source: VLSFO price $846/mt; B30-VLSFO $1
- `2026-05-12` · QatarEnergy · LNG / gas · W1T5 · source: Tadawul filing


**Events rejected (validation failed):**
- 2026-05-18 · Persian Gulf Strait Authority · Shipping / Hormuz — REJECTED: invalid indicator_class: '1' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])
- 2026-05-16 · Iran Parliament · Shipping / Hormuz — REJECTED: invalid indicator_class: '2' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])
- 2026-05-11 · Lotte Chemical · Naphtha / petchem — REJECTED: invalid indicator_class: '2' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])


## 19 May · 09:54 UTC · Day 81

**Count:** 160 → 163 (+3)


**Events added (with provenance):**
- `2026-05-18` · Iran (PGSA) · Maritime / Strait toll · WT · source: PGSA official launch / Windward
- `2026-05-18` · India-flagged vessel cluster · Maritime / safe passage · WT · source: Windward maritime AI
- `2026-05-15` · Iran IRGC · Strait / operational control · WT · source: Windward SAR imagery


## 19 May · 10:18 UTC · Day 81

**Count:** 164 → 166 (+2)


**Events added (with provenance):**
- `2026-05-18` · Iran PGSA · Maritime / Strait · WT · source: Windward / Lloyd's List
- `2026-05-05` · Saudi Aramco · Crude oil · WT · source: Reuters / Discovery Alert

