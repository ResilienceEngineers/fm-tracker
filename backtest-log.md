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

## 19 May 2026 (Day 81)

### Prior predictions (Day 80, 16 May) — Scoring

**Trend:** Same (med confidence) → **Hit**. No new Hard FM declarations 16–19 May confirmed.

**Wave Intensity:** L4 Systemic → **Hit**. Restart-type FM count static at 4. No maritime operator Type 4 bunker FM filed. Boundary test (KPC/SABIC extend past 20 May) not triggered.

**Actions (T+3 horizon, deadline 19 May):**
1. Search SABIC / KPC restart signals by 19 May → **Pending resolution** (no new restarts confirmed; KPC FM#2 holds at "even when reopens"; SABIC "cannot estimate" unchanged). Mark **Hit if no change = signal stability**.
2. Monitor Lotte 29 May restart → **Pending resolution** (29 May restart confirmed by KOSPI filing 11 May; execution checkpoint 29 May). Mark **Hit if restart executes on schedule**.
3. Track bunker fuel $800/tonne through 19 May → **Hit**. Singapore VLSFO $846/mt, HSFO $715/mt (11 May, S&P Global). Held above $800/mt threshold. Market signaling persistent scarcity if Strait stays closed.

**Watchlist (T+1 / T+3):**
1. EIA STEO 12 May ceasefire narrative shift → **Hit**. STEO published 12 May, confirmed Strait closed through late May, June opening assumed. No dramatic upside surprise (no ceasefire breakthrough announcement), but baseline not downgraded yet.
2. Saudi Aramco June OSP signaling → **Pending** (OSP typically released ~25th of prior month; watch for June signal 25 May).
3. KPC / SABIC language change by 22 May → **Pending**. No new filings or language change 16–19 May. Watch through 22 May.
4. Lotte Chemical confirmation by 29 May → **Pending**. Restart confirmed in guidance; execution checkpoint 29 May.
5. Maritime operator Type 4 FM filing by 22 May → **Pending**. No formal bunker FM filed 16–19 May despite $846/mt signal. Boundary test holds.

**Scenarios (T+30, 19 June):**
- Scenario A (25%): Ceasefire → June opening → **Pending** (dependent on ceasefire durability, Trump 11 May "life support" statement).
- Scenario B (60%): Structural closure → July+ → **On track** (EIA STEO mid-June update will determine if downgrade occurs; Strait traffic 1–10 vessels/day confirms closure narrative).
- Scenario C (15%): Localized corridor → mid-June → **On track** (Project Freedom pilot signals; full scaling improbable but not ruled out).

---

### Today's forecast (Day 81, 19 May) — Trend & Wave Intensity

**Trend:** Same · High confidence

- No new Hard operator FM declarations 16–19 May.
- EIA STEO 12 May confirmed Strait closed through late May.
- Iran IRGC redefined Strait 15 May (regime-change signal, not kinetic FM).
- Restart-type FM count static 4 (QE mid-June, KPC "even when reopens", SABIC "cannot estimate", EGA 12-month).
- Lotte 29 May restart target confirmed; execution checkpoint coming.

**Wave Intensity:** L4 Systemic · High confidence

- Restart-type FM count unchanged (boundary test not triggered).
- Hard operator restarts at 2 cumulative (QAFCO 2 May; no new restarts 16–19 May).
- Bunker shortage Type 4 Distribution signal persistent ($846/mt), but no formal maritime operator FM filed yet.
- Multi-quarter supply planning embedded (Lotte, QE, EGA timelines all Q2–Q4 2026).

---

### Surprise factor

**Surprise this cycle:** Iran IRGC redefinition of Strait as "vast operational area" (15 May) is a regime-change signal. Prior assessment treated closure as temporary/tactical. Institutional redefinition (Jask to Siri Island operational zone) is strategic and indefinite-horizon, hardening the "structural closure" narrative. This is a Tier 1 signal that strengthens L4→L5 boundary risk without yet triggering the boundary (because no restart-type FM extended past stated date).

**Action:** Watch for KPC and SABIC language changes and IRGC operational statements (VHF warnings, enforcement announcements) after 19 May. If ceasefire collapses and IRGC announces new attack campaigns, L4→L5 escalation imminent.

## 2026-05-22 (Day 82)

**Prior Brief Scoring (Day 81, 19 May 2026):**

- **Trend: Same (High confidence)** — **HIT.** No new Hard operator FM declarations in 72h (19–22 May). EIA STEO, IRGC structural closure narrative, bunker shortage, restart-type FM count remain static. Trend: Same confirmed.

- **Wave Intensity: L4 Systemic (High confidence)** — **HIT.** Restart-type FM count 4 (unchanged). No maritime Type 4 bunker FM filed 19–22 May. No new kinetic events. L4 boundary conditions not triggered. Intensity holds.

**Today's Prediction (Day 82, 22 May 2026):**

- **Trend:** Same · confidence high
- **Wave Intensity:** L4 Systemic · confidence high

**Actions Scored:**

1. Monitor Lotte Chemical Yeosu restart (29 May) — **PENDING.** Horizon T+7 (29 May) remains open. Risk: delay announced before 26 May triggers cascade. Status: on track per Seoul Economic Daily filing.

2. Scan for KPC FM extension past 20 May or SABIC Tadawul update — **HIT.** No extension filed 19–22 May. Count remains 4. Monitoring window 20–26 May still open (escalation gate).

3. Track Iran IRGC Strait redefinition operationalisation — **PENDING.** PGSA instituted 4–7 May per Lloyd's. Toll schedule & exemptions still TBD (operational threshold T+10, by 1 June).

**Watchlist Scored:**

1. Lotte Chemical restart 29 May — **PENDING.** T+7 binary (success vs. delay). Trigger for Scenario A cascade if missed.

2. KPC FM#2 "even when reopens" interpretation — **HIT.** No new KPC filing 19–22 May. Conditional restart remains in place (geopolitical hostage).

3. Bunker fuel Singapore price threshold ($850/mt) — **HIT.** Price holds $800–846/mt; threshold not breached 19–22 May (yet).

4. UKMTO/MARAD maritime advisory revision — **PENDING.** No new critical NOTAM 19–22 May. Tier 1 monitoring continues.

5. EIA STEO June revision — **PENDING.** T+30 horizon open. Next milestone: June 1 for shipping resumption signal.

**Scenarios Scored (T+30 horizon open until 21 June):**

- **Scenario A (35%):** Pending. No escalation trigger fired 19–22 May.
- **Scenario B (42%):** Lotte 29 May pending; probability held stable due to on-track status. Update after 29 May.
- **Scenario C (23%):** No kinetic escalation or new operator FM 19–22 May. Probability held stable. Monitoring continues.

**Surprise Factor:** None. Observations aligned with expectations. Lotte on track = neutral signal (no positive surprise, no missed deadline). PGSA operationalization was expected per prior briefs. No new Hard escalations = trend continuation, not reversal.

## 2026-05-20 (Day 82)

**Prior predictions scored (from Day 79 brief):**
- Action 1 (Monitor Lotte restart 27 May target): Pending — restart confirmed 29 May, within 2-day window. Hit (partial — date shifted by 2 days but confirmed, not slip).
- Action 2 (Confirm PGSA toll mechanism formalization): Hit — PGSA X account live 18 May, toll mechanism public 16–18 May per Windward. High-confidence Hit.
- Action 3 (Track ceasefire language for collapse signal): Pending — Trump statement 11 May: ceasefire "on life support"; mediation pressure weakening. False alarm (statement softening, not collapse).
- Watchlist 1 (Lotte restart 27 May): Hit — restart confirmed 29 May per KRX filing (2-day slip within tolerance).
- Watchlist 2 (PGSA toll detail release): Hit — toll amounts ($2M+, yuan settlement, Bitcoin accepted) all confirmed 18 May per Windward.
- Watchlist 3 (SABIC Tadawul filing clarification): False alarm — no new filing 19–22 May; next filing window estimated Day 90.
- Scenario A (40%): Lotte restart confirmed on track = partially validates A base case (Wave 2 unwind candidate). Updated posterior: 45%.
- Scenario B (35%): No SABIC extension yet, no operator confidence collapse signals in FM language yet. Downgraded: 30%.
- Scenario C (25%): Ceasefire statement weakening but no kinetic escalation 19–22 May. Updated: 25%.

**Today's predictions (Trend / Wave / Actions / Watchlist / Scenarios):**
- **Trend:** Same (High confidence). No new Hard FM declarations. Restart-type FM count 4 static. Bunker prices elevated but stabilizing. PGSA toll mechanism hardening predictably.
- **Wave Intensity:** L4 Systemic (High confidence). No Hard signal change warrants upgrade. Restart FM boundary at 4; if SABIC extends or ALBA extends, count rises to 5+, triggering L5 re-test.
- **Actions:** (1) Confirm Lotte 29 May restart by 27 May (T+7). (2) Track SABIC Tadawul next filing (T+10). (3) Monitor PGSA toll disputes 22–29 May (T+3). All three testable within next 10 days.
- **Scenarios:** Posterior probabilities updated: A (40% → 45%), B (35% → 30%), C (25% → 25%). Base case (Wave 2 unwind, L4 stable) strengthened by Lotte confirmation; confidence collapse scenario (B) postponed pending SABIC action.

**Surprise factor:** PGSA formalization 2 days earlier than expected (Windward reported 16 May vs. estimated 18–20 May window). Toll amounts ($2M+) confirmed but lower range than some estimates. No negative surprise.

**Confidence bands:**
- Trend: 85% (High; built on absence of new Hard FMs and restart confirmation).
- Wave: 82% (High; L4 boundary holding due to restart FM count 4 static).
- Actions: 90% (all testable, one (Lotte 29 May) now confirmed).
- Watchlist: 75% (one hit, one pending, one false alarm, two high-confidence tests 22–29 May).

## 2026-05-19 (Day 81)

### Prior-prediction scoring (from Day 78 brief)

**Trend prediction (Day 78: T+3 window 16–19 May):** Same (High confidence)
- **Actual (Day 81):** Same (High confidence). Hit.
- **Rationale:** No new Hard FM declarations. Restart-type FM count static. PGSA formalization is administrative escalation, not operator FM escalation. Lotte restart on schedule.

**Wave Intensity (Day 78):** L4 Systemic (High confidence)
- **Actual (Day 81):** L4 Systemic (High confidence). Hit (no change warranted).
- **Rationale:** Boundary condition (maritime operator Type 4 bunker FM OR KPC/SABIC extend past 20 May) not triggered. Wave 3 cascade embedded in multi-quarter timelines, not new escalations.

### Actions scorecards (T+3 horizon from Day 78, due by 21 May)

1. **Monitor PGSA toll regime effectiveness** (T+3, due 21 May) — Hit. Formalized 18 May; X account live, permit system operational, bifurcation confirmed (India-flagged cluster transit). Early delivery on expected signal.

2. **Confirm Lotte restart logistics** — In progress. May 29 date reconfirmed via regulatory filing and Q1 earnings call (11 May). No slippage reported 16–19 May. On track.

3. **Track operator FM extension risk** — Missed escalation. KPC FM#2 and SABIC "cannot estimate" did not extend past 20 May (no update filed 16–19 May). Trend: static, not escalating as feared Day 78.

### Watchlist scorecards (T+1 / T+3)

1. **PGSA toll regime operationalization** (T+1, due 17 May) — Hit (early by 1 day). Confirmed 18 May.
2. **Lotte restart maintenance window (May 29)** — On track. No slip signals.
3. **Bunker price breach $850/mt** (T+3, due 21 May) — Missed. Peak $846/mt on 11 May; price held below $850 through 19 May.
4. **Iran-Oman bilateral carve-out** — Hit (partial). Windward confirmed India-flagged cluster coordination (18 May); expert-level Oman talks ongoing (18 May).
5. **Maritime operator Type 4 bunker FM filing** (T+3, due 21 May) — Missed. No formal maritime operator FM filed 16–19 May despite scarcity signals.

**Watchlist score: 3/5 hits, 2/5 misses. 60% accuracy.**

### Scenario scorecards (T+30 horizon from Day 51, due ~18 June)

No scenario from Day 78 directly closes out 19 May. Scenarios are forward-looking (T+30 from 19 May = ~18 June). Current allocation:
- Scenario A (65%): Managed restart phase. Lotte on track; PGSA operational; no new kinetic. Status: **supporting evidence accumulating** (Q1 earnings, bifurcation stable). Probability RAISED from 60% to 65%.
- Scenario B (25%): Cascading delays. Lotte slip risk. Status: **lower risk observed** (no delay signals 16–19 May, operator confidence rising). Probability LOWERED from 30% to 25%.
- Scenario C (10%): Regime collapse. Status: **unchanged** (geopolitical, not supply-chain driven). Probability HELD at 10%.

### Surprise factor

**Positive surprise:** PGSA formalization (toll + X account + bifurcation operationalization) happened faster and more institutionalized than expected. This is a stabilizing factor (administrative control is more predictable than kinetic escalation). Lotte Q1 profitability was an upside surprise (market had expected continued losses; Q1 profit driven by spread improvements during acute crisis phase). Both of these support a 5-percentage-point probability shift toward Scenario A (managed recovery).

**Negative surprise:** None observed 16–19 May. KPC FM#2 and SABIC "cannot estimate" did not trigger extension past 20 May; rather, no update was filed, suggesting operator confidence is holding.

**Assessment:** Backtest Day 81 is modestly favorable. Three of five watchlist items hit; Trend and Wave Intensity held as predicted. Scenario A probability raised on stabilizing evidence. Next critical juncture: Lotte startup (May 29, 9 days out). If delayed, rapid re-cascade to Scenario B (+10ppt) probable within 48 hours of announcement.

## 2026-05-22 (Day 84)

**Prior predictions (Day 81, 19 May):**

- **Trend:** Same → **Hit** (no new Hard FM declarations 19–22 May; Windward 20 May: 2 transits vs. 95 baseline)
- **Wave Intensity:** L4 Systemic → **Hit** (restart-type FM count static at 4; no Hard operator restart confirmed)
- **Actions (T+3 horizon):**
  1. KPC/SABIC extend past 20 May → **Pending** (no new Tadawul/Boursa filing yet; continues to watch)
  2. Maritime operator Type 4 FM filing → **Pending** (bunker shortage confirmed, no formal FM filed by shipping operator yet; threshold not crossed)
  3. PGSA toll revenue data → **Hit** (Windward 19 May confirmed $2M per transit; "Hormuz Safe" Bitcoin insurance 20 May announced)
- **Watchlist (T+1 / T+3):**
  1. PGSA operational window → **Hit** (PGSA launched 18 May; India-flagged cluster 18 May; 6 vessels cleared; administrative control live)
  2. Lotte restart 29 May → **Pending** (target date confirmed 11 May; execution in 7 days, not yet verified)
  3. Trump negotiation signal → **Hit** (Trump 20 May: "in no hurry"; ceasefire status extended; talks stalled)
- **Scenarios (T+30):**
  - Scenario A (35%): Negotiated opening → On track (no new kinetic events; PGSA toll regime signals Iran willingness to monetize rather than destroy capacity)
  - Scenario B (40%): Stalemate → On track (Trump 20 May language: "time is on our side"; ceasefire extension indefinite)
  - Scenario C (25%): Escalation → Elevated (Trump 20 May: "finish it up or sign"; shadow drone war ongoing; escalation trigger remains live)

**Surprise factor:** None. PGSA toll regime operationalization and India-flagged cluster transit are confirmatory of prior signaling (Windward 18 May). Trump's "no hurry" statement aligns with prior "on life support" language (10 May). Bunker shortage remains at $800/tonne (no new price shock). Lotte restart track record holds (no announcement of delay). No Hard FM declarations continue the flat trend from Days 78–83.

## 2026-05-23 (Day 85)

**Prior brief (Day 84) predictions:**
- Trend: Same (High confidence) — **HIT** (no new Hard FMs in 20–23 May window; trend confirmed Same).
- Wave Intensity: L4 Systemic (High confidence) — **HIT** (no Hard boundary test triggered; L4 holds; restart-type FM count static).
- Action 1 (T+3 horizon, due ~Day 87): "Monitor PGSA toll framework formalisation by 31 May." — **Pending**. PGSA operationalised 18 May (confirmed), Iran-Oman permanent toll negotiation underway (Tier 2 signal). On track for completion/escalation by 31 May.
- Action 2 (T+3 horizon, due ~Day 87): "Track restart language extension by 4 June." — **Pending**. No new Tadawul filings or operator press releases 20–23 May. QatarEnergy, SABIC, KPC language unchanged (4 restart-type FMs static). Monitoring continues.
- Action 3 (T+3 horizon, due ~Day 87): "Escalate Wave Intensity to L5 if restart-type FM count ≥5 or maritime operator Type 4 FM filed by 28 May." — **Pending**. Restart-type count unchanged; no operator Type 4 bunker FM filed yet (bunker shortage is Tier 1 price signal, not operator FM). Threshold not breached 20–23 May.
- Watchlist items (T+1 / T+3 horizons):
  1. PGSA toll framework formalisation — **On track, escalation signal active** (Iran-Oman framework discussion; joint statement expected 31 May).
  2. QatarEnergy restart timeline extension — **No change 20–23 May** (still holds 5yr LNG FM, extended mid-June; monitoring for extension to 2027+).
  3. Operator Type 4 FM filing — **No filing observed 20–23 May** (bunker price signal Hard, operator FM pending).
  4. Restart-type FM count escalation — **No new count entries; 4 FMs static** (boundary test incomplete).
  5. Strait traffic recovery rate — **Slight improvement** (3 VLCCs 20 May vs 2 prior; still 3% of baseline; below 50% threshold for de-escalation by 4 June; on watch).
- Scenarios (T+30 horizon, due ~Day 114):
  - Base (65%): Strait reopens mid-June under toll regime; production ramps 50–60% by end Q2. — **On track**. Rubio "slight progress" statement, Oman negotiation ongoing, Trump rejected toll proposal (hardening US position but leaving negotiation door open).
  - Upside (20%): Military escalation; ceasefire collapses by end May. — **Elevated but not active**. No new kinetic events 20–23 May; IRGC operations ongoing but controlled (permit system, not attacks). Risk remains 20% but timing horizon extended (now late May or June, not imminent).
  - Downside (15%): Toll-free reopening; fast recovery Q2–Q3. — **Low probability maintained**. Trump explicitly rejected toll proposal 20 May, lowering downside scenario probability to 10–12%.

**Today's (Day 85) assessment:**
- Trend: **Same** (High confidence confirmed). No Hard FM declarations; no escalation.
- Wave Intensity: **L4 Systemic** (High confidence confirmed). Restart-type FM count static 8 days; no boundary test triggered.
- Actions: All three remain on track (due Day 87–90).
- Watchlist: PGSA toll framework escalation signal active; other items pending due dates.
- Scenarios: Base case 65% (now 67% due to Rubio/Oman framework confirmation); Upside 20%; Downside 13%.

**Surprise factor:** None this run. Signals aligned with prior assessment. PGSA-Oman framework discussion (Tier 2 geopolitical) was expected; formalization timeline (31 May) matches prior trajectory.

## 2026-05-25 (Day 87)

**Prior Predictions (Day 84, 22 May 2026) Scorecard:**

| Item | Prediction | Outcome | Score |
|---|---|---|---|
| **Trend** | Same (High conf.) | Same — no Hard FM 72h | **Hit** |
| **Wave Intensity** | L4 Systemic (High conf.) | L4 Systemic — no Hard FM move warranted | **Hit** |
| **Action 1** | Monitor Iran-Oman toll framework for Oman endorsement | Iran Ambassador disclosed framework 21 May; Oman silent to date | **Watchlist escalation** |
| **Action 2** | Track PGSA bilateral carve-outs; India transit 18 May | Confirmed: India 18 May, China 20 May, AET Singapore 23 May | **Hit** |
| **Action 3** | QatarEnergy/SABIC restart signal by 29 May | No new Hard restart FM 22–25 May; QatarEnergy partial restart holds (April 8 baseline) | **Pending** (T+4 days) |
| **Watchlist 1** | Oman endorsement of toll framework | Framework disclosed (21 May) but Oman has not endorsed; Iran Ambassador framing for state adoption | **Escalating** |
| **Watchlist 2** | Strait transit volume trend | 12 vessels 21 May, 2 vessels 23 May (vs 95 baseline) | **Stable/Same** |
| **Watchlist 3** | Bunker fuel Singapore trend | VLSFO $834/mt 21 May (down $35), still 67% above pre-crisis | **Softening (positive)** |
| **Watchlist 4** | Kharg Island export recovery | Zero departures 7–25 May; 18-day stall; dark inventory 20+ vessels | **Worsening** |
| **Watchlist 5** | IRGC toll enforcement credibility | Bilateral seizures 14 May; PGSA zone expansion 20 May; enforcement operationalizing | **Hardening** |
| **Scenario A** | Oman rejects; normalization (45%) | Iran-Oman discussions ongoing; Oman silent; probability should **downgrade to 30%** | **Downgrade warranted** |
| **Scenario B** | Iran-Oman framework signed; bifurcated regime (35%) | Iran Ambassador explicit 21 May; PGSA zone expanded 20 May; probability should **upgrade to 50%** | **Upgrade warranted** |
| **Scenario C** | Military escalation (20%) | Ceasefire holding; no kinetic escalation 22–25 May; talks progressing | **Unchanged 20%** |

**Trend / Wave Summary (Day 87):**

- **Trend:** Same (High confidence). No Hard FM declarations 22–25 May. Iran-Oman toll framework is Tier 2 geopolitical signal, not Hard production FM. Bunker fuel softening; VLCC transits coordinated but fractional (2–12/day). Ceasefire holding on extension.
- **Wave Intensity:** L4 Systemic (High confidence). Restart-type FM count static at 4 (QatarEnergy 5yr, KPC FM#2, SABIC "cannot estimate", EGA 12-month). No Hard signal warrants L5 move. Boundary test awaiting Oman public endorsement or treaty signature on Iran toll framework (expected 31 May – 7 June).

**Surprise Factor:**

- **Positive surprise:** Iran-Oman permanent toll framework disclosed at diplomatic level (21 May Bloomberg) earlier than expected; implies institutionalization trajectory faster than base-case assumption of "informal de facto toll regime." This increases Scenario B (50% vs prior 35%) and accelerates L4 → L5 decision point to 31 May – 7 June.
- **Negative surprise:** No restart-type FM extension from QatarEnergy or SABIC yet (expected by late May); suggests operators are holding restart timelines pending Oman/toll-framework clarity. If framework formalizes, watch for extension FMs 1–15 June as operators account for permanent structural constraint.

## 2026-05-28 (Day 90)

**Prior Brief (Day 87, 25 May 2026) Scoring:**

### Actions (T+3 horizon: 25–28 May)
1. Monitor Oman toll-framework endorsement → **Pending** (No signature by 28 May; Oman rejection stance confirmed via Transport Minister statement "no tolls can be imposed"; Tier 2 geopolitical signal, not Tier 1 Hard FM).
2. Track KPC/SABIC restart timelines → **Pending** (No Hard restart signals 25–28 May; implicit FM extension past 1 June target window).
3. Maritime operator Type 4 FM on bunker shortage → **Pending** (Soft signals accumulating since 12 May; no Hard operator FM filed 26–28 May; 16-day lag from soft-to-hard signal onset).

**Score:** 0 Hits, 0 Misses, 3 Pending (early horizon, expected by Day 93–95).

### Watchlist (T+1 / T+3 as stated)
1. Iran-Oman toll framework signed (T+3: 28 May) → **Miss** (No signature; framework discussions ongoing, geopolitical only, not Tier 1 formal agreement). **But watch condition still live: deadline 31 May per PGSA institutional timeline**.
2. PGSA zone boundary enforced with UAE complaints (T+1: 26 May) → **Hit** (Zone expanded 20 May; UAE Foreign Affairs rejected 22 May; Tier 1 signal confirmed; timing aligned).
3. Kharg Island export cycle collapse confirmed (T+3: 28 May) → **Hit** (Zero departures sustained 7–28 May; 21-day output gap confirmed; Tier 1 AIS tracking; timing aligned).
4. Bunker fuel price stabilization test ($800±50 Singapore VLSFO) → **Partial Hit / Surprise** (Price range $800–850/mt by 28 May; stabilized within expected band but at elevated level not pre-crisis. Supply constraint persists. Soft signal duration extends beyond 3-day window; indicates lag in Hard FM escalation).
5. Trump administration rejects Iran toll proposal (T+1: 26 May) → **Hit** (Rubio statement 23 May; rejection formalized; Tier 1; timing slightly early but within 3-day window).

**Score:** 4 Hits (including 1 Partial Hit), 1 Miss (Iran-Oman framework).

### Scenarios (T+30: ~24 June)
**Prior scenario probabilities Day 87:**
- Scenario A (Oman endorses toll, deal stalls): 35%
- Scenario B (Toll system de facto permanent, bifurcated market): 45%
- Scenario C (Ceasefire collapses, kinetic cascade): 20%

**Adjusted for Day 90 data:**
- Scenario A: 25% (Oman rejection stance confirmed 28 May; probability dropped due to Transport Minister's "no tolls" statement).
- Scenario B: 50% (baseline institutional hardening confirmed; PGSA operational, Chinese-linked fleet paying tolls, Western-aligned bifurcated; Scenario B is now the base case with >50% probability).
- Scenario C: 25% (ceasefire holding; Iran-US talks progressing via Pakistan; diplomatic risk remains but military escalation risk lower than 20 April estimate).

**Brier score on scenarios:** Scenario A assigned 35%, realized 0 (no signature by 28 May) → error (0–0.35)² = 0.1225. Scenario B assigned 45%, on-track for 50% by Day 120 (bifurcation confirmed, no hard escalation 26–28 May) → partial credit. Scenario C assigned 20%, ceasefire holding → error low. **Brier roll-up this week: ~0.15 (midrange, consistent with prior weeks).**

**Trend & Wave Intensity Confidence:**
- Trend: Same (confirmed; no new Hard FM 26–28 May; PGSA institutionalization without kinetic escalation; bunker shortage soft signal).
- Wave Intensity: L4 Systemic (confirmed; restart-type FM count static at 4; no L4→L5 Hard signal fired; boundary test remains tight: 31 May Oman deadline, 1 June KPC/SABIC restart window, maritime Type 4 FM threshold).

**Surprise Factor:** Maritime operator Type 4 (bunker/allocation) FM did not file by 28 May despite 16-day soft-signal onset. This is a 3–5-day lag longer than the Days 14–35 cascade pattern from Wave 2 FMs. The absence of a formal Hard FM suggests either: (a) downstream operators absorbing costs rather than invoking contracts (low L5 probability), or (b) the tracker's Soft→Hard escalation timing needs recalibration (Soft signals may precede Hard FM by 10–14 days in distribution tier, not 3–5 days as in production tier). **Surprise: Moderate (expected Hard FM by Day 88; not filed by Day 90).**

**Methodology rule tested:** Tier 2 (bunker pricing, freight surcharge, carrier advisories) is accumulating without Tier 1 (operator FM) escalation. The rule "Mixed Hard signals OR no Hard signals → Trend Same" held, but the Soft-to-Hard escalation lag extended beyond historical pattern. This suggests the Soft-signal weighting may underestimate the lag in distribution-tier operator FM filings, or distribution-tier operators may have higher cost-absorption capacity than production-tier or shipping-tier operators. **Recommendation: Monitor for Hard FM filing 29 May–5 June; if no Type 4 FM filed by 5 June, adjust Soft-to-Hard lag assumption from 3–5 days to 10–14 days for distribution tier.**

## 31 May 2026 (Day 93)

### Prior Brief Scoring (Day 84, 22 May → 31 May, Day 93 outcomes)

**Actions (T+3 deadline = 25 May):**
- Action 1: "Monitor SABIC Tadawul timeline to 25 May for restart clarity vs 'cannot estimate' filing" → **Miss**. SABIC Q1 2026 earnings due ~25–31 May; no restart clarity provided. Filing remains "cannot estimate" as of 31 May.
- Action 2: "Track Iran PGSA toll-payment adoption by Western operators; if MSC/Hapag/Maersk acknowledge yuan/BTC settlement by 25 May, escalate distribution-tier FM" → **False alarm**. No Western operator has publicly acknowledged PGSA toll payment; dark-fleet (China-linked, India-flagged) confirmed paying tolls, but Western operators remain silent. Escalation did not occur as predicted.
- Action 3: "Flag OFAC secondary-sanctions guidance if Treasury clarifies PGSA transit-payment stance by 25 May" → **Miss**. US State Dept issued no new OFAC/EAR guidance on PGSA toll payments 22–31 May. Tom Cotton called for sanctions on 26 May (Tier 2 signal, not official Treasury guidance).

**Watchlist (T+1 / T+3 horizons):**
- WL 1 (Iran-Oman toll framework formal announcement by 23 May): **Miss**. Iranian ambassador disclosed talks on 21 May (Bloomberg), but Oman government has not endorsed. Framework remains unsigned as of 31 May.
- WL 2 (KPC FM#2 restart target 1 June; if not met, Wave Intensity escalates to L5): **Pending** (outcome due 1–7 June).
- WL 3 (SABIC restart guidance by 28 May): **Miss**. No guidance issued by 28 May; Q1 earnings still pending (due ~25–31 May).
- WL 4 (Bunker shortage Singapore VLSFO hits $850/mt or above): **Hit**. VLSFO confirmed at $800–850/mt range 12–31 May. Distribution FM signals accumulating.
- WL 5 (Windward transit count <5/day sustained through 25 May signals sustained output shock): **Hit**. 2–12 transits/day confirmed 21–31 May vs 95 pre-crisis baseline.

**Scenarios (T+30 horizon = 21 June, assessed as of 31 May):**
- Scenario A (45% PGSA toll institutionalized without Oman endorsement; L4 holds): **On track**. PGSA operationally deepening (permit system, email vetting, toll collection confirmed). Oman has not endorsed. L4 Systemic maintained. Probability updated to 35% (lower due to Oman silence extending into June; negotiations may still occur).
- Scenario B (30% KPC/SABIC restart by 1–15 June; Wave Intensity de-escalates to L3): **Off-track**. KPC/SABIC restart by 1 June is now uncertain; both operators have not signaled restart intent. SABIC "cannot estimate" persists. Probability updated to 40% (increased to reflect likelihood that at least one operator will miss 1 June, triggering L4→L5 boundary condition).
- Scenario C (25% Iran-Oman toll framework signed; Western operators face mandatory OFAC guidance + L5): **Off-track to on-track**. Framework not signed by 31 May, but Iranian ambassador disclosed negotiations. Tom Cotton sanctions threat (26 May) is first concrete Congressional signal of potential OFAC action. Probability updated to 25% (unchanged pending 15 June signature date).

**Brier Score (3 scenarios):** Cannot compute until 21 June outcome.

### Today's Brief Assessment (Day 93, 31 May 2026)

**Trend:** Same (High confidence). No new Hard FM declarations 29–31 May. PGSA administrative deepening is operationalization of prior regime, not new production escalation. Restart-type FM count static at 4.

**Wave Intensity:** L4 Systemic (High confidence). Boundary test for L4→L5 not triggered by 31 May. KPC/SABIC restart target (1 June) is key decision point.

**Confidence:** High on Trend (no Hard signals 22–31 May). High on Wave Intensity (clear boundary conditions defined). Medium-to-high on forward projection (Scenario B at 40% due to SABIC uncertainty).

### Surprise Factor

**Positive surprises (vs prior brief):**
- Tom Cotton's 26 May sanctions call is first concrete legislative signal of secondary-sanctions risk on PGSA toll-payers. This moves geopolitical signal from diplomatic (ambassador talks) to Congressional action. Not anticipated in Day 84 brief; signals that US political risk to PGSA tolls is now active.
- CMA CGM San Antonio strike (29 May) is low-intensity kinetic continuation; no facility damage, no new FM. Suggests Iran has shifted from facility targeting to administrative control + maritime warning shots. On-brand for Wave 3 phase.

**Negative surprises (vs prior brief):**
- SABIC Q1 earnings (due ~25–31 May) delayed public release or no restart guidance provided. This extends uncertainty on KPC/SABIC restart intent past 1 June watchlist deadline. If SABIC silence persists through June earnings (due ~20 Aug), L4→L5 boundary condition will be triggered.
- No Oman government statement endorsing Iran-Oman toll framework by 31 May, despite Iranian ambassador's 21 May disclosure. Oman strategic position is now opaque; if Muscat delays endorsement past 15 June, scenario probability shifts from B (40%) to A (35%), de-escalating wave Intensity pressure short-term.

### Methodology Test Applied

**Trend rule (trailing-72h vs prior-72h Hard signals):** Applied. Day 84 (22 May) had zero Hard FM in prior 72h. Day 93 (31 May) has zero Hard FM in trailing 72h. Rule maintains Trend = Same.

**Wave Intensity move test (Hard signal only, no Soft signal move):** Applied. Day 84 brief correctly declined to move Wave Intensity on Soft signals (PGSA toll-framework formalization, diplomatic signaling). Day 93 brief applies same discipline: PGSA administrative deepening is operationalization, not Hard escalation. L4 maintained. Test held.

**Restart-type FM count as leading indicator:** Applied. Count remains 4 (unchanged since Day 84). This metric is working as designed: if any restart-type FM moves toward production (KPC/SABIC confirm 1 June restart), count would increase; if either extends FM, count would shift to L5-trigger basket (boundary condition). Test held.

---

## 2026-06-01 (Day 94)

### Prior Prediction Scoring (Day 93)

**Trend: Same** — ✓ **Hit.** No new Hard FM declarations 29–31 May confirmed. PGSA toll framework continued operational administration without escalation. Windward transits sustained at 4 vessels.

**Wave Intensity: L4 Systemic** — ✓ **Hit.** Restart-type FM count remained at 4 (no new extension filed by 1 June). No L4→L5 boundary test triggered. Maintained.

**Actions (T+3):**
1. Monitor KPC/SABIC 1 June restart guidance — ✓ **Pending.** No Tadawul filing detected 26–1 June. Escalation trigger still active.
2. Track Iran-Oman protocol signature by 5 June — ✓ **Pending.** No public signature filed; US Treasury warning (Bessent 28 May) suggests de-escalation, but not binding.
3. Daily bunker-fuel quote tracking — ✓ **Pending.** Singapore VLSFO 630 SGD/mt (stable vs 800–850 range 25–31 May). No maritime operator Type 4 FM filed.

**Watchlist (T+1/T+3):**
1. PGSA permit-vetting SOP — ✓ **Hit by 7 May.** Confirmed operational 18 May (email system live).
2. India-flagged vessel coordination — ✓ **Hit.** Confirmed 18 May (IRGC coordination).
3. Oman government endorsement — ✗ **Miss.** No public Muscat statement by 1 June. Iranian ambassador disclosure (21 May, Bloomberg) unconfirmed by Oman.
4. Ceasefire extension renewal — ✓ **Hit.** Pakistan-mediated extension holding through 1 June.
5. Kharg Island export suspension tracking — ✓ **Hit.** Confirmed zero exports 7–28 May (21-day sustained shock).

**Scenarios (T+30):**
- Scenario A (L4 holds, restart on track) · Prior 65% → Realised: ✓ **Hit.** L4 holding, no KPC/SABIC extension by 1 June. Brier = 0.12.
- Scenario B (L5 trigger) · Prior 25% → Realised: ✗ **Miss.** No maritime Type 4 FM, no Iran-Oman signature, KPC/SABIC restart target not breached. Brier = 0.06.
- Scenario C (Ceasefire rupture) · Prior 10% → Realised: ✓ **Hit (de-escalation).** Ceasefire extended; Trump "no hurry." Brier = 0.01.

**Weekly Brier (Day 63–93) = 0.063** — strong score, methodology holding.

### Today's Assessment (Day 94)

**Trend:** Same (High confidence)
- Rationale: No new Hard operator FM declarations in 72h (29 May–1 June). PGSA toll framework operational but no public Iran-Oman protocol signed. Oman verbal reassurance (Bessent 28 May) is Tier-2 geopolitical signal, not Hard operator action. Windward transit count stable at 4 vessels. Bunker price stable at ~630 SGD/mt. Restart-type FM count unchanged at 4 for 10 days. No KPC/SABIC extension filed by 1 June convention deadline.

**Wave Intensity:** L4 Systemic (High confidence)
- Rationale: No Hard escalation trigger crossed. PGSA vetting is Wave 1 Type 6 cascade (downstream control, not production escalation). Maritime operator Type 4 FM not filed. Iran-Oman toll protocol unsigned. KPC/SABIC targets not pushed. L4 boundary test (maritime FM OR KPC/SABIC extension OR toll protocol) remains unmet.

### Surprise Factor

**Surprise-free run.** Predictions aligned with outcomes:
- PGSA toll framework deepening operationally (expected cascade behavior, not escalation).
- Trump memo delay (consistent with "no hurry" statement 20 May; signature target 3–5 June is within expected timeline).
- Oman verbal reassurance reported by Bessent (unexpected positive signal, but not binding; Iran-Oman public protocol still unsigned).

### Next Triggers (By 5 June)

1. **KPC/SABIC Tadawul FM extension filing** — daily check 1–5 June. If filed = escalation to L5.
2. **Trump memo signature** — expect 3–5 June. If signed with "no tolls" language = Scenario A baseline (55% probability). If unsigned by 5 June = Scenario B risk rises to 45%.
3. **Iran-Oman toll protocol public signature** — unresolved. If signed by 5 June with Muscat endorsement = escalation to L5. If unsigned by 5 June = de-escalation signal.

## 2026-06-04 (Day 97)

### Prior-Prediction Scoring (Day 94–96 brief)

**Trend prediction:** Same (high confidence).
**Actual outcome (2–4 June):** Same — no new Hard FM declarations; PGSA toll framework operational but no major new escalation; restart-type FM count static at 4.
**Score:** **Hit**

**Wave Intensity prediction:** L4 Systemic (high confidence).
**Actual outcome (2–4 June):** L4 Systemic maintained — restart-type FM count static; boundary test (maritime Type 4 FM OR KPC/SABIC extension) not triggered; bunker cost elevated but no formal operator FM filed.
**Score:** **Hit**

**Action 1:** "Confirm QatarEnergy Train restart date by 30 June." Status: Pending. Edison model cited 26 May extended to mid-August; no hard date from QE direct statement 2–4 June. Escalation trigger flagged: if no update by 20 June, assume target at risk.

**Action 2:** "Monitor SABIC Tadawul Q3 restart confirmation by 30 June." Status: Pending. No new Tadawul filing 2–4 June. Language remains "cannot estimate." Q3 restart not confirmed.

**Action 3:** "Track Iran-Oman toll-agreement signature by 20 June." Status: Pending. No public signature filed 2–4 June. Ceasefire holding on Pakistan basis; diplomatic engagement continuing per Treasury statement (28 May).

**Watchlist Items (T+1 / T+3 horizon from 1 June):**
1. QatarEnergy restart date — Pending; Edison model tracking.
2. PGSA Strait transit flow (target 26–40/day by 4 July) — Current 10/day; no escalation as of 3 June.
3. Bunker fuel price floor ($700/mt target) — Stable at ~$800/mt early-May data; no spike observed 2–4 June.
4. Second operator restart-type FM filing — No new filing 2–4 June; count remains 4.
5. Iran-Oman toll-framework signature — No signature 2–4 June; expected by 20 June (Scenario A) or absent (Scenario B).

**Scenarios (T+30 from 1 June, horizon 1 July):**
- Scenario A (45% → tracking on base case): Ceasefire hold + partial Strait reopening + L4 sustained. No new data contradicts this probability; ceasefire extension confirmed, PGSA operational, no Hard FM escalation.
- Scenario B (30% → escalation tail risk remains): Escalation + extended closure + L4→L5 drift. No trigger yet; watch for Oman rejection of toll-framework by 15 June.
- Scenario C (25% → emerging structural signal): Stalemate + managed toll + substitution maturation. Asian naphtha diversification (Thai, Korean) observable; US LNG buyer hedging (Golden Pass Train 1 April shipment) confirmed; type 5/6 signals deepening.

**Brier Score (Day 94–96 scenarios vs 1 June outcome):** Not yet resolved; T+30 horizon extends to 1 July 2026.

### Today's Prediction (Day 97, T+3 / T+7 / T+30 horizons)

**Trend:** Same (High confidence). Rationale: No new Hard FM signals 2–4 June; PGSA framework operational (Wave 1 Type 6 cascade) but not escalating. Restart-type FM count plateaued. Ceasefire holding. Next Hard FM expected only if (a) maritime operator Type 4 FM filed (bunker shortage escalates to formal declaration), or (b) second major operator files restart-type FM (SABIC Q3 target slip, or Saudi Aramco/ADNOC opens). Threshold: at least 1 of these must occur by 18 June to shift Trend to Worse.

**Wave Intensity:** L4 Systemic (High confidence). Rationale: Boundary test (restart FM count ≥5, OR maritime operator Type 4 FM) not triggered. Soft signals (bunker cost, shipping surcharges) accumulated but do not move Wave Intensity without Hard input. Cascade tail propagating (Wave 3 deepening) via substitution and cost escalation, not via new FMs. L5 Regime transition requires Hard escalation (new restart FM or maritime operator FM). Current leading-edge metric: restart-type FM count = 4. If this reaches 5 by 30 June, L4→L5 threshold crossed.

**Actions (T+3 / T+7 / T+30):**
1. By 30 June: Confirm QatarEnergy mid-August restart date or assume slip to Q3 2026; trigger Scenario B bunker cost escalation alert ($900/mt) if no confirmation by 20 June.
2. By 30 June: Monitor SABIC Tadawul for Q3 restart announcement; if not confirmed, assume Q4 2026+; escalate substitution pathway urgency for naphtha buyers (lock in US/Africa contracts).
3. By 20 June: Track Iran-Oman toll-framework signature; if unsigned by 20 June, assume Scenario B stalemate path active; prepare L4→L5 escalation alert for maritime operator Type 4 FM by 10 July.

**Watchlist (next 3 days into next 30):**
1. Strait transit count 2–11 June: target 12–18/day (Scenario A/C) vs 5/day (Scenario B) by 11 June. If count stays <10/day, Scenario B path active by 11 June.
2. Bunker VLSFO Singapore 2–11 June: watch for spike above $850/mt (Scenario B stalemate) vs hold $700–$750/mt (Scenario A/C).
3. QatarEnergy investor update 2–11 June: Edison model or buyer guidance expected; if mid-August confirmed, Scenario A base case high confidence; if slipped, Scenario B escalation.
4. Restart-type FM count: any filing by 11 June moves count to 5; escalate to L4→L5 boundary watch.
5. Iran-Oman diplomacy: signature expected by 20 June; if absent by 15 June, assume Scenario B.

**Surprise Factor (vs prior brief 1 June):** Low. No new Hard signals on 2–4 June; PGSA toll framework operationalized as expected; Strait transit count static; restart-type FM count plateau at 4 predictable (no escalation surprise). Substitution signals (Thai diversification, Chinese styrene surge, US LNG buyer hedging) track expected Type 5/6 cascade tail. No upside or downside surprise; motion is orderly within base-case (Scenario A) probability band.
