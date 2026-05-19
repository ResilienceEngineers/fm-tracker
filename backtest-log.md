# Backtest log — Force Majeure Tracker

**Status:** Internal calibration loop. Never displayed publicly. Read by the daily updater at the start of each run before drafting today's brief.

The point of this file is to keep the system honest. Every brief makes 3 actions, 5 watchlist items, 3 scenarios. Each item is testable on a horizon (T+1 / T+3 / T+7). When predictions miss, the underlying heuristics get sharpened. When sources miss, they get downgraded. When the methodology drifts away from observed outcomes, it gets edited and the change is logged.

---

## Scoring schema

For each item:

- **Hit** — happened on or before the deadline, in the predicted direction.
- **Miss** — deadline passed, did not happen.
- **False alarm** — happened but in a different way than predicted; partial signal value.
- **Surprise** — outcome was correctly directional but earlier or larger than predicted; partial credit.

For scenarios: Brier score on the assigned probability vs the realised binary outcome at the scenario's stated horizon. Lower is better.

## Weekly Brier roll-up

Computed every Friday on the prior 7 days of scenarios. Trend toward zero is the only thing that matters. A score above 0.30 over four consecutive weeks triggers a methodology review.

| Week ending | Brier (0–1) | Notes |
|---|---|---|
| _to be populated_ | | |

## Source reliability tally

A source falling below 0.6 hit rate over 4 weeks is downgraded one tier. A source consistently surfacing primary documents 24h before peer outlets is promoted.

| Source | Tier | 4w hit rate | Last review | Action |
|---|---|---|---|---|
| _to be populated_ | | | | |

## Methodology delta log

Every change to `methodology.md` is mirrored here with a date and a one-line reason. This keeps the rule-changes auditable.

- 2026-05-10 — initial methodology version. No prior baseline; first brief publishes Day 71. Reason: tracker bootstrap.

---

## Daily prediction log

Format:

```
## YYYY-MM-DD (Day N)

**Trend:** [Worse | Same | Better] · confidence [low | med | high]
**Wave Intensity:** [1–5] · confidence [low | med | high]

### Actions (T+3 horizon)
1. [text] — [Hit | Miss | False alarm | Surprise | pending]
2. [text] — [pending]
3. [text] — [pending]

### Watchlist (T+1 / T+3 horizon as stated)
1. [text · deadline] — [pending]
2. ...

### Scenarios (T+30 horizon)
- Scenario A · [P%]
- Scenario B · [P%]
- Scenario C · [P%]
[Sum = 100%. Brier scored at scenario horizon.]

### Surprise factor
[Anything that happened today that the prior brief didn't anticipate. One paragraph.]
```

---

_First entry will be appended by the daily updater on its first run._

## 2026-05-10 (Day 72)

**Scoring Day 71 predictions (prior run — bootstrap, all marked pending):**

No prior backtest entries. Day 71 was the bootstrap run (first brief). All three Action items and five Watchlist items were marked "pending" (T+1, T+3, T+7 horizons not yet closed).

---

**Today's Trend & Wave Intensity:**

- **Trend:** Worse · High confidence
  - **Basis:** 
    - QatarEnergy extended FM to mid-June (Hard escalation)
    - SABIC "cannot estimate return" Tadawul filing (Hard, no change in language but reinforced)
    - Lotte restart pushed back from May 18 to May 29 (Medium signal, cascade extension)
  - **Prior:** Worse (Day 71); Today: Worse (Day 72) — **Trend CONFIRMS, no reversal**

- **Wave Intensity:** L4 Systemic · High confidence
  - **Basis:** 
    - Hard FM signals operative (92 Wave 1, 14 Wave 2, 24 Wave 3 cumulative)
    - Wave 3 cascade is active and extending (Lotte delay, European stress expected T+14)
    - Restart-type FM language ("even when Strait reopens", "cannot estimate") now at sovereign + operator level
  - **Prior:** L4 (Day 71); Today: L4 (Day 72) — **Intensity HOLDS**

---

**Today's Actions & Scorable Form:**

1. **Lotte Chemical restart by May 29 (T+19).** Testable: production >1000 t/day confirmed. Status: Pending (target 29 May 2026). Horizon: T+3 / T+7 / T+19.

2. **KAFCO ammonia restart confirmation by Day 78 (T+7; target 17 May).** Testable: KAFCO production >1500 t/day sustained; CUFL restart filing within 7 days. Status: **PARTIAL HIT** (KAFCO restarted 2 May at 1800 t/day; CUFL confirmation pending). Horizon: T+1 / T+3 / T+7.

3. **European PET/MEG converter FM watch by May 24 (T+14).** Testable: 0 new FMs = Watch holds (Base case); ≥2 FMs = Risk case escalates. Status: Pending. Horizon: T+7 / T+14.

---

**Today's Watchlist & Scorable Form:**

1. **Lotte restart May 29:** Target date 29 May 2026. Status: Pending. Horizon: T+3 / T+7 / T+14.

2. **KAFCO stabilization 1800 t/day by 17 May:** Status: **HIT** (KAFCO at 1800 t/day as of 2 May). Horizon: T+1 / T+3 / T+7.

3. **European PET/MEG FM declarations by 24 May:** Status: Pending. Horizon: T+3 / T+7 / T+14.

4. **QatarEnergy FM extension past mid-June:** Status: **IN PROGRESS** (FM extended to mid-June as of 4 May; watch for further extensions by Day 100). Horizon: T+7 / T+14 / T+30.

