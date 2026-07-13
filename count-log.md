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


## 22 May · 00:14 UTC · Day 84

**Count:** 166 → 168 (+2)


**Events added (with provenance):**
- `2026-05-22` · Iran PGSA · Maritime/Strait toll regime · W1T6 · source: Windward 19 May
- `2026-05-20` · Strait of Hormuz · Maritime/shipping · W1T2 · source: straits.live 20 May


**Events rejected (validation failed):**
- 2026-05-18 · Iran PGSA official · Maritime/Strait regulatory — REJECTED: invalid indicator_class: 'Signal' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])


## 23 May · 08:22 UTC · Day 85

**Count:** 175 → 180 (+5)


**Events added (with provenance):**
- `2026-05-20` · Windward AIS Tracking · Hormuz Strait / VLCC transit · WT · source: Windward Maritime AI
- `2026-05-18` · Iran PGSA · Hormuz Strait / transit toll · WT · source: PGSA X account / Iran state media
- `2026-05-22` · Oil Markets · Crude oil / pricing · WT · source: Trading Economics
- `2026-05-20` · Iran-Oman · Hormuz Strait / permanent toll framework · WT · source: Trading Economics citing diplomatic reports
- `2026-05-12` · EIA STEO · Middle East crude production · WT · source: EIA Short-Term Energy Outlook (12 May release)


## 1 Jun · 05:12 UTC · Day 94

**Count:** 180 → 183 (+3)


**Events added (with provenance):**
- `2026-06-01` · Iran PGSA · Strait of Hormuz / Maritime toll · W1T6 · source: Windward (blog 27 May)
- `2026-06-01` · US Treasury · Iran policy / Hormuz toll prevention · WT · source: CNN (28 May)
- `2026-06-01` · Trump Administration · Iran ceasefire memo / nuclear talks · WT · source: Axios (28 May)


**Events rejected (validation failed):**
- 2026-06-01 · QatarEnergy · LNG / Gas — REJECTED: FM-class row needs wave 1/2/3; got ''


## 7 Jun · 04:53 UTC · Day 100

**Count:** 183 → 183 (+0)


**Events added:** none


**Events rejected (validation failed):**
- 2026-06-03 · Formosa Petrochemical · Olefins / naphtha — REJECTED: FM-class row needs wave 1/2/3; got ''


## 10 Jun · 00:22 UTC · Day 103

**Count:** 183 → 184 (+1)


**Events added (with provenance):**
- `2026-06-03` · Formosa Petrochemical · Naphtha / petchem · W3T4 · source: ICIS 3 June direct customer communication


**Events rejected (validation failed):**
- 2026-06-03 · KPC (managing director) · Crude oil / refining — REJECTED: invalid indicator_class: 'Signal' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])


## 16 Jun · 05:28 UTC · Day 109

**Count:** 184 → 188 (+4)


**Events added (with provenance):**
- `2026-06-16` · PGSA Status · Strait of Hormuz / Maritime toll · WT · source: PGSA official statement (1 Jun) + Mondaq (26 May)
- `2026-06-16` · Hormuz Transit Volume · Strait of Hormuz · WT · source: IMF PortWatch (7 Jun) + Straits.live (15 Jun)
- `2026-06-16` · War-Risk Insurance · Maritime / Tanker · WT · source: Straits.live (15 Jun)
- `2026-06-16` · Bunker Fuel East of Suez · Bunker / Distribution · WT · source: Manifold Times / Inchcape (9 Jun)


## 19 Jun · 05:20 UTC · Day 112

**Count:** 188 → 192 (+4)


**Events added (with provenance):**
- `2026-06-18` · Trump-Pezeshkian MOU · Strait of Hormuz / Maritime · WT · source: Reuters / White House
- `2026-06-18` · JMIC Threat Downgrade · Hormuz Strait / Maritime · WT · source: JMIC statement
- `2026-06-18` · Saudi VLCC Transits · Crude oil / Hormuz · WT · source: House of Saud analysis, 17-18 Jun
- `2026-06-19` · PGSA Exemption Asymmetry · Strait of Hormuz / Toll regime · WT · source: Windward / House of Saud, 17-19 Jun


**Events rejected (validation failed):**
- 2026-06-18 · QatarEnergy LNG Ramp Announcement · LNG / gas — REJECTED: FM-class row needs wave 1/2/3; got ''
- 2026-06-19 · KPC Force Majeure Lift · Crude oil — REJECTED: FM-class row needs wave 1/2/3; got ''


## 25 Jun · 20:20 UTC · Day 118

**Count:** 192 → 194 (+2)


**Events added (with provenance):**
- `2026-06-19` · Lloyd's Market Consortium · Maritime insurance · WT · source: Lloyd's press release 19 Jun 2026
- `2026-06-22` · Indonesia LPG duty exemption · Naphtha / petchem feedstock · WT · source: ICIS / Ministry of Economic Affairs 22 Jun