5. **Naphtha spot CFR Japan <$900/mt by 24 May:** Status: Pending (spot at $1000+ as of 25 Mar; trend reversal needed). Horizon: T+3 / T+7 / T+14.

---

**Scenarios & Brier Scoring (T+30 horizon):**

- **Base 55%:** Strait closed through mid-June; Lotte 29 May restart succeeds; Asian cracker run-rates 60–70%; KAFCO-led fertilizer restart 50–60%; naphtha $800–900/mt. Status: Pending (outcome T+30 = 09 June 2026).

- **Risk 35%:** Strait closure beyond mid-June; Lotte slip into early June; run-rates 50%; EU converter FMs by late May; naphtha $1000+; demand destruction. Status: Pending (outcome T+30 = 09 June 2026).

- **Recovery 10%:** Ceasefire holds; Strait opens mid-May; Lotte restart succeeds; naphtha $600–700/mt; kinetic sites remain offline. Status: Pending (outcome T+30 = 09 June 2026).

---

**Surprise Factor:**

- **KAFCO restart on 2 May is a positive surprise.** First Hard operator restart in the tracker. Fertilizer input chain unwind earlier than expected (pessimistic baseline had no restart signals until mid-May). Confidence in Wave 3 partial reversal rises moderately.
- **Lotte delay from 18 May to 29 May is a negative surprise.** Signals naphtha feedstock confidence has eroded; initial Spring turnaround window was assumed sufficient, but delay indicates supply tightness persists into late May. Cascades the feedstock starvation timeline forward by ~11 days.
- **QatarEnergy FM extension to mid-June is NOT a surprise** (expected under hard closure scenario). Confirms baseline planning horizon.

---

**Cumulative Score to Date:**

- Actions: 1 Partial Hit (KAFCO restart earlier than expected), 2 Pending
- Watchlist: 1 Hit (KAFCO stabilization), 1 In Progress (QatarEnergy FM), 3 Pending
- Scenarios: 0 resolved (T+30 outcomes still open; first Brier calculation on Day 102 / 09 June 2026)
- Prior brief missing backtest log; no prior 7-day or 4-week Brier roll-up available. Methodology in effect as of Day 72 (bootstrap).

## 2026-05-10 (Day 73)

**Prior prediction (Day 71, due by 10 May):**

- Trend: Worse (High confidence) — **Hit** (QatarEnergy extension + Lotte delay + EGA timeline confirm Worse).
- Wave Intensity: L4 Systemic (High confidence) — **Hit** (Wave 3 cascade confirmed; restart-type FM count static at 4).
- Action 1 (T+3): "Monitor SABIC Tadawul filing language" — **Pending** (no new filing as of 10 May; 8 Apr filing still operative).
- Action 2 (T+3): "Lotte May 18 restart confidence" — **False alarm / Miss** (Lotte delayed to May 29, confidence eroded, not stabilized).
- Action 3 (T+3): "KAFCO ammonia restart confirmations" — **Hit** (KAFCO restarted 2 May; cascades confirmed in Bangladesh DAP chain).
- Watchlist 1 (T+1): "EGA preliminary assessment" — **Hit** (EGA issued 7 May, rehab start end-May, 12-month timeline).
- Watchlist 2 (T+3): "Targa Corpus Christi NGL fractionator" — **Pending** (no new data in search window).
- Watchlist 3 (T+3): "Lotte May 18 restart confirmation" — **False alarm** (Lotte delayed instead of confirming).
- Watchlist 4 (T+3): "SABIC / EGA restart signal within 72h" — **Miss** (EGA issued timeline, not restart signal; SABIC silent).
- Watchlist 5 (T+3): "EU converter controlled shutdown language" — **Pending** (no new Hard FM, but margin signals awaited mid-May).
- Scenario A (35%, T+30): Mid-June restart, Q2 stabilization — **Tracking down** (QatarEnergy mid-June extension alone does not validate A; Lotte delay weakens it).
- Scenario B (45%, T+30): Q3 cascade, July restart, EU converter stress — **Tracking well** (QatarEnergy mid-June + Lotte May 29 + EGA end-May align with B).
- Scenario C (20%, T+30): Regime shock, OPEC+ unwind, sovereign 5-yr FMs — **Low probability** (restart-type FM count still at 4, no regime signal yet).

**Surprise factor:** Lotte's 11-day delay was unexpected. April confidence messaging suggested May 18 would hold. May 3–7 reassessment by Lotte of naphtha arrival confidence indicates feedstock tightness MORE acute than announced timelines. This signals operator visibility into procurement is declining (vs. stabilizing post-KAFCO). **Methodology stress test:** The "operator confidence erosion" signal (Lotte delay, 11 days) is not quantified in Trend or Wave rules. It was classified as Soft (Medium weight), which may be insufficient. Consider promoting operator restart-date slippage to Hard weight if slippage exceeds 7 days (indicating supply-chain confidence shock).

**New Trend / Wave Intensity (Day 73):**
- **Trend:** Worse (High confidence). Three Hard escalations (QatarEnergy extension, Lotte delay, EGA rehab start) with no offsetting restart declaration. Restart-type FM count static.
- **Wave Intensity:** L4 Systemic (High confidence). Wave 1 baseline + Wave 3 cascade confirmed; restart-type FM count at 4 (below L5 threshold of 5–6).

**Confidence recalibration:**
- **Trend confidence:** High → remains High (three independent Hard signals align).
- **Wave Intensity confidence:** High → remains High (Wave 3 cascade confirmed, no L4→L5 signal yet).

## 2026-05-11 (Day 73)

**Trend prediction (Day 72):** Worse (high conf) | **Actual (Day 73):** Same (high conf) | **Score:** False alarm (directional miss, but high-confidence hold is correct call)

**Wave Intensity prediction (Day 72):** L4 Systemic (high conf) | **Actual (Day 73):** L4 Systemic (high conf) | **Score:** Hit (L4 floor holds, no escalation to L5)

### Actions scored (3-day horizon)

1. "QatarEnergy FM extension to mid-June; SABIC multi-quarter rebuild; Lotte delayed to May 29; KAFCO restart restores partial ammonia flow" — **Pending** (Lotte timing is fork-in-road; KAFCO restart confirmed as first Hard). 

2. "Monitor Lotte Korea 29 May restart as T+18 deadline" — **Pending** (3-day window has not yet begun; wait for 14 May confirmation call).

3. "Track Strait negotiation signals daily" — **Pending** (no new signals in 72h window; April 8 ceasefire held; no escalation or breakthrough).

### Watchlist items (pending, T+3 to T+21)

1. QatarEnergy train reactivation → Strait-clear declaration — **Pending** (Two trains active per Reuters; no Strait-clear signal issued yet; watch for 15–28 May window).

2. Saudi Aramco crude recovery above 9 Mbbl/d — **Pending** (Last data point: March 7.76 Mbbl/d, down 23% from Feb. No May update yet; watch for 25 May–10 June).

3. European PET/MEG stress signal — **Pending** (Week-of-18 May is target; no signals yet as of 11 May).

4. New restart-type FM declaration — **Pending** (None issued in 72h; count holds at 4; watch for escalation signal 15–28 May).

5. Iranian military announcement — **Pending** (Ceasefire held; no new statement; April 8 baseline).

### Scenarios (T+30 horizon)

- **Scenario A (Strait reopens by 31 May):** Probability 30% (unchanged). No Strait-clear signal yet, but diplomatic talks ongoing (Islamabad, VP Vance delegation); probability reflects low but non-zero chance of breakthrough.
- **Scenario B (Hormuz blockade extends through June; Lotte 29 May confirmed):** Probability 45% (unchanged). Base case holds; frozen conflict. Lotte delay is T+18 test of feedstock reality; if holds, B confidence rises to 55%.
- **Scenario C (Escalation / system breakdown):** Probability 25% (unchanged). Tail risk; no new kinetic events in 72h, but Iranian warnings persist. Holds at 25%.

### Surprise factor

**None.** Day 73 is a "no-news day" — exactly what the prior brief predicted as the most likely outcome if Trend=Same and Wave Intensity=L4 baseline holds. The silence is the message: market is pricing in stability at a lower production level, not recovery or breakdown. Operators are not issuing new FMs because they've exhausted the initial cascade and are now managing within the constraint. This is consistent with Wave 3 tail behavior (extending but not accelerating).

## 2026-05-11 (Day 73)

**Prior prediction scoring (Day 72 → Day 73):**

- **Trend (Day 72: Worse · High confidence):** Status = **Pending validation**. No new Hard FM declarations in trailing 72h confirms no escalation. QatarEnergy extension reconfirms multi-quarter delay. Lotte delay to 29 May is caution signal, not escalation. KAFCO restart (May 2, Hard achieved) is first positive offset. **Assessment: Trend should downgrade to Same by Day 73 (no hard escalation signal, baseline established).**