**Events rejected (validation failed):**
- 2026-06-22 · Iran PGSA · Strait of Hormuz / Maritime — REJECTED: invalid indicator_class: 'Signal' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])
- 2026-06-22 · Kharg Island crude · Crude oil — REJECTED: invalid indicator_class: 'Signal' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])
- 2026-06-24 · EGA Al Taweelah Recycling · Aluminium (circular feedstock) — REJECTED: FM-class row needs wave 1/2/3; got ''


## 28 Jun · 04:46 UTC · Day 121

**Count:** 194 → 194 (+0)


**Events added:** none


**Events rejected (validation failed):**
- 2026-06-22 · Barzan Plant Second Explosion · LNG / helium / urea co-located — REJECTED: invalid indicator_class: 'Kinetic' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])
- 2026-06-25 · Cargo Vessel Projectile Strike ·  — REJECTED: missing chain
- 2026-06-26 · Strait of Hormuz Post-Strike Status Disputed ·  — REJECTED: missing chain


## 1 Jul · 00:18 UTC · Day 124

**Count:** 194 → 197 (+3)


**Events added (with provenance):**
- `2026-06-28` · Windward AIS · Strait of Hormuz / Maritime transits · WT · source: Windward Maritime Intelligence
- `2026-06-28` · First VLCC Return · Crude oil / Hormuz · WT · source: Windward Maritime Intelligence
- `2026-06-25` · Cargo Vessel Strike · Maritime / Hormuz incident · WT · source: gCaptain / MARAD MSCI


## 4 Jul · 03:57 UTC · Day 127

**Count:** 197 → 200 (+3)


**Events added (with provenance):**
- `2026-07-01` · Windward AIS tracking · Strait of Hormuz / Maritime transits · WT · source: Windward Intelligence · 1 Jul 2026
- `2026-06-25` · Ever Lovely · Maritime / Hormuz incident · WT · source: UKMTO / PGSA.IO / gCaptain · 25 Jun 2026
- `2026-06-22` · Barzan plant · Natural gas / domestic supply · WT · source: QatarEnergy statement · 22–24 Jun 2026


## 7 Jul · 04:13 UTC · Day 130

**Count:** 200 → 202 (+2)


**Events added (with provenance):**
- `2026-07-04` · IRGC · Strait of Hormuz / Maritime · WT · source: Windward Intelligence
- `2026-07-06` · Iran · Crude oil export · WT · source: EO satellite imagery


**Events rejected (validation failed):**
- 2026-07-03 · QatarEnergy · LNG / gas — REJECTED: FM-class row needs wave 1/2/3; got ''
- 2026-07-05 · Windward Intelligence · Maritime transits — REJECTED: invalid indicator_class: '16 outbound); southern corridor preferred; 5 inbound dark' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])


## 10 Jul · 04:09 UTC · Day 133

**Count:** 202 → 208 (+6)


**Events added (with provenance):**
- `2026-07-07` · AL REKAYYAT · LNG / Hormuz shipping · W2T2 · source: Windward MIOC
- `2026-07-07` · WEDYAN · Crude oil / Hormuz shipping · W2T2 · source: UKMTO + Reuters
- `2026-07-08` · US CENTCOM strike · Iran military / Hormuz anti-shipping · WT · source: CENTCOM statement
- `2026-07-09` · IRGC counterstrike · Jordan/US military bases · WT · source: IRGC statement + RFE/RL
- `2026-07-09` · QatarEnergy CEO halt · LNG production / Ras Laffan · W1T5 · source: Bloomberg
- `2026-07-02` · Saudi Aramco / SABIC project cancellation · Petrochemical capex · WT · source: AKM.RU + Saudi Aramco statement


## 13 Jul · 00:07 UTC · Day 136

**Count:** 208 → 210 (+2)


**Events added (with provenance):**
- `2026-07-12` · Cyprus-flagged container ship · Container shipping · WT · source: CENTCOM press release (12 July)
- `2026-07-09` · QatarEnergy CEO · LNG production / Ras Laffan ramp-up · WT · source: Bloomberg / CEO statement (9 July)


**Events rejected (validation failed):**
- 2026-07-12 · IRGC Navy · Strait of Hormuz / governance — REJECTED: invalid indicator_class: '1' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])
- 2026-07-11 · US CENTCOM · Strait of Hormuz / Iranian military strikes — REJECTED: invalid indicator_class: '1' (must be one of ['Analyst', 'Carrier-advisory', 'FM', 'Geopolitical', 'Industry', 'Insurance', 'NAVTEX', 'NOTAM', 'Regulatory', 'Reserve', 'Restart', 'Sanction'])