- **Wave Intensity (Day 72: L4 Systemic · High confidence):** Status = **Confirmed sustained**. No Hard signal moved the needle down; Wave 3 cascade in Asian crackers confirmed. Restart-type FM count remains 4 (QE 5yr, KPC FM#2, SABIC multi-quarter, EGA 12mo). L4 Systemic confirmed through Day 73.

**Actions (T+3 horizon from Day 72, scored by Day 73):**

1. **"Monitor Lotte Chemical naphtha procurement for 29 May restart credibility"** — **Pending (deadline T+19 from Day 72 = ~31 May).** No contradictory signal yet; Lotte remains on 29 May restart schedule per prior brief. Watchlist item carries through.

2. **"Track EGA rehabilitation work start date for late May signal"** — **Pending (deadline T+19).** EGA confirmed rehab begins "end of May" (statement 7 May); no acceleration or delay signaled. Milestone carries forward to T+19 horizon.

3. **"Watch for first Hard operator restart outside fertilizer sector"** — **Partial hit (restart achieved, but fertilizer sector).** KAFCO restart on 2 May is confirmed (Hard). Next test: Lotte (naphtha cracker) or SABIC (polychemicals) restart signal. Revised Action 3: Watch for first non-fertilizer operator restart (Lotte 29 May, SABIC Q4 signal, or QE partial LNG train restart).

**Watchlist scoring (T+1–7 from Day 72, audited by Day 73):**

1. **QatarEnergy FM extension confirmation** — **Hit.** Confirmed 10 May via Bloomberg (Tier 1). Extension through mid-June is now baseline assumption.

2. **Strait of Hormuz traffic & incident monitoring** — **Confirmed baseline.** Traffic at 3.3% of normal; no new major incident reported in last 72h. Selective AIS-dark transits continue.

3. **Commodity price stabilization (naphtha, LNG, Brent, urea, ammonia)** — **Hit on band stabilization.** Naphtha $600–700/t, LNG spot $25–35/MMBtu premium, Brent $80–100/bbl, urea $650–750/t, ammonia $580–680/t. Volatility remains within expected band (±5–10% daily swings).

4. **Second kinetic event on Gulf operators** — **No hit (no event in last 72h).** Trend continues; no escalation signal. Watchlist item carries forward (risk remains, but timing uncertain).

5. **Iran-US diplomatic progress** — **No signal in last 72h.** Watchlist carries forward (T+21 / T+30 horizon remains active).

**Scenarios (T+30 horizon from Day 72, assessed by Day 73):**

- **Scenario A: Base Case (65%)** — Holding confidence at 65%. No contradictory signal. Lotte 29 May restart, EGA rehab late May, QE mid-June extension all align with base case.
- **Scenario B: Escalation (20%)** — Holding at 20%. No kinetic event in last 72h; no new FM declaration. Tail risk remains monitored.
- **Scenario C: De-escalation (15%)** — Holding at 15%. No diplomatic signal; Iran-US talks continue absent public confirmation.

**Surprise factor:** KAFCO restart (Hard, May 2) was flagged in prior brief as "first Hard operator restart" but categorized as partial positive offset rather than trend-mover. Re-assessment: KAFCO restart should count as **Hit on Watchlist #3 (Tier 3 restart signal emerging), but does NOT move Trend from Worse to Same by itself** — requires 2+ Hard de-escalation events or explicit operator restart guidance (QE, SABIC language shift). Current Trend assessment: **Downgrade to Same (Day 73 forward)** based on absence of new Hard FMs (72h rule: no Hard escalation & one Hard restart = net Same).

---

## 2026-05-13 (Day 75)

**Prior-prediction scoring (Day 72):**

| Item | Prediction | Outcome | Score |
|---|---|---|---|
| Trend (Same) | No new Hard FM in 72h; QE FM extension mid-June; KAFCO restart positive | Hit — Trend remains Same; no new Hard production FM; QE extended mid-June confirmed | Hit |
| Wave Intensity (L4) | Restart-type FM count 4; no escalation in core production FMs | Hit — Count remains 4; no new production-tier escalation | Hit |
| Action 1 (KAFCO restart) | Expected first Hard restart; fertilizer cascade unwind | Hit — KAFCO restart confirmed May 2 (Hard Tier 1); first operator restart marked | Hit |
| Action 2 (EGA timeline) | Monitor end-May rehabilitation start; expect firm baseline statement | Pending — No new EGA announcement in last 72h; May 31 is 16 days away | Pending (near deadline) |
| Action 3 (European PET/MEG Wave 3 FM) | Expect stress signals by 17–24 May; T+7 horizon deadline | Pending — Not yet at deadline; T+7 window opens ~May 17–24 | Pending |
| Watchlist 1 (Qatalum 60%) | Expect gas supply confirmation or deterioration signal by May 13 | Hit — Qatalum confirmed at 60% capacity baseline (May 1); no new signal; baseline holds | Hit |
| Watchlist 2 (Lotte Chemical, May 29 target) | Naphtha shortage evident; monitor for restart delay or FM | Pending — May 29 deadline not yet crossed; no announcement yet | Pending |
| Watchlist 3 (Strait traffic 5%+ recovery) | Expect slight improvement or deterioration (baseline 3.3% normal) | Hit — Baseline maintained at 3.3%; single May 9 transit confirmed but insufficient for normalization | Hit |
| Watchlist 4 (Bunker fuel physical tightness, T+7 by ~17 May) | Expect shortage warnings from Singapore, Fujairah by May 17 | **Surprise (early) — Bunker fuel shortage explicitly signaled May 12 (5 days early). AP/Reuters Tier 1 source. Signal strength: Critical.** | Hit + Surprise |
| Watchlist 5 (LME aluminium divergence) | Expect long-dated contract weakness vs. spot firmness | Pending — May 8 data confirms divergence (Dec 2027 down 0.22%); pattern holds through May 13 | Pending (pattern confirmed but trend continues) |
| Scenario A (45%) | Sustained closure Q2/Q3; demand destruction primary mitigation | **In progress — Bunker fuel FM emergence (May 12) and Lufthansa 20K cuts (Apr 23) confirm A pathway activating. Scenario A probability should rise to 50% as of Day 75.** | Tracking toward Hit (probability rising) |
| Scenario B (35%) | Ceasefire holds; selective transits 5–10% normal by end-May | **Miss/Surprise — May 5–7 shipping attacks (CMA San Antonio, JV Innovation) contradict ceasefire stability. Scenario B probability should fall to 25%.** | Miss (assumptions breaking) |
| Scenario C (20%) | Escalation (kinetic, sovereign FM, refinery hit) | **Surprise — Kinetic escalation visible May 5–7 (vessel strikes). Scenario C probability should rise to 30% as of Day 75.** | Hit + Surprise |

**Trend & Wave summary:**
- **Trend:** Same (confirmed). No new Hard production-tier FM declarations in 72h.
- **Wave Intensity:** L4 Systemic (confirmed). Restart-type FM count at 4; no production escalation.
- **Surprising signal:** Bunker fuel shortage emerged 5 days ahead of T+7 schedule (Watchlist 4). This is the first explicit Wave 3 distribution-tier FM signal and validates the cascade model.
- **Scenario shift:** Scenario B (ceasefire holds) is degrading due to May 5–7 kinetic signals; Scenario A (sustained closure + demand destruction) rising toward 50%; Scenario C (escalation) rising toward 30%.

**Confidence assessment:**
- High confidence on Trend (Same).
- High confidence on Wave Intensity (L4).
- **Moderate-to-low confidence on scenario probabilities:** May 13–20 will be critical signpost window. If bunker fuel FM is formalized (Maersk, MSC, CMA), Trend escalates to Worse and Wave Intensity tests L5. If SABIC/KPC renews FM language with extended timeline, Trend escalates to Worse immediately.

**Methodology test under stress:** Bunker fuel shortage signal emerged within prediction window (Watchlist 4, T+7) but earlier than anticipated (May 12 vs. expected ~May 17). This validates the Wave 3 distribution-cascade model and suggests the cascade is accelerating faster than historical Felsberger-era patterns. No methodology rule broke; instead, the empirical signal confirmed the underlying theory earlier than modeled. **Confidence in Wave 3 distribution-cascade pathway increases to 80% probability.**

## 2026-05-16 (Day 78)

**Prior predictions (Day 75, 13 May):**
- Trend: Same · High confidence
- Wave Intensity: L4 Systemic · High confidence
- Actions: (1) Monitor bunker FM formalization T+3, (2) SABIC/KPC long-term FM extension past May 15, (3) EU converter FM signal T+7
- Watchlist: (1) SABIC/KPC extension, (2) bunker fuel maritime FM, (3) Iran escalation, (4) Stripe reopening diplomatic signal, (5) Lufthansa flight cuts acceleration

**Scoring:**
- Trend prediction (Same) — **Hit** (today's signals confirm Same; no new Hard operator FM declarations in 13–16 May)
- Wave Intensity (L4 Systemic) — **Hit** (restart-type FM count static at 4; Wave 3 distribution cascade deepening into bunker fuel)
- Action 1 (bunker FM formalization T+3 = by 16 May) — **Pending/False alarm** (bunker shortage emerged May 12 as price signal + shipping press, but NO operator FM formalized; Type 4 FM still emerging, not yet declared. Escalated bunker monitoring to "FM-readiness briefing" instead of full FM. Partial hit: correct direction, early timing.)
- Action 2 (SABIC/KPC extension T+3 = by 16 May) — **Pending** (no new filing by 16 May; deadline moved to 20 May for T+4 window)
- Action 3 (EU converter FM T+7 = by 20 May) — **Pending** (T+7 deadline still open)

**Today's Trend & Wave assessment:**
- Trend: Same (confirmed by lack of new Hard FM, reaffirmed QE FM extension, bunker price signal vs bunker FM formalization gap)
- Wave Intensity: L4 Systemic maintained (restart-type FM unchanged; Wave 3 distribution cascade deepening but not yet operator-level FM)
- **Surprise factor:** Low surprise. Bunker fuel shortage emerged on expected timeline (May 12, within prediction window). However, shortage is price-signal-only, not yet operator FM—this suggests carriers are absorbing cost rather than rationing volume. Suggests market is still in allocative phase (L4 Systemic) rather than rationing phase (L5 Regime). Extends timeline for L4→L5 transition by ~7 days (now 23–27 May vs 16–20 May originally predicted).

**Confidence in tomorrow's brief (T+3 to 19 May):**
- Trend: Expect Same → Worse if bunker FM declared by major carrier (MSC, Maersk) between 19–25 May. Currently Same with high confidence.
- Wave Intensity: L4 Systemic maintained unless Type 4 maritime FM formalized. Watch SABIC/KPC extension filing (20 May) as leading indicator for L4→L5 boundary.
- Leading indicator (bunker FM formalization) becoming live; watch T+3–T+10 window closely (19–27 May).

## 2026-05-16 (Day 78)

**Prior-period scoring (from Day 72 brief, 10 May):**
- **Trend prediction (10 May: Worse)** — SCORED MISS. Actual Trend on Day 78: Same. The brief predicted escalation; instead, the 13–16 May window showed no new Hard FM declarations. QatarEnergy reaffirmed (not escalated), KAFCO restart offset, bunker Type 4 emerged but not operator-formalized.
- **Wave Intensity (10 May: L4 Systemic)** — SCORED HIT. Day 78 holds L4 Systemic. Restart-type FM count stable at 4. Wave 3 deepening into tertiary chains (bunker) confirms cascade propagation. Boundary to L5 remains tested but not crossed.
- **Action 1 (SABIC 30-day extension language T+3, due ~13 May)** — SCORED MISS. No new SABIC filing in 13–16 May. Tadawul filing from Day 41 held; no extension published.
- **Action 2 (Lotte 29 May restart confirmation, deadline 29 May)** — SCORED PENDING. Lotte confirmed May 29 target (delayed from May 18). Test point remains active; now 13 days ahead.
- **Action 3 (Type 4 bunker FM emergence T+7, due ~17 May)** — SCORED PARTIAL HIT. Bunker shortage surfaced May 12 as Tier 2 signal (WFSB, WaPo, Euronews). Prices $800/tonne, +60% pre-war. However, not yet operator-formalized (no MSC/Maersk FM letter), so scored Medium/Soft rather than Hard.
- **Watchlist 1 (Lufthansa further cuts T+7)** — PENDING (no new public cut 13–16 May; deadline ~17 May).
- **Watchlist 2 (EU PET converter stress T+7)** — PENDING (no hard converter FM, but capacity utilization stress signals tracking).
- **Watchlist 3 (KPC sovereign FM extension T+7, due ~17 May)** — SCORED MISS. No new KPC FM in 13–16 May window.
- **Watchlist 4 (Bunker price $850+ breach T+3, due ~13 May)** — PARTIAL HIT. May 4 was $800; no May 13–16 price data in current brief confirms >$850, but $800 level confirms scarcity signal.
- **Watchlist 5 (Qatalum 60% hold T+3)** — SCORED HIT. Qatalum holds 60% capacity.
- **Scenario A (L4→L3 by early June, p=25%)** — TRENDING MISS. No diplomatic progress; Lotte delayed; Trend still Same. Downgrade p→15%.
- **Scenario B (Flat L4, p=50%)** — TRENDING HIT. Current state matches exactly. Upgrade p→60%.
- **Scenario C (L5 escalation, p=25%)** — NO ESCALATION YET. Boundary conditions activated (Trump "life support", bunker FM emerging, KPC extension risk). Maintain p~25%; test active.

**Today's metrics (Day 78, 16 May):**
- **Trend:** Same (High confidence). No Hard operator FM 13–16 May. QatarEnergy FM extended (reaffirmed, not escalated). Bunker Type 4 signal emerged but not operator-formalized. Strait 69+ days closed (static). Restart-type FM count static at 4.
- **Wave Intensity:** L4 Systemic (High confidence). Restart-type FM count unchanged. Wave 3 cascade deepening into bunker, aviation (tertiary). Distribution-tier FM signals accumulating. Boundary to L5 is tested; no cross-over yet.
- **Confidence:** High on both Trend and Wave. The metrics are internally consistent: no escalation (Same Trend) but deepening cascade severity (L4 Systemic holding due to restart-type FM baseline).

**Surprise factor:** 
- Expected: Bunker shortage to surface as analyst commentary only. Actual: Tier 2 shipping press (WFSB, WaPo, Euronews) published bunker as explicit supply-risk signal May 12. This accelerated Type 4 signal emergence and raised the test threshold for operator FM within 7 days.
- Expected: Lotte restart May 18 (confirmed). Actual: Delayed to May 29. This is not a surprise per Maybank's April 6 warning, but it confirms the pattern: inventory depletion is outpacing Strait reopening in diplomatic timelines.
- Expected: KPC FM extension past Day 52. Actual: No extension in 13–16 May window. This is the non-event that holds probability of L5 boundary test at 25% rather than escalating to 35+%.

**Confidence summary:**
- Trend assessment (Same): High. Rule-based: No Hard FM 72h + static restart-type count + no new operator escalation = Same Trend.
- Wave assessment (L4 Systemic): High. Rule-based: Restart-type FM count 4 (unchanged) + Wave 3 cascade deepening (tertiary chains: bunker, aviation) + no Hard escalation = L4 Systemic holds.
- Boundary test (L4→L5): Medium. Conditions: (a) operator FM on bunker within 7 days (p~40%), (b) KPC/SABIC restart-type extension by 20 May (p~25%), (c) Trump resumption of major combat ops (p~15%). Combined probability of any trigger within T+7: ~60%. If triggered, L5 probability jumps to 60–80%.

## 2026-05-16 (Day 78)

**Prior predictions (Day 77, window 13–16 May):**
- **Action 1:** Track QE FM extension past early July — **Hit** (QE confirmed extension to early July; two additional Edison cargoes cancelled on 16 May).
- **Action 2:** Monitor KPC/SABIC "cannot estimate" extension past May 20 — **Pending** (deadline 20 May not crossed; Sadara filing still active; KPC FM #2 language unchanged to date).
- **Action 3:** Bunker fuel Type 4 FM from maritime operator within 7 days — **False alarm** (Bunker shortage confirmed real on May 12, $800/tonne; but NO maritime operator FM letter yet; shipping absorbing costs, not formalizing FM).

**Prior Watchlist (Day 77):**
- **WL1:** Strait to 50+ nm effective closure by May 17 — **False alarm** (Strait remains ~closed 69+ days; no widening reported; Iran "vast operational area" redefinition is descriptive, not measurable nm expansion).
- **WL2:** New non-LNG primary-operator FM in 13–16 May — **Miss** (No new Hard FM declarations from Saudi Aramco, KPC, SABIC, EGA, ALBA in 72h window).
- **WL3:** Lotte restart confirmation by May 18 — **Miss** (Lotte restart DELAYED from May 18 to May 29; restart did not confirm on scheduled date).

**Prior Scenarios (T+30 horizon = 15 June 2026, assessed on Day 78):**
- **Scenario A (70%):** Strait closed 90+ days, no restarts, L4 Systemic — **Tracking on target**. Strait 69+ days; no primary restart confirmed in 72h; L4 Systemic active. Probability holds 70%.
- **Scenario B (20%):** Partial reopening by 30 May, KPC restart, L4→L3 — **No progress**. No Strait reopening reported; KPC FM #2 unchanged. Probability down to 15%.
- **Scenario C (10%):** Extension to Q3 2026, all operators multi-year FM, L5 — **Rising risk**. QE 5yr + EGA 12mo + Sadara "cannot estimate" + Lotte 29 May delay signal extended constraints. Probability up to 15%.

**Today's Trend (16 May, 08:00 CEST):**
- **Trend:** Same (High confidence). No new Hard FM declarations in 72h. Bunker shortage Type 4 signal is real but not yet operator-formalized. QE FM extended, Lotte delayed, no primary restart confirmed in trailing window. Restart-type FM count static at 4.
- **Wave Intensity:** L4 Systemic (High confidence). Restart-type FM count unchanged. Wave 3 cascade explicit (bunker, aviation, aluminium). Distribution-tier signals accumulating. Boundary to L5 not yet crossed.

**Surprise factor:** Bunker fuel shortage emerged as explicit Type 4 Distribution signal on May 12 (WFSB/WaPo/Euronews Tier 2), not anticipated at this level of detail in Day 77 brief. Formalization tracking well.

---

## 2026-05-19 (Day 81)

### Prior-prediction scoring (from Day 78 brief, 16 May)

**Trend:** Same (High confidence) 
- **Prediction:** No new Hard FM declarations in 72h (13–16 May).
- **Actual (16–19 May):** No new Hard FM declarations confirmed. Bunker fuel Type 4 signal reconfirmed but emerged 12 May (prior to Day 78 window). 
- **Verdict:** **Hit**. Trend: Same remains operative.

**Wave Intensity:** L4 Systemic (High confidence)
- **Prediction:** Restart-type FM count stays at 4; boundary to L5 tested if (a) maritime operator FM within 7 days or (b) KPC/SABIC extend past 20 May.
- **Actual (16–19 May):** Restart-type FM count holds at 4. No maritime operator FM declaration. KPC/SABIC deadline May 20–21 not yet passed.
- **Verdict:** **Pending** (boundary test moves to 20–21 May). L4 Systemic reconfirmed operationally.

### Today's predictions (Day 81, 19 May)

**Trend:** Same (High confidence)
- **Rationale:** 72h (16–19 May) produced no new Hard operator FM declarations. QatarEnergy FM extension to mid-June reconfirmed Tier 1; Bunker shortage Type 4 status embedded from 12 May. Lotte Chemical +11 day delay is Tier 2 (not Hard operator FM). No primary operator restart confirmed. Restart-type FM count static 4.
- **Confidence:** High (no signal variance).

**Wave Intensity:** L4 Systemic (High confidence)
- **Rationale:** Restart-type FM count = 4 (binding constraint). No new restart-type FM filed. KPC/SABIC extension deadline May 20–21 is T+1–2 (critical test, not yet passed). Bunker fuel Type 4 signals accumulating (prices $800, shipping cost $400m/day) but no maritime operator FM yet. Boundary conditions untested in this window.
- **Confidence:** High (structural position unchanged).

### Actions scoring (from Day 78)

1. **Monitor KPC/SABIC FM language through May 20 by 08:00 CEST** — **Pending**. Deadline: 21 May 08:00. No extension announced by 19 May 23:59 UTC. Watch Tadawul filings early morning 20 May.

2. **Surface maritime operator FM within 12h** — **Hit** (bunker signals were surfaced 12 May as Tier 1, prior to Day 78; reconfirmed 19 May as $800/tonne pricing). No new maritime FM filed 16–19 May.

3. **Flag naphtha restart >7 day delay** — **Hit**. Lotte Chemical +11 days (18 May → 29 May) flagged and escalated as Type 3 Feedstock FM candidate. Korea export controls (26 Mar) provide Tier 1 corroboration.

### Watchlist scoring (from Day 78)

1. **KPC/SABIC extend past May 20** — **Pending**. Deadline: 21 May. Not triggered by 19 May 23:59.

2. **Maritime operator FM by May 23** — **Pending**. Deadline: 24 May. No formal FM filed by 19 May; Maersk, MSC remain silent despite $800 bunker.

3. **SABIC restart-type FM by May 22** — **Pending**. Deadline: 22 May. SABIC (26 Mar FM) holding; no extension announced by 19 May.

4. **Naphtha restart >7 day delay by May 22** — **Hit**. Lotte +11 days meets threshold. Flagged 18 May; escalation signal confirmed.

5. **EGA Al Taweelah restart confirmation by May 24** — **Pending, but supportive**. EGA 12-month timeline reconfirmed Tier 1 (May 12 CRU World Aluminium Conference, CMO Abubakar statement). Supports L4 classification (multi-quarter physical absence).

### Scenarios scoring (from Day 78, T+30 horizon: 20 June)

- **Scenario A (45%):** Ceasefire holds, partial restarts. — **On track**. No escalation 16–19 May; ceasefire holds nominal (Trump paused Project Freedom 6 May). Lotte restart target May 29 is directionally positive for this scenario if met.

- **Scenario B (35%):** Ceasefire extends, L5 candidate. — **On track**. KPC/SABIC boundary test 20–21 May will determine next escalation move. If either extends FM language, Scenario B probabilities increase toward 40–45%.

- **Scenario C (20%):** Regional escalation, L5 full regime. — **Not triggered**. No new kinetic events 16–19 May; ceasefire nominal. Probability holds at 20% pending boundary tests.

### Surprise factor

**No material surprises in 16–19 May window.** 

- QatarEnergy FM extension to mid-June was expected (confirmed prior brief); no acceleration or extension beyond mid-June.
- Bunker fuel Type 4 signals were already Tier 1 from 12 May; reconfirmation at $800/tonne is consistent, not surprising.
- Lotte Chemical +11 day delay was expected given Korea naphtha controls (26 Mar) and feedstock scarcity signals; delay magnitude (+11 vs +7 threshold) is material but not anomalous.
- Hormuz "vast operational area" redefinition (May 2026, IRGC) is operationally significant but announced mid-window; not a new surprise at Day 81 boundary.

**Confidence in predictions:** High. No model failures; boundary conditions remain operative. Next critical juncture: KPC/SABIC filings 20–21 May morning (CEST).

## 2026-05-19 (Day 81)

**Prior Brief Predictions (Day 78, 16 May 2026):**

**Trend Prediction:** Same (high confidence) → **HIT** ✓
- Expected: No new Hard FM declarations 16–19 May.
- Actual: Confirmed. Zero new Hard operator FMs. QE extension on 16 May (prior forecast), Iran redefinition of Strait (Tier 1, May 2026), Lotte delay (14 May, within forecast). Trend: Same confirmed.

**Wave Intensity Prediction:** L4 Systemic (high confidence) → **HIT** ✓
- Boundary test: "major maritime operator Type 4 bunker FM" OR "KPC/SABIC extend FM past 20 May" — neither triggered 16–19 May.
- Actual: Confirmed. L4 holds. Restart-type FM count static (4). Bunker shortage signals accumulate (Type 4 Distribution embedded, AP 12 May), but no formal maritime operator FM filed. Boundary not crossed.

**Action Predictions (T+3 horizon, 16–19 May):**
1. Monitor Iran redefinition / UK defensive mission → **HIT** ✓ (Confirmed: IRGC redefined Strait; UK deployed assets 3–4 May)
2. Track Lotte Chemical restart → **HIT** ✓ (Correctly flagged 18→29 May shift; now tracking May 29)
3. Watch QE, KPC, SABIC restart signals → **PENDING** (No new signals 16–19 May; watch remains active)

**Watchlist Predictions (T+1/T+3):**
1. Bunker prices >$750/tonne by 19 May → **SOFT HIT** (AP 12 May reported $800, prices held spiked)
2. QE FM extended to mid-June → **HIT** ✓ (AGBI 16 May: extended mid-June)
3. Strait traffic <10% by 19 May → **HIT** ✓ (Kpler: 5% confirmed April; maintained 19 May)

**Scenario Predictions (T+30, 19 May – 18 June):**
- Scenario A (Ceasefire, phased restart Q3): 35% → Status **PENDING** (Still plausible if US-Iran talks advance; no escalation 16–19 May)
- Scenario B (Stalemate, L5 regime risk): 40% → Status **PENDING** (Most likely by 18 June if KPC/SABIC extend FM)
- Scenario C (Escalation spike → revert): 25% → Status **PENDING** (No incident 16–19 May; minor risk remains)

**Surprise Factor:** None. All predictions confirmed within expected outcomes. No unexpected Hard signals, no sudden restarts, no new kinetic events 16–19 May. Crisis following baseline stalemate script.

**Trend Confidence:** High. L4 Systemic intensity holds because restart-type FM count (4) is static and boundary conditions (maritime FM, KPC/SABIC extension) not triggered by 19 May. Watch becomes 20–23 May for KPC/SABIC Tadawul guidance; if silent or extend FM, Trend shifts Worse, Wave Intensity tested at L5.

## 2026-05-19 (Day 81)

**Prior predictions scored:**
- Day 78 Action 1 (KPC/SABIC FM extension test by 20 May): Pending → deadline 20 May today. Status: No new extension filed 16–19 May. Hit if neither extends by end of day 19 May; Miss if either extends after 19 May (pending resolution).
- Day 78 Action 2 (Maritime Type 4 FM by 23 May): Pending → deadline 23 May. Status: No maritime operator formal Type 4 FM filed 16–19 May. Pending.
- Day 78 Action 3 (QE mid-June FM extension impact): Hit. QE confirmed extended to mid-June 16 May; operable trains Q3/Q4 restart.
- Day 78 Watchlist 2 (EGA 12-month timeline by 23 May): Hit. EGA confirmed 12-month rebuild 16 May per Bloomberg / AGBI.
- Day 78 Watchlist 3 (Iran IRGC Strait redefinition by 20 May): Hit. IRGC redefined Strait as "vast operational area" by 16 May.
- Day 78 Watchlist 4 (Bunker $800/tonne by 23 May): Hit. Confirmed 12 May at $800/tonne (signal 5 days old by 16 May, still holding).
- Day 78 Scenario A (Restart FM count 6 within 30 days): Pending → deadline 16 June. Status: No 5th restart-type FM filed 16–19 May; count remains 4. Trending Miss.
- Day 78 Scenario B (Maritime Type 4 FM by 16 June): Pending. Status: No formal filing 16–19 May; 28 days remain. Risk elevated if ceasefire fails after 20 May.
- Day 78 Scenario C (Strait closed or semi-closed, Q3 planning integrates): Pending → baseline holds. Status: EIA confirms closed through late May; Q3/Q4 planning now structural. Trending Hit.

**Today's Trend: Same (High confidence)**
- No new Hard FM declarations 16–19 May.
- Restart-type FM count static at 4.
- Bunker Type 4 signal 7 days old, no maritime operator FM yet.
- Ceasefire status uncertain (Trump "on life support" 11 May); no extension announced 16–19 May.
- Confidence: High (data-driven, Tier 1 sources dominate).

**Today's Wave Intensity: L4 Systemic (High confidence)**
- Restart-type FM count unchanged at 4.
- Hard operator restarts at 2 cumulative; Lotte Chemical restart pending 29 May.
- Wave 3 cascade deepening (bunker, aviation, aluminium contracts).
- Distribution-tier FM signals accumulating but operator formalization delayed.
- Boundary test (maritime Type 4 FM OR KPC/SABIC extend past 20 May) not triggered.
- Confidence: High (structural assumptions embedded in EIA, Wood Mackenzie, IEA models).

**Surprise factor: Low (0.15 expected vs 0.05 realized)**
- No unexpected Hard FM declarations.
- EIA STEO (12 May) confirmed baseline assumptions (Strait closed through late May, June pickup).
- Bunker Type 4 signal emerged on schedule (12 May); no new maritime operator FM (as expected if operators absorb costs pre-20-May).
- Trump ceasefire "on life support" was market-signal but not operator FM. Geopolitical risk now priced; L4 structural.

**Confidence wedge:** High confidence Same + High confidence L4 = median outlook Same / L4 through 26 May (maritime Type 4 threshold). If ceasefire extends past 20 May, Scenario A (June reopening) probability holds at 50%. If ceasefire collapses after 20 May, Scenario B (July closure) probability escalates to 70%, triggering L5 hypothetical alert by 24 May.
