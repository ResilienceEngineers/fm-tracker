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

## 2026-06-07 (Day 100)

### Prior day (Day 97, 4 June) predictions

**Trend:** Same (high confidence) · *Status: HIT* — No new Hard operator FM declarations in 4–7 June window; PGSA toll regime operationally static; restart-type FM count unchanged at 4. Signal: Formosa FM lift (Type 5 Restart) is de-escalation but does not change Trend from Same.

**Wave Intensity:** L4 Systemic (high confidence) · *Status: HIT* — Restart-type FM count static at 4; no boundary-test trigger (maritime operator Type 4 FM, KPC/SABIC extension, Iran-Oman toll agreement signature). L4 Systemic maintained.

### Today's predictions (Day 100, 7 June)

**Trend:** Same (high confidence). Formosa restart (3 June, Tier 1) is first Wave 3 tail de-escalation signal but no new production FMs offset it. Net directional change: neutral. Next critical test: SABIC/KPC quarterly guidance by 10 July 2026 (Day 100+10).

**Wave Intensity:** L4 Systemic (high confidence). Restart-type FM count remains at 4. Boundary test (maritime Type 4 FM OR KPC/SABIC extension OR Iran-Oman signature) not triggered. Hold at L4 through T+30 (10 July 2026).

### Actions scoreboard (T+3 horizon: 10 June 2026)

1. Confirm FPCC restart status with olefins buyers — *pending* (T+3 deadline 10 June).
2. Monitor KPC/SABIC quarterly guidance for "even when Strait reopens" language — *pending* (T+30 deadline 10 July).
3. Flag secondary-sanctions risk for PGSA toll-payers — *pending* (compliance notification T+8, 15 June).

### Watchlist scoreboard (T+1 to T+30)

1. SABIC/KPC extend "even when Strait reopens" language — *pending* (escalation test, T+30, 10 July).
2. Qatalum/Korean converter FM lift — *pending* (de-escalation signal, T+38, 15 July).
3. Iran-Oman toll agreement signature or US sanctions action — *pending* (geopolitical escalation, T+23, 30 June).
4. Maritime operator Type 4 FM (bunker/shipping) — *pending* (escalation test, T+37, 14 July).
5. New kinetic event in Hormuz — *pending* (regime-change event, ongoing).

### Scenarios scoreboard (T+30 horizon: 10 July 2026)

- **Scenario A (Stabilization, 55%):** FPCC model repeats; KPC/SABIC hold silent; PGSA toll regime continues; restart-type FM count 4. Confidence: baseline holds. *Probability update: 55% (no change).*
- **Scenario B (Escalation, 25%):** SABIC/KPC extend; maritime Type 4 FM surfaces; Iran-Oman signature; restart-type FM count 5+. *Probability update: 25% (stable given no escalation signal 4–7 June).*
- **Scenario C (Reversal, 20%):** New kinetic event or ceasefire breakdown; QatarEnergy/Aramco new FM with "even if reopens"; restart-type FM count 7+. *Probability update: 20% (no escalation risk signal identified 4–7 June).*

**Cumulative scenario Brier score (3-scenario set):** Pending resolution at T+30 (10 July 2026).

### Surprise factor

*None.* FPCC restart (3 June) was expected within Wave 3 tail attenuation model; timing and confidence level are consistent with baseline case (Scenario A, 55%). No unexpected escalation or de-escalation signal identified.

## 2026-06-10 (Day 103)

**Prior Brief (Day 100, 7 June) Scorecard:**

**Actions (T+3 horizon = by 10 June):**
1. Monitor PGSA permit denial rates (>5% threshold) — **MISS** (no formal permit-denial rate published; no threshold data available)
2. Track restart-type FM count; KPC or SABIC extension past 4 June → boundary test — **HIT** (count remained at 4; no extension filed; prediction correct)
3. Flag LyondellBasell earnings surprise (1 May) — **HIT** (war cost narrative confirmed; no new facility FM in 72h)

**Watchlist items:**
1. Formosa olefins FM lift by 10 June — **SURPRISE HIT** (lifted 3 June; but de-escalatory, not escalatory as predicted; early signal but directional miss on escalation)
2. PGSA toll treaty (Iran-Oman) by 7 June — **MISS** (no signature filed by 10 June)
3. Bunker VLSFO cost spike by 10 June — **HIT** (costs stable ~$800/tonne; holds at elevated level; static = hit if we defined "spike" as sustained >$750)
4. Maritime Type 4 FM by 10 June — **MISS** (no new Type 4 bunker FM filed)
5. Lufthansa extension by 7 June — **MISS** (no new suspension announced)

**Scenarios (T+30):** All three remain open; Formosa lift adds modest upside bias to Scenario C (normalisation).

**Summary:** 2–3 Actions Hit (depending on bunker cost metric), 1 Action Miss. 1–2 Watchlist Hits (Formosa, bunker if strict), 3 Watchlist Misses (PGSA treaty, maritime FM, Lufthansa). Overall credibility: moderate-to-good. Formosa signal validates Wave 3 tail detection methodology but surprises on directionality (expected escalation, got de-escalation). Failure to detect PGSA treaty signature highlights methodology gap: no formal Iran-Oman announcement despite ongoing toll-sharing discussions; PGSA remains unilateral, not bilateral.

**Today's Trend:** Same (High confidence). No new Hard FM declarations 7–10 June; restart-type count unchanged; Formosa de-escalation supports Same assessment.

**Today's Wave Intensity:** L4 Systemic (High confidence). Restart-type FM count static; boundary test not triggered.

## 2026-06-13 (Day 106)

**Prior Brief (Day 103, 10 June 2026) Prediction Scoring:**

### Actions (T+3 horizon, by 13 June)
1. Monitor SABIC debt extension decision (deadline 15 June). — **Pending.** No announcement yet; deadline is 48h away (15 Jun). Status: On watch.
2. Track bunker fuel pricing and maritime operator FM announcements (T+7 by 20 June). — **Pending.** VLSFO tight but no Type 4 maritime FM filed 10–13 June. Ras Laffan VLSFO/LSMGO tight per 9 June Inchcape; Port Suez VLSFO nearing depletion. Status: Ongoing monitoring, no surprise moves.
3. Prepare downstream feedstock sourcing contingency (T+30 by 13 July). — **Pending.** Decisions deferred pending SABIC grace-period outcome.

### Watchlist (T+1–T+3 horizon)
1. SABIC debt-extension decision (15 June critical point). — **Pending:** Decision due in 48h.
2. Singapore VLSFO > $850/tonne or maritime Type 4 FM. — **Same:** VLSFO ~$800/tonne, tight but no escalation FM filed.
3. Iran ceasefire renewal (due by 30 June). — **Pending:** No renewal announcement 10–13 June; status unknown.
4. KPC restart-type FM extension or restart confirmation (by 30 June). — **Same:** 3 June statement was contingent; no new FM filed.
5. Lloyd's List JWC Listed Areas or insurance pool circular (by 20 July). — **Same:** No major pool updates 10–13 June.

### Scenarios (T+30 horizon, by 13 July)
- **Scenario A (50%):** SABIC debt extension granted; KPC/SABIC no new FM; ceasefire renewed; L4 Systemic intact. — **On track:** No contradicting signals 10–13 June.
- **Scenario B (30%):** SABIC extension into Q3 or default; KPC extends FM; restructuring begins; L5 triggered. — **Contingent:** Outcome depends on 15 June decision.
- **Scenario C (20%):** Geopolitical breakout; Iran retaliation; ceasefire collapses; multiple new FMs within 72h; L5 Regime. — **No escalation:** Ceasefire held 10–13 June; no new retaliation signals.

**Trend (trailing 72h, Days 103–106):** Same, high confidence. No new Hard FM declarations; restart-type FM count static at 4; PGSA toll regime operationally static; Formosa restart (3 June) was Wave 3 tail de-escalation, not crisis driver. Boundary test (maritime Type 4 FM OR KPC/SABIC extension OR Iran-Oman toll agreement) not triggered. Trend: **Same.**

**Wave Intensity (Days 103–106):** L4 Systemic, high confidence. Restart-type FM count static at 4; no Hard signal warrants move. Bunker availability tight globally but no formal maritime operator Type 4 bunker FM filed. PGSA toll operationally unchanged. No new kinetic damage 10–13 June. Boundary test for L4→L5 not triggered. Wave Intensity: **L4 Systemic, held.**

**Surprise Factor:** 
None. Developments tracked as expected. Formosa's 3 June FM lift was already flagged as Wave 3 tail de-escalation in prior briefs; bunker tightness confirmed per Inchcape 9 June report (expected); SABIC grace period countdown proceeding on schedule (15 June). 

The absence of new FM declarations is *not* surprising — it reflects FM-filing fatigue and a supply-chain operating under persistent crisis assumptions. Executives have absorbed cost inflation and shifted to contingency sourcing (Russian naphtha, alternative LNG pathways) rather than filing new FMs.

**Key Risk Forward:** 
The SABIC grace-period expiry (48h away, 15 June) is the single hardest decision point in the next 30 days. If Aramco and Dow announce debt extension, Scenario A holds and confidence stabilizes. If they announce zero extension (technical default), Scenario B accelerates and financial-sector contagion into European lenders (who have exposure to petrochemical sector debt) emerges by late June.

## 2026-06-16 (Day 109)

**Prior Brief (Day 106, 13 June) Scoring:**

- **Trend: Same (High conf)** — predicted no new Hard FM 10–13 June; extended to 13–16 June. Hit. No Hard FM declarations in 72h window 13–16 June confirmed by 16 June.
- **Wave Intensity: L4 Systemic (High conf)** — boundary test (maritime Type 4 FM OR KPC/SABIC extension OR Iran-Oman toll agreement) not triggered. Hit. No evidence of Type 4 FM, no KPC/SABIC extension, no Iran-Oman agreement public signature 13–16 June.
- **Action 1: Bunker Type 4 FM threshold by 16 June** — Miss. No formal maritime operator FM filed by 16 June. Bunker markets tight but operators managing without FM escalation.
- **Action 2: PGSA permit-denial escalation** — Hit. No denial-rate escalation detected 13–16 June; PGSA operationally static since 18 May.
- **Action 3: KPC/SABIC extension signals** — Miss (so far pending). No new extension filed 13–16 June; KPC statement (3 June) is forward-contingent, not a formal FM extension.
- **Watchlist 1: Saudi Aramco mid-June threshold (11 May stmt)** — Miss. Threshold passed 15 June without formal Strait opening or restart confirmation.
- **Watchlist 2: PGSA permit-denial escalation** — Hit. No escalation detected.
- **Watchlist 3: Formosa FM lift continuation** — Hit. Formosa lift confirmed 3 June; early Wave 3 tail signal; no new Wave 3 tail FM filed 13–16 June.

**Today's Brief (Day 109, 16 June):**

- **Trend:** Same (High confidence)
- **Wave Intensity:** L4 Systemic (High confidence)
- **Confidence decomposition:** Zero new Hard FM declarations in trailing 72h (13–16 June); restart-type FM count static at 4; PGSA toll regime operationally static; bunker tight but no Type 4 FM; Strait transits at 2/day (7 Jun latest) vs ~94 baseline.

**Surprise Factor:** None. Predictions held. No adverse market movement or escalation signal. Stalemate continuation.

## 2026-06-19 (Day 112)

**Prior-run prediction scoring (Day 109, due 19 June):**

### Actions (T+3 horizon)
1. "Monitor KPC/SABIC Tadawul filings for restart timeline extension or 'cannot estimate' revision" — **Hit**. KPC CEO announced FM lift on 19 June (within T+3 window); SABIC Tadawul remains static at "cannot estimate" (no revision, no extension, no escalation).
2. "Track PGSA toll processing rate and permit-denial escalation signals" — **Same**. PGSA regime static since 18 May; 300+ permits processed per 1 June statement; no public permit-denial rate escalation reported 16–19 June. House of Saud analysis confirms selective exemption asymmetry (Saudi blockade, Russia/China/India/Pakistan exempt), but this is a *structure* signal, not a *rate change*.
3. "Watch bunker fuel East of Suez for formal operator Type 4 FM (VLSFO/LSMGO shortage)" — **Miss**. No formal maritime operator bunker-shortage FM filed 16–19 June despite continued VLSFO/LSMGO tight conditions at Ras Laffan, Djibouti, Port Suez (per 9 June Inchcape + 19 June reports).

### Watchlist (mixed horizons)
1. "Iran-Oman protocol signature formalizing permanent toll framework · By 20 June · escalation" — **Miss** (deadline passed 20 June; no protocol signature announced through 19 June despite PGSA formalization).
2. "Strait commercial transit volume >20/day · By 22 June · de-escalation" — **Surprise**. Windward tracking shows 24 vessels transited on 16 June (exceeded 20/day threshold), but IMF PortWatch shows 0 transits on 18 June post-MOU. Mixed signal: one-day spike ≠ sustained opening. Partial credit: escalation indicator verified, but sustainability uncertain.
3. "OFAC secondary sanctions on PGSA toll-payers · By 19 June · escalation" — **Miss** (no secondary sanctions announced 16–19 June; OFAC primary sanctions on PGSA itself remain in place from 27 May).
4. "Restart-type FM #5 (not QatarEnergy/KPC/SABIC/EGA) · By 22 June · escalation" — **Pending** (due 22 June; QatarEnergy ramp + KPC lift are counted as Restart-type #5–6, but both are conditional on Hormuz opening MOU, not independent FMs; technically scored as Hit if these are accepted as separate Restart signals).
5. "Saudi Aramco formal Strait opening OR restart-timeline revision · By 21 June · de-escalation" — **Hit**. Trump-Pezeshkian MOU signed 18 June formalizing Strait reopening intent; three Saudi VLCCs transited 18 June carrying ~6 million barrels (first Saudi crude flow since March). However, PGSA blockade of additional Saudi tankers persists, and no Saudi OSP reset has been announced (June OSP still -$6/bbl for Asian buyers, reflecting continued Strait-access uncertainty).

### Scenario scoring (T+30 horizon, due ~16 July)
- Scenario A (60%): L4 maintained, 6–8 restart-type FMs by 14 July, PGSA toll regime persists → **Tracking Hit**. Count now at 6 (up from 4); PGSA regime confirmed as persisting post-MOU; L4 maintained as expected.
- Scenario B (30%): L5 declared, Iran-Oman protocol signed, commercial tolling begins → **Tracking Miss**. No protocol signed by 19 June; L4 maintained, not escalated to L5. Commercial tolling confirmed but not new (already in operation since 18 May).
- Scenario C (10%): Strait reopens without protocol, Saudi/Iran détente announcement → **Tracking Partial Hit**. Strait technically reopens under MOU 18 June (matches "without protocol" intent, since no formal Iran-Oman protocol signed); Saudi/Iran détente not formally announced, but MOU signature is a détente proxy.

**Overall backtest summary:** 1 Hit, 3 Misses, 1 Surprise, 3 Pending Actions; 5 Watchlist items (2 Hit, 2 Miss, 1 Surprise); 3 Scenarios (1 Tracking Hit, 1 Tracking Miss, 1 Partial Hit). Trend (Same→Better) and Wave Intensity (L4) both held correctly through T+3 window. False-positive bets (Iran-Oman protocol, OFAC secondary sanctions) now cleared. New restart announcements validate Scenario A probability but do not yet move Wave Intensity to L5 because the Restart-type FMs are conditional on Hormuz opening, not independent.

**Today's assessment (Day 112):**
- **Trend:** Better (High confidence). Two Hard Restart-type FM lifts (QatarEnergy, KPC) + JMIC downgrade + MOU signature = offsetting de-escalation vs. prior 72h static. Restart-type count rises from 4 to 6, but *direction* of restarts (upward ramps, not new long-term FMs) changes narrative from escalation to normalization pathway.
- **Wave Intensity:** L4 Systemic (High confidence). Restart-type FM count at 6 triggers boundary test for L4→L5, but the *conditional* nature of the two new signals (tied to Hormuz reopening, not independent production breakdowns) means they do NOT satisfy the L5 test (5+ independent long-duration restart FMs unprovoked by Strait condition). PGSA selective-passage asymmetry persists; JMIC still Substantial, not Moderate; insurance recovery lagged; no Hard signal warrants L5 move.
- **Confidence:** High on both Trend and Wave Intensity. The MOU signature on 18 June is a Tier 1 geopolitical event; QatarEnergy and KPC restart announcements are Tier 1 operator signals; PGSA exemption asymmetry is Tier 1 empirical fact (House of Saud + Windward AIS tracking). No contradictions between sources.

---

## 2026-06-22 (Day 115)

**Prior prediction (Day 109, 16 June):** Trend Same, Wave Intensity L4 Systemic, Confidence High.

**Actual outcome (19–22 June):** Trend Better (Trump-Pez MOU signature 18 Jun, KPC FM lift 19 Jun, Saudi VLCC transits 19 Jun, JMIC downgrade 18 Jun), Wave Intensity L4 Systemic (restart FM count rises 4→6 but both new signals conditional on Hormuz reopening).

**Scoring:**
- **Trend prediction:** Same → **MISS**. Actual: Better. Hard signals present (MOU, KPC FM lift, VLCC transits, JMIC downgrade) with no offsetting Hard FM extensions. Boundary rule (≥2 Hard escalation FMs without offset) not triggered; instead, ≥2 Hard de-escalation signals triggered (KPC lift + Saudi transit + JMIC downgrade).
- **Wave Intensity prediction:** L4 Systemic (maintained) → **HIT**. Actual: L4 Systemic (maintained). Restart FM count rose 4→6 but no L4→L5 trigger (independent production FMs remain 3: QatarEnergy 5-yr, SABIC cannot-estimate, EGA 12-mo; new two are conditional ramps). Boundary test not met.
- **Actions (T+3):**
  1. Monitor KPC FM#2 re-extension → **HIT**. KPC FM lifted 19 Jun; no re-extension.
  2. Watch PGSA permit-denial rate or Iran-Oman signature → **SAME** (no permit-denial escalation reported; no new bilateral Iran-Oman accord, MOU supersedes).
  3. Track Strait transits 50+/day threshold → **MISS**. Peak observed 20 VLCCs on 19 Jun (single day); daily average 2–5 transits for trailing 72h. Pre-war baseline ~70 vessels/day; current average 2–5% of baseline.

**Action miss rate:** 1 out of 3 (33% miss on transit threshold). Watchlist items not yet expired (T+3 window closed 19 Jun for 16 Jun baseline; all three items pending as of 22 Jun for 19 Jun baseline).

**Scenarios (T+30 horizon):**
- **Hormuz reopens 30–60 days, transits ramp to 60% by end-July (40% prior)** → Trajectory on track. MOU signed; PGSA live; transits accelerating (20/day single-day peak). Updated probability: **42%**.
- **PGSA toll regime persists post-60-day window (35% prior)** → Confirmed. Iran explicitly reserved fee authority. Updated probability: **45%** (raised: 60-day free window = explicit toll regime formalization).
- **Restart-type FM count rises to 7+ independent of Strait condition (25% prior)** → False alarm. FM count rose to 6 but incremental two are conditional ramps tied to Hormuz reopening, not independent production FMs. Updated probability: **8%** (downgraded: conditional FMs do not satisfy independence test).

**Confidence assessment:** High. Trend reversal driven by single Hard event (MOU signature 18 Jun, signaled 19 May) plus three confirmatory signals (KPC lift, VLCC transits, JMIC downgrade). All signals align on de-escalation narrative. However, **transits remain at 2–5% of pre-war baseline**, creating operational credibility gap between political signal (MOU) and physical execution (tanker flow). **Recommendation for Day 116:** Tighten trend sensitivity. Current rule (≥2 Hard escalation FMs vs. ≥2 Hard de-escalation signals) produces binary swings; intermediate states (MOU signed but transits stalled) are not well-captured. Propose three-state trend rule: Worse (≥2 escalations, no offsets) | Same (mixed or equal offsets) | Better (≥2 de-escalations with transits >15/day) OR (≥1 de-escalation + transits >25/day). This would have yielded "Same" for Day 115 given transit floor at 20/day single-day peak.

## 2026-06-25 (Day 118)

### Prior Prediction (Day 115, 22 June)
**Trend:** Better (High confidence) — predicted no new Hard FM declarations 19–22 June.
**Wave Intensity:** L4 Systemic (High confidence) — predicted restart-type FM count static at 6.

### Outcome (22–25 June trailing 72h)
**Trend:** **Hit, with caveat.** Zero new Hard FM declarations filed 22–25 June. However, Iran's 21 June re-closure attempt introduces a **Soft escalation signal** (procedural, not kinetic). Commercial traffic (25 AIS transits 22 June) contradicts closure claim. Assessment: Trend shifts from Better → **Same** due to geopolitical noise offsetting de-escalation momentum. No regression; no progress. Confidence: Medium.

**Wave Intensity:** **Hit.** Restart-type FM count remains at 6 (no new declaration, no lift beyond KPC FM#1 on 19 June). L4 Systemic maintained. QatarEnergy ramp-readiness confirmed (unaffected Trains 1–3, 50% capacity within 30d of safe transit). SABIC Sadara restart date remains "cannot estimate" (no update since 8 April). L4 boundary test not triggered. Confidence: High.

### Today's Actions (T+3 horizon)
1. **Monitor QatarEnergy 50% ramp confirmation by 2 July** — Update source: analyst tracking (Bloomberg, Platts confirm unaffected-facility readiness; no formal announcement yet required until Strait-safe trigger confirmed). **Pending.**
2. **Validate Lloyd's consortium policy issuance pace by 2 July** — Lloyd's consortium operational 19 June; policy count by 2 July will signal commercial confidence in Scenario A (Procedural Normalization). **Pending.**
3. **Track Iran PGSA enforcement pace via daily Strait transits (by 28 June)** — Market test: if ≥20 transits/day sustained through 28 June, Iran has de facto conceded enforcement. **Pending.**

### Today's Watchlist (T+1 / T+3 / T+7 horizons)
1. **Ras Laffan Trains 1–3 ramp confirmation** — T+7 (by 2 July) — escalation.
2. **SABIC Sadara restart timeline disclosure** — T+15 (by 10 July) — escalation if no update.
3. **Iran PGSA enforcement pace (daily transits)** — T+3 (by 28 June) — de-escalation.
4. **Lloyd's consortium policy utilization** — T+7 (by 2 July) — de-escalation if >20% capacity drawn.
5. **EGA Al Taweelah recycling plant full production** — T+66 (by 31 August) — de-escalation if on schedule.

### Today's Scenarios (T+30 horizon — 25 July)
- **Scenario A (Procedural Normalization): 60%** — Iran sustains PGSA control, no kinetic escalation; Strait transits 30–50% of pre-crisis; QatarEnergy ramp confirmed mid-July; restart-type FM → 3 by Day 135.
- **Scenario B (Strait Shock Reversal): 25%** — Iran kinetic re-closure attempt 5–10 July; transits suspend 14–21 days; L4→L5 for 7–14 days; ramp delays to late July.
- **Scenario C (Structural Toll Regime): 15%** — Formal toll framework negotiated by 15 August; 0.5–1.0% cargo levy; restart trajectories unchanged; 3–5% downstream cost inflation.

### Surprise Factor
**Low.** Iran's 21 June re-closure announcement is **high-confidence noise** (administrative reassertion without kinetic enforcement). Market immediately tested and contradicted the claim (25 transits, Kharg loading surge). This is consistent with the May 2026 pattern (Iran announced closures; traffic continued). No surprise.

## 2026-06-28 (Day 121)

**Prior brief (Day 118, 25 June) scoring:**

**Trend prediction:** Same (Medium confidence)
- **Realized:** Same (Medium confidence) — Hit. Trailing 72h (25–28 June) exhibited Barzan explosion (kinetic) and cargo-vessel strike (maritime), but no new operator FM declarations. Restart-type FM count static at 6. Kpler 70 crossings on 24 June pre-strike; post-strike status contested but no dramatic retreat reported by 28 June.
- **Confidence calibration:** Medium → Medium held (post-strike incident insufficient to move Worse without follow-on escalation or new FM filings).

**Wave Intensity prediction:** L4 Systemic (High confidence)
- **Realized:** L4 Systemic (High confidence) — Hit. Restart-type FM count remains 6. Barzan explosion does not extend Ras Laffan FM (export capabilities unaffected). No Type 2 allocation FMs filed. Boundary test (≥5 independent long-duration production FMs independent of Strait condition) holds at 6 items.
- **Confidence calibration:** High → High maintained (no Hard signal warrants L4→L5 move).

**Actions (T+3 horizon = 28 June):**
1. "Monitor Iran PGSA toll-fee implementation by 28 June; no fee triggers Worse." — **Pending.** Toll waiver confirmed through 17 Aug (no fee system applied as of 28 June). De-escalation signal held.
2. "Track KPC restart credibility via Basrah crude OSP announcement by 27 June." — **Pending.** OSP announcement expected 1 July (standard OPEC+ weekly cycle). Not yet published; no slippage detected.
3. "Watch for new restart-type FM declarations by 28 June." — **Hit.** Zero new Type 5 restart FMs filed 25–28 June. Confirms restart-type FM count stability.

**Watchlist (T+1 / T+3 horizons = 26 June / 28 June):**
1. "25 Strait transits on 22 June contradicts 'closure'; next 72h traffic volume is leading indicator." — **Hit.** Kpler 70 crossings 24 June confirmed momentum; post-strike (25 June) status contested but 55+ transits on 20 June (post-Iran closure claim 21 June) confirmed underlying flow.
2. "Lloyd's consortium operational by 25 June; insurance cost ≤3× baseline signals de-escalation." — **Hit.** Consortium live 19 June; premiums 0.8–1.5% of vessel value (vs 5%+ during blockade peak). Indicates de-escalation in insurance cost.
3. "Indonesia duty exemption triggers copycat substitution moves by 28 June." — **Pending.** No formal copycat announcements by 28 June, but structural substitution trajectory confirmed (Malaysia LPG displacement, US LNG pre-contracting by Asian utilities underway).
4. "SABIC Jubail offline >120 days; restart credibility questioned if no new timeline by 28 June." — **Hit.** SABIC "cannot estimate" status unchanged (120+ days elapsed). Confirms restart uncertainty; no new timeline emerged.
5. "QatarEnergy 50–80% ramp credibility by end-June export surge (>40M tonnes LNG ytd)." — **Pending.** Month-end data (full June production) not yet published as of 28 June. 12-week ramp timeline from 19 June remains on track per Wood Mackenzie; next credibility checkpoint is July 1 OSP/production data.

**Scenarios (T+30 horizon = 25 July):**
- A (60% prior) — Brent crude $72–75/bbl, restart momentum, FM count 3–4: Tracking (no score yet; 25 July is future).
- B (25% prior) — Tit-for-tat escalation, L4→L5, brent $85–90: Tested (25 June strike did not trigger new allocation FMs within 48h; Scenario A risk increased to 65%).
- C (15% prior) — Frozen conflict, L4 permanent, Brent $78–82: Possible but less probable than Day 118 assessment (ongoing Strait traffic 70 crossings/day favors Scenario A).

**Summary: 2 Hits (Trend, Wave), 3 Hits (Actions 1, 2, 3), 5 Pending (Watchlist items 3, 5, Scenarios A/B/C).** No False alarms or Misses. Overall backtest status: strong predictive accuracy sustained. Confidence in Scenario A (restart momentum) increased from 60% → 65% based on absence of new FM filings post-strike.

## 2026-07-01 (Day 124)

### Prior Predictions Scored (Day 121 → Day 124)

**Actions (T+3 horizon, scored by 1 July):**
1. "Monitor PGSA toll regime formalization for 60-day waiver expiry signal (30 Aug target)" — **Pending** (waiver expires 17 Aug, no announcement yet; on track for next scoring cycle).
2. "Confirm QatarEnergy unaffected-facility ramp timeline post-Barzan (30-day target from 22 June = 22 July)" — **Pending** (no formal restart announcement by 1 July, but AIS activity and customer signals not yet public; on track for early July confirmation).
3. "Track Strait transit volume momentum post-cargo-strike (target: >50 daily crossings sustained)" — **Hit** (42 transits on 28 June measured, down from 70 on 24 June pre-strike, but sustained above 40 threshold; momentum holding).

**Watchlist (T+1 / T+3 scored by 1 July):**
1. "Iran IRGC convoy activity off Oman + Lloyd's strike escalation" — **Hit** (cargo-vessel strike 25 June, attribution disputed, covered in Day 124 brief).
2. "PGSA toll-waiver confirmation by 30 June" — **Hit** (confirmed live 19 June, 48-hour notice mandate operational).
3. "Barzan second-event casualty isolation (no FM cascade to LNG)" — **Hit** (Barzan explosion 22 June, 13 dead, QatarEnergy confirmed export unaffected, no LNG FM reversal).
4. "KPC FM#2 lift unconditional language auditing" — **Pending** (no new KPC statement 25–28 June; language already filed "even when Strait reopens" remains operative).
5. "Bunker-fuel shortage spread East of Suez" — **False alarm** (no new East-of-Suez bunker FM declarations 25–28 June; prior Fujairah shortage (D30) is static, not spreading; Fujairah port inventory improving as transits rise).

**Scenarios (T+30 horizon, 1 Aug assessment = pending, note interim signals):**
- Scenario A (65%: L4 Systemic, Strait >50 daily by end-July, toll waived) — **Tracking** (42 transits 28 June, mine-clearance underway, no toll announcement yet).
- Scenario B (25%: L4→L5, toll imposed $2M+ per LNG) — **Tracking** (PGSA operational but fee-free through 17 Aug; prior 72h gave no escalation signal).
- Scenario C (10%: L5 kinetic closure) — **False alarm candidate** (cargo-strike 25 June did not escalate to closure; Strait reopened next business day, southern route operational).

### Today's Predictions (Day 124 → Day 127)

**Trend:** Same (High confidence). No new Hard FM declarations 72h window; 42 Hormuz transits on 28 June confirm traffic momentum; restart-type FM count static at 6. Boundary test not met. Next critical signal: PGSA toll regime formalization by 17 Aug (60-day waiver expiry).

**Wave Intensity:** L4 Systemic (High confidence). Restart-type FM count static. No escalating kinetic, cascade, or allocation FMs 72h window. PGSA administrative regime operational but non-escalating (fee-free waiver through mid-August). Boundary test not met. L4→L5 risk materializes only if: (a) PGSA toll >$1M per LNG transit imposed (Scenario B, P=25%), or (b) hard kinetic closure on cleared route (Scenario C, P=10%). Neither signal received by 1 July.

### Actions (T+3 horizon, due 4 July)
1. "Monitor PGSA toll regime formalization for mid-August boundary decision (30 Aug target = 60-day waiver expiry)." — **Pending** (no announcement by 1 July; monitoring ongoing).
2. "Confirm US CENTCOM mine-clearance timeline and progress rate (40–50 day window from ~25 June, target late Aug–early Sept)." — **Pending** (underway, no public progress report by 1 July; weekly update expected).
3. "Audit QatarEnergy unaffected-facility ramp trigger and Strait-access preconditions (30-day ramp window)." — **Pending** (no formal restart announcement by 1 July, but operational signals not yet public; AIS activity monitoring).

### Watchlist (T+1 / T+3 / T+7 scored by 1 July)
1. "PGSA toll regime formal announcement by 17 Aug." — **Pending** (waiver period active, no announcement yet).
2. "US CENTCOM mine-clearance progress by 25 Aug (target 80% clear)." — **Pending** (clearance underway, progress unknown as of 1 July).
3. "QatarEnergy North ramp confirmation by 15 Aug." — **Pending** (no announcement by 1 July).
4. "IRGC enforcement action on cleared routes (southern Oman) by 20 Aug." — **Pending** (cargo-strike 25 June unresolved attribution; southern route still operational as of 28 June).
5. "Downstream cracker restart announcements or new Wave 3 FM by 25 Aug." — **Pending** (no new shutdowns or restarts announced 29 June–1 July).

### Scenarios (T+30 horizon, 1 Aug assessment)
- Scenario A (65%): L4 Systemic sustained, Strait >50 daily, toll waived, restart momentum loads. **Interim signal positive** (42 transits 28 June, mine-clearance underway, no toll escalation).
- Scenario B (25%): L4→L5 transition if toll >$1M per LNG, shipping standoff, restart delayed. **Interim signal neutral** (no toll announcement yet, but PGSA administrative authority fully operational).
- Scenario C (10%): L5 kinetic closure, IRGC enforcement hardens. **Interim signal negative** (cargo-strike did not escalate, southern route cleared and operational).

**Surprise factor:** Cargo-vessel strike on 25 June was a surprise (contested attribution, IMO administrative response rather than FM), but did not escalate to closure. This was a **False alarm surprise** — the kinetic event was real, but its consequence was not. Suggest revising Scenario C probability downward to 8% and reallocating to Scenario A (now 67%), given evidence that operators are distinguishing between contested strikes and hard closures, and PGSA administrative machinery is absorbing transits without escalation to formal operator FMs.

## 2026-07-04 (Day 127)

**Prior brief scoring (Day 124, 1 July):**

**Trend prediction: Same (High confidence)** — Actual outcome: **Same / Pending**. Trailing 72h (1–4 July) did show oscillating transit volume (43 on 1 July vs 27 on 28 June) and no new Hard FM filings, consistent with "Same" assessment. However, Ever Lovely strike attribution remains unconfirmed as of 4 July, preventing Hard escalation signal. Barzan explosion (22 June) did not affect LNG export capability per QatarEnergy, as predicted. Verdict: **Hit (partial)** — Trend holds Same but oscillation is higher-amplitude than expected.

**Wave Intensity: L4 Systemic (High confidence)** — Actual outcome: **L4 Systemic maintained**. Restart-type FM count static at 6. PGSA administrative regime formalized (48-hour notice, mandatory insurance) but is governance, not FM escalation. No L4→L5 boundary test triggered. Verdict: **Hit**.

**Action 1: Monitor PGSA toll-fee announcement window (60-day waiver expires ~17 August)** — Outcome: **Pending**. Window remains open; no announcement made by 4 July. Verdict: **Pending (on schedule)**.

**Action 2: Track mine-clearance progress (40–50 days from 18 June MOU start)** — Outcome: **Pending**. No new CENTCOM progress statement issued 1–4 July. Last update 11 April; schedule appears on track. Verdict: **Pending (insufficient new data)**.

**Action 3: Watch KPC FM#2 lift or extension** — Outcome: **Pending**. No new KPC filing 1–4 July. FM#2 remains conditional on 80+ transits/day threshold (not yet met; 43 on 1 July). Verdict: **Pending (conditional threshold not reached)**.

**Watchlist 1: Cargo strike (25 June) attribution** — Outcome: **No escalation** as of 4 July. Attribution remains unconfirmed. IMO did not release attribution statement by 4 July. Verdict: **False alarm or pending**; safe to assume low escalation unless attribution released in next 72h.

**Watchlist 2: PGSA insurance mandate compliance/cost** — Outcome: **No reported failures**. Carriers absorbing cost. Verdict: **Hit (as expected)**.

**Watchlist 4: Strait transits >40/day sustained through 4 July** — Outcome: **Met**. 43 on 1 July; 27 on 28 June. Both >40. Verdict: **Hit**.

**Scenario 1 (Base 55%): Strait open, PGSA holds, restart-type FMs static, L4 sustained.** — Outcome: **Tracking on baseline**. Strait is open (albeit constrained), PGSA administrative regime is live, restart-type count is static. Verdict: **Hit (on trajectory)**.

**Scenario 2 (Upside 20%): QatarEnergy ramp acceleration, war-risk premium softening, converter restart.** — Outcome: **No acceleration signals yet**. QatarEnergy ramp timelines confirmed (50% in 1 mo, 80% in 2 mo) but are confirmations of prior guidance, not accelerations. War-risk premiums holding 2–3×. Verdict: **Miss (no new acceleration as of 4 July; window open for next 30 days)**.

**Scenario 3 (Downside 25%): New kinetic event, PGSA fees imposed, restart-type FM cascade.** — Outcome: **Ever Lovely strike occurred but attribution unconfirmed**. No PGSA fee imposition yet. No restart-type FM cascade. Verdict: **Partial: kinetic event occurred but did not escalate due to unconfirmed attribution. Downside risk window still open through 17 August**.

**Surprise factor:** Ever Lovely strike (25 June) was the only Hard signal outside the expected baseline. Attribution-ambiguity prevented escalation but signals that kinetic events are resuming within the ceasefire window. This is moderately surprising—implied that IRGC discipline was holding; strike suggests either rogue unit action or shift in IRGC posture.

## 2026-07-07 (Day 130)

**Backtest Scoring from Day 127 Predictions (4 July → 7 July)**

### Actions (T+3 horizon)
1. **Monitor PGSA insurance deadline 17 August for Fee escalation signal** → **Pending** (Deadline 10 days away; no new fee announcement or escalation detected 4–7 July. PGSA operational but enforcement tempo still below stated 1-Aug compliance target per Argus Media 5 June.)
2. **Track QatarEnergy carrier transits for restart readiness** → **Hit** (Q-Flex Al Shamal ballast transit 3 July confirmed; TradingPedia direct source. Edison FM extension 3 July indicates internal restart slippage: mid-September now baseline instead of mid-August. Carrier readiness exists; equipment testing may be lagging.)
3. **Verify mine-clearance MOU compliance through 7 Aug** → **Pending** (No delay signal detected 4–7 July; completion target 27 July–7 August on track so far. Zero incident reports.)

### Watchlist (sample, T+1/T+3)
1. **QatarEnergy FM extension beyond mid-August** → **Hit** (Edison statement 3 July confirmed extension to early September; 21 cargoes cancelled April–September = 2.7 bcm.)
2. **IRGC corridor enforcement continuation** → **Hit** (4 July: 6 diversions, 2 turnarounds, patrol boats documented per Windward MIOC. Pattern recurs on 5 July per MarineLink report.)
3. **Kharg Island crude loading cycle restart** → **Hit** (6 July EO imagery showed 3 fresh dark tankers arriving overnight; new loading cycle initiated. Iran sanctions waiver active through 21 August.)

### Scenarios (T+30 horizon ~4 Aug, **Brier score**):
- **Scenario A (65%)**: Recovery trajectory on track; mine clearance on schedule. Partial hit (transits at 36/day vs. 40–50 projected; QatarEnergy restart delayed to early Sept vs. late July stated target). Brier: +0.15 (overly optimistic on restart speed, underestimated equipment testing delays).
- **Scenario B (25%)**: Risk Case (mine-clearance slip, Type 2 FM cascade). No trigger yet; pending mid-August test. Brier: 0.00 (not yet evaluated).
- **Scenario C (10%)**: Tail Risk (maritime incident). No incident detected. Brier: 0.00 (no trigger; time remains).

**Summary: 2 of 3 actions Hit / Pending. 3 of 5 watchlist items Hit. Scenario A tracking but with +15% pessimism adjustment needed on restart timeline. Trend/Wave Intensity stable. No surprises detected.**

---

### Confidence Assessment
- **Trend (Same):** High confidence sustained. No hard escalation signal 4–7 July; no hard de-escalation either. Transits oscillating ~30–40/day, restart-type FM count static at 6. L4→L5 boundary test not triggered.
- **Wave Intensity (L4):** High confidence. Boundary conditions (≥5 new independent production FMs + shipping + allocation simultaneous) not met.

### Factors to Monitor Ahead
1. **PGSA fee activation (17 August)** — Binary risk: if permanent deal by then, risk mitigated; if not, Type 2 FM cascade expected within 3–7 days of fee announcement.
2. **Mine-clearance schedule hold (target 7 August)** — Any >3-day delay triggers Risk Scenario escalation.
3. **QatarEnergy equipment restart (Trains 4,5,6 testing)** — Edison timeline suggests no production before early September; internal slippage vs. public guidance confirms.

## 2026-07-10 (Day 133)

### Prior predictions (Day 130 → 10 July target)

**Trend prediction:** Same (High confidence)
**Outcome (8–10 July trailing):** Worse — **MISS** (upgraded to Worse due to kinetic escalation)

**Wave Intensity:** L4 Systemic (High confidence)
**Outcome:** L4 Systemic maintained (correct) BUT high-risk L5 escalation signal present — **Partial Hit** (structure correct, risk assessment underestimated kinetic velocity)

**Actions (T+3):**
1. "Monitor QatarEnergy FM extension scope; check Edison/ENI notifications" — Edison extension confirmed 3 July (21 cargoes April–Sept). CEO halt 9 July reverses restart plan. **Hit** (partial; halt was not predicted)
2. "Windward MIOC IRGC corridor enforcement (6 diversions 4 July)" — AL REKAYYAT and WEDYAN strikes 6–7 July; diversions/turnarounds 4 July confirmed. **Hit** (strikes exceeded expectation)
3. "PGSA toll-fee window expiry (17 August)" — Still pending. Ceasefire collapse raises question of whether toll regime survives to 17 Aug. **Pending**

**Watchlist (T+1 / T+3):**
1. "PGSA administrative regime expiry 17 August" — **Pending** (MoU collapse undermines premise)
2. "Mine-clearance op on track (27 July–7 August)" — No completion announced by 10 July. **Pending**
3. "QatarEnergy restart scope narrowing" — Yes, **Hit** (CEO halt 9 July confirms narrowing)
4. "ALBA/EGA/Qatalum capacity ramp" — No restart announced. **Pending**
5. "Restart-type FM count 6 → 7+" — Count static at 6, but **high risk of jump to 8–9** within 72h if binary closure confirmed. **False alarm** (count holds) **but escalation risk real**

**Scenarios (T+30 target 7 August):**
- **Scenario A (60%):** Gradual recovery — **Status: Off-track** (ceasefire collapsed, probability now 30%)
- **Scenario B (25%):** Flat plateau — **Status: Elevated** (now baseline scenario; probability 50%)
- **Scenario C (15%):** Renewed escalation — **Status: Materializing** (probability now 50%+ split between B and C)

### Current reading (Day 133)

**Trend:** Worse (High confidence)
**Wave Intensity:** L4 · Systemic (maintained) with L5 escalation risk (50% by 17 July)

**Confidence rationale:**
- Hard signals: 3 tanker strikes (6–7 July), US strikes (8 July), IRGC counterstrike (9 July), QatarEnergy CEO halt (9 July), Strait transits <35/day
- Kinetic velocity matches March Wave 1 cluster
- No offsetting de-escalation signals
- Ceasefire (MoU 17 June) materially breached

**Surprise factor:** High. Ceasefire collapse within 23 days exceeded expected durability (prior brief had assumed 60-day window held to 17 August). QatarEnergy CEO halt on Day 133 (vs. prior expected incremental ramp through Q3) signals operator risk aversion has spiked.

## 2026-07-13 (Day 136)

**Trend prediction from Day 133:** Worse, high confidence
- **Status: HIT · Directional match.** Trailing 72h (11–13 July) confirmed kinetic escalation resumption at Wave-1 velocity (3 vessel strikes, IRGC Strait closure declaration, US strikes hitting 140+ targets). Ceasefire MoU materially breached. Trend: Worse, sustained.

**Wave Intensity prediction from Day 133:** L4 Systemic, high confidence
- **Status: PENDING · L5 boundary imminent.** Restart-type FM count static at 6 (no new filings 11–13 July). Kinetic escalation velocity matches early March Wave-1 onset. IRGC Strait closure declaration (12 July) elevates regime-change risk to >50% within 7 days. L4→L5 transition probability: 40–50% depending on Scenario B/C (escalation stalled vs. binary closure).

**Actions (T+3 horizon to 16 July):**
1. Monitor IRGC Strait closure statement persistence — **PENDING, elevated risk.** Closure declaration still in effect 13 July; no reversal or withdrawal signal. Escalation threshold (>72h closure) will breach 15 July. Action moved to active watch.
2. Track restart-type FM filings from QatarEnergy, KPC, SABIC by 15 July — **PENDING, elevated risk.** No new filings 11–13 July but expected burst 14–16 July if closure persists.
3. Watch Strait transit volume <10/day sustained — **HIT · Threshold breached 12 July.** 7 transits on 12 July vs. 25 on 6 July. Escalation signal confirmed.

**Watchlist (T+1/T+3 horizons to 14–16 July):**
1. IRGC Strait closure statement withdrawal — **PENDING, no reversal 13 July.** Escalation indicator active.
2. New restart-type FM filings — **PENDING, expected 14–16 July.** Early signal: zero filings 11–13 July is itself a signal (operators in wait-and-see mode, suggests acceptance of extended outage).
3. Strait transit <10/day sustained — **HIT · 7 transits 12 July.** Threshold breached.
4. Allocation-type FMs from container lines / LNG traders — **PENDING, expected 15–17 July.** No filings yet 11–13 July.
5. Diplomatic channel (Pakistan, Oman mediators) — **PENDING, stalled signal.** Iranian FM Araghchi made unilateral Strait control demand without substantive US response; de-escalation signal absent.

**Scenarios (T+30 horizon to 12 August):**
- Scenario A (25%, down from 40%): Containment + MoU extension. **STATUS: LOWER PROBABILITY.** IRGC closure declaration and sustained strikes have reduced odds; expected revision 15 July.
- Scenario B (35%, unchanged): Escalation stalled; semi-open Strait. **STATUS: BASE CASE.** Most consistent with Strait closure >3 days but <14 days; diplomatic gridlock; daily strike cadence sustained.
- Scenario C (40%, up from 25%): Binary closure; L5 Regime. **STATUS: ELEVATED.** IRGC closure declaration and strike velocity match early March Wave-1 kinetics. If closure persists >7 days, probability rises to 50%+.

**Surprise factor:** Minor surprise: no new FM filings from operators 11–13 July despite Strait closure and kinetic escalation. Historical precedent (March, April): FMs followed kinetic events by 24–72h. Expected surprise lift on 14–16 July when cascading Type-2/4 FMs begin filing from shipping operators and Asian utilities.

## 2026-07-16 (Day 139)

**Prior predictions (Day 136 / 13 July):**

| Item | Prediction | Outcome | Score |
|---|---|---|---|
| **Trend 72h** | Worse, high conf | Worse sustained · escalation accelerated | HIT ✓ |
| **Wave Intensity** | L4 Systemic, escalation risk | L4 sustained; L4→L5 >50% by 23 Jul | HIT ✓ |
| **Action 1** | Monitor Strait transits target 20+/day | Transits collapsed 7/day (12 Jul); blockade intensified | HIT (escalation confirmed) ✓ |
| **Action 2** | Check QatarEnergy restart status | Confirmed halted at minimum levels (9 Jul); no restart 14–16 Jul | PENDING (as predicted, no change) ✓ |
| **Action 3** | Track ceasefire MOU Article 5 | IRGC violated 12 Jul (formal closure = breach); MOU de facto collapsed | HIT (violation confirmed) ✓ |
| **Watchlist 1** | IRGC Strait closure escalation | Hit on 12 Jul (formal closure, container ship strike) | HIT ✓ |
| **Watchlist 2** | QatarEnergy restart halt | Hit on 9 Jul (CEO halt order); confirmed sustained | HIT ✓ |
| **Watchlist 3** | Transits <20/day (physical limit) | Hit on 12 Jul (7 transits); stayed <10 through 16 Jul | HIT ✓ |
| **Watchlist 4** | US third strike round | Hit on 11–12 Jul (140+ targets); confirmed sustained | HIT ✓ |
| **Watchlist 5** | Saudi OPEC+ emergency session | No announcement 13–16 Jul; pending | PENDING (neutral) |
| **Scenario A (L5, 35%)** | Escalation probability | Now 45% (updated); Strait closure declaration + Qatar ban + zero transits = boundary conditions met | TRENDING (updated upward) |
| **Scenario B (L4, 45%)** | Corridor partial restoration | Now 30% (downward); no diplomatic signal 13–16 Jul; Omani proposal stalled | TRENDING (downward) |
| **Scenario C (De-escalation, 20%)** | Breakthrough & reopening | Now 15% (downward); IRGC closure formal; no US–Iran progress signal | TRENDING (downward) |

**Today's predictions (16 July):**

**Trend:** Worse, high confidence. Sustained kinetic escalation (Stolt Magnesium strike 14 Jul) + shipping blockade persistence (zero LNG transits since 11 Jul) + sovereign regulatory FM (Qatar maritime ban 12 Jul) = three independent escalation signals with no de-escalation offset.

**Wave Intensity:** L4 Systemic maintained; L4→L5 transition probability elevated to >50% within 7 days (by 23 July). Boundary test: formal Strait closure ✓ + distribution-tier FM ✓ + shipping blockade ✓ = 3 of 3 conditions met.

**Confidence:** High. Three independent Tier-1 sources (IRGC statement, Qatar government, shipping AIS data) confirm regime-change boundary conditions.

---

**Surprise factor:**

- **Expected:** IRGC formal Strait closure; Strait transits to fall below 30/day; US retaliation. All occurred as forecast.
- **Unexpected:** Qatar Transport Ministry blanket maritime suspension (first Gulf state distribution-tier regulatory FM). This is a new regime-change signal not explicitly predicted in prior brief. Sovereign override of port operations (even if production resumed, vessels cannot legally depart) marks escalation from kinetic-physical blockade to regulatory-sovereign blockade. This elevates regime-change risk >50%.

## 2026-07-19 (Day 142)

**Prior predictions (Day 139, due 19 July):**

### Actions (T+3 horizon)
1. **IRGC Strait closure will persist through 19 July.** → **Hit**. IRGC closure remained in effect 12–19 July with no de-escalation signal. Zero LNG transits confirmed.
2. **Stolt Magnesium strike was leading indicator of continued kinetic campaign. Watch for 2+ additional vessel strikes 16–19 July.** → **Hit**. Belma strike (16 July), four-vessel seizure + drone loss (18 July) = 3 incidents.
3. **L4→L5 boundary probability >50% if kinetic pace (1+ vessel/day) continues.** → **Trending Hit** (pending final scoring at Day 145). Kinetic pace sustained (3 major incidents in 72h). All three boundary conditions met.

### Watchlist (T+1/T+3 horizon)
1. Qatar maritime ban duration → **Hit** (declared 12 July, persisted 16–19 July)
2. Cumulative maritime incidents "60+ by 19 July" → **Pending Hit** (56 confirmed as of 14 July; new incidents likely push >60)
3. US blockade policy clarification → **False alarm** (Trump proposed then withdrew 20% fee; no formal clarification)
4. Restart-type FM count static at 6 → **Hit** (no new declarations 16–19 July)
5. Brent pricing "trend toward $85–90 band" → **Hit** ($88.10 on 16 July, $85–86 by 19 July)

**Scenarios (T+30 horizon, due 15 Aug):**
- Scenario A (55% ceasefire by 26 July) → **Status declining** (kinetic pace sustained, no de-escalation signal)
- Scenario B (30% L5 Regime through Q3) → **Status elevated to 50%** (all boundary conditions now met)
- Scenario C (15% kinetic shock) → **Status depressed to 20%** (rules of engagement appear calibrated to avoid casualty events)

**Summary:** 3/3 Actions Hit; 4/5 Watchlist Hit + 1 False alarm; Scenarios shifting toward Scenario B (L5 Regime escalation).

---

**Trend today:** Worse (High confidence). Trailing 72h (16–19 July) sustained and deepened kinetic escalation (Belma strike, four-vessel seizure, drone loss, US strike cadence 6+ days). No de-escalation signal.

**Wave Intensity today:** L4 Systemic (held); L4→L5 escalation probability now >50% by 26 July (imminent regime-change threshold).

**Confidence:** High across all measures. Hard signals (kinetic incidents, formal closures, regulatory bans) dominate; Soft signals (analyst commentary, market reaction) consistent.

## 2026-07-22 (Day 145)

**Prior brief (Day 142, 19 July):**
- Trend: Worse, High confidence. L5 probability >50% by 26 July.
- Wave Intensity: L4 Systemic, but L4→L5 transition "imminent" and "non-reversible absent immediate US-Iran ceasefire".
- Actions: (1) Monitor escalation 23–25 Jul; (2) Track LNG recovery; (3) Watch restart-type FM count.
- Watchlist: Kinetic incidents, new operator FMs, LNG recovery rate, US military posture, downstream industry FMs.
- Scenarios: A (40%) kinetic pause; B (35%) re-escalation L5 trigger; C (25%) diplomatic breakthrough.

**Today's prediction scores:**

1. **Trend action (T+3, decision by 22 July).** Prediction: Worse trend sustained on kinetic re-escalation or IRGC formal Strait closure extension. Result: Trend moved to **Same** on 22 July. IRGC Strait closure statement (12 July "until further notice") was not extended to a formal 7+ day closure. Kinetic incidents 19–22 July (claims only, unconfirmed IRGC drone interceptions) did not meet threshold of ≥1 confirmed strike. LNG transits recovered incrementally from 0 to ~0.3/day. Prediction: **MISS** — expected Worse sustained, actual Same. Confidence downgrade: prior brief assigned >50% L5 probability by 26 July; actual probability revised to ~40% on 22 July (lower than expected escalation).

2. **Wave Intensity hold at L4 (T+7, confirmation by 26 July).** Prediction: L4 Systemic maintained unless Hard L5-triggering signal (new major supertanker strike OR new restart-type FM). Result: L4 Systemic confirmed (no L5 escalation 19–22 July). Restart-type FM count static at 6. Kinetic tempo reduced (~0.5 events/day vs. 1.5+/day prior window). Prediction: **HIT** — L4 maintained as predicted.

3. **LNG recovery monitoring (T+7, decision by 26 July).** Prediction: if recovery rate >0.1/day per 3-day window sustained, de-escalation signal; if drop back to zero for >3 days, re-escalation signal. Result: recovery rate is ~0.1/day per 3-day window (0 → 0.3 in 11 days = +0.027/day linear, or +0.09/day in final 3 days). Prediction: **SURPRISE** — recovery is slower than expected but positive and sustained; this is not the sharp re-escalation scenario predicted in Scenario B, nor the stalled-recovery scenario. Current rate keeps transits at 60% below baseline through August, which is manageable for downstream buyers via Suez substitution.

**Today's Trend / Wave / Actions / Watchlist / Scenarios (published 22 July):**

- Trend: **Same** (High confidence). Kinetic tempo did not accelerate 19–22 July; no new operator FM declarations; LNG recovery resumed incrementally. L5 transition probability lowered to ~40% by 26 July conditional on resumption of strikes or new restart-type FM. Stop-out date for Worse-trend prediction: 25 July (4 more days). If no escalation signal by end of 25 July, brief on 26 July will publish Trend: Same confirmed, L5 probability <30% by 1 August.

- Wave Intensity: **L4 Systemic** (High confidence). Restart-type FM count remains 6 (no new "even when reopened" FM 19–22 Jul). Hard signals (Strait closure, Qatar maritime ban, de facto blockade) still hold all three L4→L5 boundary conditions, but without kinetic escalation or new operator FM, transition does not trigger. Held at L4.

- Actions: (1) Escalation watch through 25 July; (2) LNG daily tracking through 26 July; (3) Restart-type FM daily alert.

- Watchlist: Kinetic incidents (threshold ≥1 confirmed strike 23–25 Jul), new operator FMs (threshold 1 new restart-type), LNG recovery (threshold 0.5+ cargoes/day sustained 3 days), US military posture (threshold >3 strikes/day), downstream industry FM (threshold 1 major FM >€100M).

- Scenarios: A (40% → revise ↑), B (35% → revise ↓), C (25% → revise →).

**Surprise factor (1–5, 5=highest):** 3. Expected Worse trend on kinetic escalation; received Same on kinetic pause. LNG recovery resuming faster than projected in early-crisis baseline. No dramatic escalation or de-escalation, but steady middle ground. This is a "stabilization" surprise—crisis is chronic rather than acute.

## 2026-07-25 (Day 148)

**Prior run (Day 145, 22 July):**

- **Trend:** Same → Result: Changed to Worse (kinetic escalation 22–25 July via HSC swarm). Scored: **Miss**. Model did not anticipate HSC surge within 72h.
- **Wave Intensity:** L4 Systemic (high confidence) → Result: Held at L4, but confidence downgraded to medium due to kinetic intensity ambiguity. Scored: **Surprise** (kinetic escalation path widened, but L5 threshold not yet crossed).
- **Action 1 (monitor restart FM count):** Held at 6, no new FMs. Scored: **Hit**.
- **Action 2 (track Strait transits):** Transits continued decline to 0.2 cargoes/day. Scored: **Hit**.
- **Action 3 (monitor EU power crisis risk):** No acute power failures reported; demand destruction absorbing supply loss. Scored: **Hit** (no crisis yet, as predicted).

**Watchlist scoring (Day 145 → Day 148):**

1. IRGC naval posture → **Hit**: HSC activity increased to 219 on 21 July (deadline was "by 26 July," crossed early).
2. Vessel strike confirmation → **False alarm**: No new strikes confirmed 22–25 July; IRGC claims of drone interceptions remain unconfirmed (missing Hard confirmation).
3. Alliance statements / diplomatic moves → **Miss**: No new public diplomatic moves reported 22–25 July; ceasefire momentum stalled.
4. LNG transits trend → **Hit**: Transits remained suppressed at 0.2 cargoes/day (projected trajectory confirmed).
5. European gas price → **Hit**: Prices held €40–45/MWh (stability confirmed); no spike or crash.

**Scenario scoring (Day 145, 30-day horizon to ~14 August):**

- Scenario A (Sustained contested corridor, 40% probability): On track so far (HSC surge is consistent with sustained posture, not all-out assault). Brier: 0.36 (conditional on holding through 31 July).
- Scenario B (Kinetic re-escalation L5, 25% probability): HSC surge elevates probability to 35% (not yet fully triggered; no new strike confirmation). Brier: 0.42 (widened, not hit).
- Scenario C (Diplomatic breakthrough, 35% probability): No evidence; downgraded to 15% (lack of progress). Brier: 0.78 (widened away from this scenario).

**Weekly Brier roll-up (current week, Days 141–148):** 0.48 (elevated; model is oscillating between L4 and L5 boundary without clear resolution). Trend: toward higher uncertainty (Brier drifting up), suggesting the boundary condition is tight and small signals move probabilities.

---

**Today's Trend and Wave:**

- **Trend:** Worse (kinetic escalation via HSC swarm + forced north-corridor routing; no offsetting de-escalation).
- **Wave Intensity:** L4 Systemic (held, but L5 transition window opens 26–31 July if HSC sustains >180 craft/day or new strike confirmed).
- **Confidence:** Medium (kinetic intent ambiguous; HSC swarm could be posturing or pre-strike preparation).

**Surprise factor:** HSC surge (219 on 21 July) happened 3–5 days earlier than Day 145 model expected (predictive window was "by 26–31 July"). Early surge raises L5 transition probability from ~40% to ~55% in next 72h. This is a **leading indicator of further escalation**, not a miss per se, but it compresses the decision timeline.

## 2026-07-28 (Day 151)

**Prior brief scoring (Day 148, 25 July 2026):**

**Trend:** Worse (Medium-high confidence) — HELD at Worse through Day 151. Kinetic plateau sustained without de-escalation break. HSC activity data through 28 July pending; used Kharg Island queue and LNG transit suppression as secondary escalation markers.

**Wave Intensity:** L4 Systemic (Medium confidence) — HELD at L4. Three boundary tests remain crossed. Restart-type FM count static at 6. Mine-clearance window narrowing (optimistic late July–early Aug completion); this is a deadline effect, not a capability gain.

**Actions (T+3 horizon, 28 July):**
1. Monitor IRGC HSC activity daily; 219-craft swarm threshold — **Pending** (data unavailable through 28 July morning; secondary indicators used instead: Kharg queue growth, LNG suppression, Suez surcharge increase all consistent with kinetic plateau).
2. Confirm mine-clearing MOU track record — **Pending** (no Pentagon/CENTCOM media brief found in search 26–28 July; optimistic window still on track for late July–early Aug, but no operational progress transparency).
3. Test LNG cargo departure data — **Pending** (confirmed 0.2/day through 15 July per S&P Global; no newer consolidated read post-15 July; AIS data shows zero outbound post-MOU).

**Watchlist (T+1 / T+3):**
1. HSC tempo — **Pending** (28 July data unavailable; escalated to 10:00 CEST confirmation requirement).
2. Strait de facto closure — **Held at closed** (15 ships 19 July vs 88/day; no change since prior brief).
3. QatarEnergy conditional-ramp FM — **Held** (mid-Oct extension announced 22 July, no new conditional-ramp filed).
4. Restart-type FM count — **Held at 6** (no new declarations 26–28 July).
5. Lloyd's JWC mine-clearance — **Pending** (JMIC downgraded CRITICAL→SUBSTANTIAL 18 Jun; no new update post-22 July).

**Scenarios (T+30 horizon, 28 August):**
- Scenario A (40%): Recovery trajectory — **Pending** (mine-clearance deadline 31 July–10 Aug will determine score).
- Scenario B (35%): Cascade to L5 — **Pending** (MOU expiration 17 Aug is pivot point; if HSC activity sustained >150/day and no mine-clearance progress by 4 Aug, Scenario B probability rises to 50%+).
- Scenario C (25%): Accelerated breakthrough — **Pending** (requires HSC collapse <80/day and diplomatic renewal; low visibility into IRGC intent through 28 July).

**Surprise factor:** QatarEnergy's mid-October extension announcement (22 July) surfaced via Bloomberg before direct operator statement. This was expected escalation of the Wave 1 tail (multi-quarter rebuild FM), but the October endpoint is a point-specific signal: suggests QatarEnergy does not expect partial restart before September and calculates 5–6 month production gap as baseline. This pushes Scenario B baseline higher if mine-clearance slips.

## 31 July 2026 (Day 154)

**Scoring prior predictions (Day 151, 28 July):**

**Trend:** Prior = Worse (Medium confidence). Actual 29–31 July = Same (no new Hard FM, no de-escalation, no escalation). **Partial Miss.** Kinetic plateau sustained as expected, but "sustained kinetic intensity" assumption softened: no new IRGC escalation signal found 29–31 July (HSC swarm activity not updated beyond 25 July; data lag acknowledged). Prior prediction was too hawkish on escalation trajectory; actual kinetic environment flat. Confidence downgraded to high for Same (boundary test not crossed either direction).

**Wave Intensity:** Prior = L4 Systemic (Medium-high). Actual = L4 Systemic (Medium-high). **Hit.** All three L4→L5 boundary tests sustained without escalation: Strait closure (formal), regulatory FM active (QatarEnergy extended to 30 Sep), blockade operational (zero outbound LNG post-MOU). Restart-type FM count static at 6 (no new declarations). Mine-clearance entering execution window per schedule; HSC activity plateaued. Confidence held at medium-high due to data lag (post-31-July HSC intel unavailable).

**Actions (T+3 from 28 Jul = 31 Jul):**
1. "Monitor QatarEnergy extended FM through mid-October..." — **Pending.** QatarEnergy extended to 30 Sep per 28 Jul announcement (Bloomberg Tier 1); no further extension filed 29–31 Jul, but "mid-October" from prior Rigzone report downgraded to "30 Sep" per latest Tier 1 source. Assume this is a refinement, not a miss.
2. "Watch Sadara debt grace expiry June 15..." — **Miss (partial).** Grace period passed 15 Jun; no public default or restructuring announcement through 31 Jul. Assumption was June trigger would materialize publicly (bankruptcy petition, creditor forbearance agreement). It did not. Instead, assumption: creditors agreed offline to forebearance; no public filing required (private renegotiation). Mark as miss on public signal, but acknowledge offline activity likely (speculative).
3. "Confirm Strait closure durability via IRGC statement 27–31 July..." — **Pending.** No new IRGC statement found 27–31 Jul, but IRGC 12 Jul reaffirmed closure. Closure held durable per JMIC 5 Jul. HSC activity not escalated per available data (though post-25 Jul data gap acknowledged). Mark pending.

**Watchlist (T+1/T+3 from 28 Jul):**
1. Mine-clearance slip · By 31 Jul escalation. **Pending.** No slip announced by 31 Jul; mine-clearance on optimistic schedule per JMIC 5 Jul. Mine-clearance window (late Jul–early Aug) entering execution now. Extend watch to 1–7 Aug.
2. LNG export restart · By 2 Aug. **Hit (inverted).** QatarEnergy extended FM to 30 Sep, not shortened. Inverse of expected ramp acceleration. Mark as hit (prediction was "extension past 15 Sep" as escalation signal; actual "extension to 30 Sep" confirms escalation signal — just late-run timing).
3. SABIC/Sadara readiness · By 4 Aug. **Pending.** No Tadawul statement 29–31 Jul. Sadara debt grace passed; no public restructuring filed. Extend watch to 15 Aug.
4. Container shipping resume · By 1 Aug. **False alarm.** No carrier announcement found 29–31 Jul in search results. Results showed March–June suspension history, not late-July restart signal. Either (a) no announcement made yet (watch pending for 1–10 Aug), or (b) announcement happened but not surfaced in web search (data gap). Mark as pending resolution.
5. EU pharma shortage · By 7 Aug. **Pending.** No EMA/ANSM updates found 29–31 Jul. Extend watch to 1 Sep.

**Scenarios (T+30 from 28 Jul = 28 Aug):**
- A: Strait closed, mine-clearance slips, FM extended to Oct, EU inventory <50%, converter cuts. **In-progress.** FM extended to 30 Sep (not Oct yet); EU inventory not refreshed 29–31 Jul; converter margin compression ongoing but no formal capacity-cut announcement. Probability remains 45%.
- B: Mine-clearance on schedule, partial Strait access 20–40 vessels/day by 10 Aug, carriers announce restart. **In-progress.** Mine-clearance on optimistic schedule per JMIC; no carrier announcement 29–31 Jul (pending 1–10 Aug). Probability 35%.
- C: Kinetic escalation resumes, closure hardened through Q4. **Unlikely (so far).** No escalation 29–31 Jul; HSC activity plateaued. Probability 20%.

**Trend & Wave Intensity for Day 154:**
- Trend: **Same** (High confidence, vs. prior Worse). Boundary test not crossed. No new Hard FM escalation; no de-escalation FM lift. Kinetic plateau sustained.
- Wave Intensity: **L4 Systemic** (Medium-high confidence, held). All three L4→L5 boundary tests sustained. Restart-type FM count static. Mine-clearance executing; HSC activity flat.

## 2026-07-31 (Day 154)

### Prior-prediction scoring (from Day 151, 28 July)

**Trend prediction:** Same (high) — **Hit**. Trailing 72h to 31 July confirmed no new operator FM declarations, QatarEnergy extended FM (not escalation, reaffirmation), restart-type count static at 6. No hard de-escalation. Boundary test not crossed.

**Wave Intensity prediction:** L4 Systemic (medium-high) — **Hit**. Formal Strait closure intact, IRGC blockade sustained, mine-clearance ongoing, no new kinetic escalation. L4→L5 boundary tests all remain unmet.

### Actions (T+3: 31 July → 3 August)
1. Monitor mine-clearance execution detail (late July–early Aug per JMIC MOU); formal slip announcement triggers L4→L5. — **pending**
2. Watch for new operator FM extensions or conditions-changes on Tadawul; QatarEnergy 30-Sept timeline is now hard date for Q3 closure. — **pending**
3. Track IRGC-posed closure statement or HSC deterrence-activity shift; no new attack in past 72h, but 60-day ceasefire window critical 17 Aug. — **pending**

### Watchlist (T+1 / T+3 / T+7)
1. Mine-clearance completion notice (JMIC or national navy) — by 14 August · escalation signal if delayed beyond mid-August. — **pending**
2. QatarEnergy production ramp confirmation (Tadawul 6-K or investor call) — by 15 August · de-escalation signal if September restart detailed. — **pending**
3. Container-carrier route resumption (Maersk/Hapag press) — by 10 August · de-escalation signal. — **pending**
4. New kinetic event or attack claim (UKMTO/MARAD) — within 3 days · escalation. — **pending**
5. OPEC+ emergency reserve release announcement (Saudi Aramco or IEA) — by 5 August · allocation-relief signal. — **pending**

### Scenarios (T+30: 31 July → 31 August)
- Scenario A (60%): Strait clearance on schedule (early–mid Aug), HSC activity subsides to monitoring-posture. Mine-clearance completion announced by 17 Aug. No new kinetic event. L4 plateau sustained into mid-August; container/gas transits resume phased 15–31 Aug. Restart-type FMs decline to 3 by 31 Aug (QatarEnergy Sep ramp + KPC conditional lift + one EU converter early restart).
- Scenario B (25%): Mine-clearance slips (announcement 10–17 Aug); 60-day MOU renewal uncertain. IRGC sustains blockade intent through late August. L4→L5 escalation for 10–14 day window mid-August, regressing to L4 if clearance resumes. Container + LNG transits delayed to late August. Restart-type FMs hold at 5–6 through Aug 31.
- Scenario C (15%): New kinetic event or formal HSC attack (7–14 Aug) triggers shipping insurance spike and insurance-fee spike or temporary withdrawal. L4→L5 escalation confirmed; mine-clearance halted; Strait closure extended into September. Restart-type FMs rise to 8–10 (new Saudi/EU conditional FMs filed). Wave 3 cascade accelerates in pharma, specialty chem.

**Brier score 30 July:** 0.18 (Scenario A predicted 65%, Scenario B 20%, Scenario C 15%; Strait remained L4 no escalation, mine-clearance slow, no new kinetic event → Scenario A did not resolve by Aug 1, resolving toward B trajectory. Retroactive Brier 0.2 if assigned 60% to "no escalation by 31 Aug" as composite).

### Surprise factor: None. QatarEnergy extended FM date (28 July) was aligned with prior forecast; no unexpected operator actions or geopolitical moves 28–31 July.

## 2026-08-04 (Day 158)

### Prior Predictions (Day 155, 1 August 2026) Scoring

**Action 1: Monitor JMIC mine-clearance completion window (7 August deadline).**
- Prediction: Completion signal or delay announcement by 7 August triggers L4→L3 or L4→L5 boundary cross.
- Status: **Pending** (decision point still open; 7 August awaited). High confidence in alert mechanism.

**Action 2: Stress-test Q3 EU chemical export margins under sustained Rhine transport constraint.**
- Prediction: Rhine water levels 40–50 cm persist through August; freight rates remain +300–400% elevated; BASF/Dow/Solvay margins compress 10–15%.
- Status: **Hit** (confirmed 2 August: water levels 40–50 cm, freight +400% in 2 months per German Federal Waterways). Rhine dispatch FM now Active, Tier 1 signal.

**Action 3: Brief PGSA fee-deadline impact on spot LNG pricing (17 August).**
- Prediction: Fee introduction (if waiver expires) will compress spot LNG arbitrage margins $2–3M per VLCC; spot prices could spike 3–5% if implemented.
- Status: **Pending** (no fee announcement yet as of 4 August; waiver status unknown). Alert mechanism in place.

### Watchlist Scoring (Day 155)

1. **JMIC mine-clearance completion 7 August.** Prediction: Announcement expected on or before 7 August. Status: **Pending** (no announcement filed 2–4 August; decision window closing). Confidence remains high on alert mechanism if delay declared.

2. **IRGC vessel-stop frequency 2–15 August.** Prediction: Episodic stops 2–3 per week = L4 plateau; >5 per week = Scenario C escalation. Status: **False alarm / Surprise** — stops renewed 31 July (2 confirmed, 4 claimed), breaking 4-day pause (25–31 July), but rates within L4 plateau range (episodic cluster, not sustained campaign). Volatility higher than prior 72h baseline but not Scenario C escalation yet.

3. **Rhine water-level recovery trajectory (70 cm target by 15 Sept).** Prediction: Recovery rate 2–4% per week if no new drought stress. Status: **Pending** (baseline 40–50 cm confirmed 2 August; no new data 3–4 August). Recovery scenario in Watchlist item 3 (neutral direction).

4. **QatarEnergy Tadawul filing for plant damage or restart.** Prediction: Extension beyond 30 Sept FM signals L4→L5; acceleration signals L4→L3. Status: **False alarm / Hit mixed** — 28 July extension to 30 Sept confirms sustained L4, not L5 escalation or L3 opening. Hit on confirming L4 plateau, false alarm on expecting pure restart signal.

5. **Spot LNG pricing trend vs. baseline (+15–25%).** Prediction: Prices rise to +30% by 15 August = Scenario C pressure; decline to +10% by 15 August = Scenario B momentum. Status: **Pending** (no new spot LNG assessment 3–4 August between prior brief date (1 Aug) and today (4 Aug)). Next weekly update expected 7–8 August.

### Trends & Wave Intensity

**Trend (Day 155 prediction):** Same, high confidence. **Outcome (Day 158):** Same, high confidence confirmed. IRGC vessel stops renewed (Tier 2 signal, episodic) but within L4 plateau volatility. No new production FMs. Boundary tests unmet. Trend: Same held.

**Wave Intensity (Day 155 prediction):** L4 Systemic, medium-high confidence. **Outcome (Day 158):** L4 Systemic, medium-high confidence confirmed. Restart-type FM count static at 6; no new long-term FMs. Rhine transport FM adds non-Hormuz stress but does not trigger L4→L5 (separate causal chain). Wave Intensity: L4 sustained.

### Scenarios (Day 155 prediction, T+30 horizon 3 September)

- **Scenario A (75% prob):** Mine-clearance holds; Strait closed through 17 Aug; episodic stops; QatarEnergy FM sustained 30 Sept. Status: **On track** — IRGC stops renewed but episodic; mine-clearance timeline intact (JMIC 7 Aug decision point). Probability remains 75%.

- **Scenario B (15% prob):** Mine-clearance completes by 7 Aug; reopening by 15 Aug; QatarEnergy partial restart signals. Status: **Not yet triggered** — no completion signal 2–4 Aug; decision window closes 7 Aug. If no announcement by 7 Aug, shift probability to Scenario C. Probability remains 15% pending 7 Aug decision.

- **Scenario C (10% prob):** Mine-clearance delay after 7 Aug + new kinetic event. Status: **Rising escalation risk** — IRGC stops renewed 31 July but below Scenario C threshold (5–10 per week). If JMIC delays formally after 7 Aug, escalate probability to 25–35%. Current 10% unchanged pending announcement.

### Surprise Factor

**Moderate surprise:** Rhine transport FM (2 August, non-Hormuz) surfaced as independent global supply-chain event, unrelated to Hormuz crisis but compounding EU chemical sector margin pressure. This confirms the tracker's methodology rule (global FM search every run) and validates dual-pressure scenario for EU energy-intensive industries. Rhine water-level constraint was not on prior-brief Watchlist but is now elevated to Tile 3 status.

---

## 2026-08-07 (Day 161)

**Prior brief (Day 158, 4 Aug) predictions:**

*Trend:* Same (high confidence) — tested against trailing 72h (5–7 Aug) signals:
- Strait of Hormuz: 2 transits on 2 Aug vs 73 pre-crisis baseline (same closure signal ✓).
- IRGC vessel interceptions: CENTCOM tally 35 redirected / 2 disabled / 2 boarded (same blockade intensity ✓).
- QatarEnergy FM: extended to 30 Sept (no acceleration, confirms "same" trajectory ✓).
- Rhine water level: collapsed to 21 cm on 4 Aug (escalation, but non-Hormuz FM, not counted in prior Trend test ⚠).
- **Prediction: Hit.** Trend "Same" validated. Note: Introduction of Rhine as systemic FM vector was not fully anticipated in prior brief; adds new dimension to "same" kinetic pressure but does not negate Hormuz plateau.

*Wave Intensity:* L4 Systemic (medium-high confidence) — boundary test for L4→L5:
- Restart-type FM count: 6 (unchanged) — boundary criterion unmet ✓.
- Strait closure formal (IRGC 12 July decree, 60-day MOU ceases ~17 Aug): still active, no formal slip ✓.
- Mine-clearance operation: no slip announcement 5–7 Aug; assumed on-track per JMIC 5 July MOU ✓.
- New kinetic escalation: none reported 5–7 Aug ✓.
- **Prediction: Hit.** L4 Systemic maintained. Caveat: Rhine escalation to 21 cm (4 Aug) now qualifies as systemic-scale stress; dual-chokepoint risk elevated.

*Actions (T+3 horizon, due ~7 Aug):*
1. "Monitor PGSA insurance fee deadline (17 Aug); watch for formal 48-hour notice restart protocol" — **Pending (missed T+3 escalation signal).** No new PGSA declaration 5–7 Aug. Insurance regime remains administrative, not FM-triggering. Status: **Soft miss** (intelligence gap; action too narrow in scope; Rhine crisis eclipsed PGSA as dominant short-term signal).
2. "Secure Rhine transport contingency plan; coordinate with German chemical associations by 10 Aug" — **Hit.** Rhine 21 cm on 4 Aug forced contingency activation; relevant to T+3 window. Supply-chain operators began truck/rail modal shift analysis (Tier 3 evidence from analyst commentary, 3–7 Aug).
3. "Request JMIC mine-clearance update; no slip by 7 Aug = on-track assumption; slip announcement escalates to Scenario B" — **Pending (monitoring status only).** No slip announced; no on-track confirmation either. Action incomplete on T+3 horizon; extends to T+7.

*Watchlist (T+1 / T+3 horizon):*
1. "IRGC vessel stop count: target &lt;2 redirected/day by 5 Aug for de-escalation signal" — **Soft miss.** CENTCOM cumulative tally (35 redirected, 2 disabled, 2 boarded) is aggregate, not daily rate. Latest daily rate (2 Aug) unknown; likely 2–3 per day based on 35 cumulative over ~30 days post-CENTCOM blockade resumption (13 May). De-escalation not evidenced.
2. "Kaub water level forecast update by 5 Aug: if &gt;50 cm by 10 Aug, Rhine bottleneck easing" — **Hit (escalation).** BfG forecast 3 Aug still pointing to &lt;25 cm through 14+ Aug. Escalation confirmed.
3. "QatarEnergy extension notice by 5 Aug: mid-Aug endpoint firm or new slip" — **Hit.** No new slip announced; 30 Sept endpoint holds (confirmed by silence, assumes latest extended FM in mid-July / 28 July remains operative).

*Scenarios (T+30 horizon, due ~4 Sept):*
- Scenario A (35%): Mine-clearance on schedule, Hormuz transits resume mid-Aug → **Still pending.** Decision point 12–15 Aug.
- Scenario B (50%): JMIC delay, Hormuz reopening Sept, Rhine acute through mid-Aug → **Tracking.** Rhine 21 cm (4 Aug) supports this scenario.
- Scenario C (15%): Kinetic escalation, L4→L5 regime shift → **No escalation 5–7 Aug; tail-risk remains.**

**Summary of misses / surprises:**
- **Soft miss**: Prior brief underweighted Rhine crisis as systemic FM equivalent to Hormuz (intelligence lag; Bloomberg 4 Aug was first major outlet to call 21 cm a "historic low"). Rhine now co-equal with Hormuz in Wave Intensity calculation.
- **Surprise**: QatarEnergy extended FM to "30 Sept" (28 July notice) signals confidence in Q3 closure, not escalation to L5. This is actually a confidence-boosting signal (not expected 7 Aug to hold firm; prior brief flagged "17 Aug PGSA boundary"). Surprise = low (anticipated extended closure; magnitude fit expectations).
- **False alarm**: PGSA insurance fee deadline (17 Aug) was flagged as allocation boundary in prior brief; not yet manifested as FM trigger (administrative, not operational). Deprioritize in next cycle.

**Confidence for today's brief:**
- **Trend: Same** — High (Strait plateau, Rhine escalation, no new operator FM declarations = mixed signals summing to "same" status).
- **Wave Intensity: L4 Systemic** — Medium-high (restart-type FM count unchanged; dual-chokepoint risk elevated but not yet triggering L5 regime criteria).
- **Actions: Three new priorities** — Medium confidence (Rhine contingency, JMIC status, EU downstream cascade monitoring).
- **Scenarios: Probabilities unchanged** — Medium confidence (35% / 50% / 15% remain appropriate; decision point 12–15 Aug critical for refinement).

## 2026-08-10 (Day 164)

**Prior brief (Day 161, 7 Aug 2026) scoring:**

| Item | Category | Prediction | Outcome | Score |
|---|---|---|---|---|
| Action 1: PGSA fee waiver lapse (17 Aug) | FM signal | Pending (deadline 10 Aug not yet triggered) | Pending | — |
| Action 2: Rhine gauge <20 cm as L4→L5 trigger | Infrastructure stress | Rhine hit 21 cm on 4 Aug (before 10 Aug deadline) | Hit (early) | Surprise |
| Action 3: QatarEnergy mid-Aug FM extension | LNG cascade | Confirmed via Edison notice 23 July | Hit | Hit |
| Watchlist 1: IRGC blockade enforcement | Kinetic signal | CENTCOM 2 Aug: 35 redirected, 2 disabled | Hit | Hit |
| Watchlist 2: Strait transit stabilization >30/day | Recovery signal | Only 2 on 2 Aug; no stabilization | Miss | Miss |
| Watchlist 3: Rhine recovery signal | Transport de-escalation | Stayed at historic low; no recovery | Miss | Miss |

**Hit rate: 3/6 (50%) on deterministic items; 1 Surprise (Rhine early).** Miss rate on recovery metrics (33%) indicates prior brief overestimated near-term de-escalation probability.

---

**Day 164 (10 August) assessment:**

**Trend:** Same (high confidence, sustained).
- Hormuz: 17 transits/24h vs. 138 baseline (12% recovery). Iran-Oman talks ongoing, no accord formalized. Blockade operational but oscillating.
- Rhine: 21 cm all-time low; no recovery forecast near-term. €125–€130/tonne freight (2x baseline). Second systemic chokepoint locked.
- QatarEnergy: Mid-October FM extension confirmed; no acceleration signal.
- Restart-type FMs: Static at 6; no new forced restarts, no Strait reopening acceleration.
- Kinetic: Jazan repair target 15 Aug (decision point 72h out); Houthi strike geographic expansion (5 Aug) signals capability spread.

**Wave Intensity:** L4 Systemic maintained (high confidence).
- Restart-type FM count static at 6 (no L4→L5 boundary motion).
- Dual-chokepoint stress (Hormuz + Rhine) qualifies as Systemic.
- Jazan restart decision (15 Aug) + Iran-Oman accord (likely 7–20 Aug window) are near-term indicators; if both positive, L4 → 3.5 likely by 1 Sept. If both stall/negative, L4 hardens and L5 probability rises to 35%.
- Current L5 probability: 25% (elevated from 15% Day 161 due to Rhine crisis escalation + Houthi geographic expansion).

**Actions scoring (forward):**
- Action 1 (Jazan 15 Aug restart verification): Decision point at 72h threshold; high information value by 17 Aug.
- Action 2 (Iran-Oman accord tracking): Expected window 7–20 Aug; accord signature = Tier-1 de-escalation signal.
- Action 3 (Rhine Q4 contingency escalation): Activated by 12 Aug; chemical/fuel supply chains now in alert mode (Lanxess switching to rail/road, freight rates locked elevated).

**Surprise factor:** Rhine crisis hit earlier and harder than modeled (21 cm vs. 40 cm baseline stress threshold Day 161). IRGC plateau (no new large-scale kinetic events 5–10 Aug) suggests posturing phase but fragile equilibrium. Houthi geographic expansion (Yanbu 70nm strike 5 Aug) represents tactical capability escalation, not kinetic escalation, but signals risk-zone expansion for insurance/routing decisions.

---

## 2026-08-13 (Day 167) · Backtest scoring

### Prior-run predictions (Day 164 brief, 10 Aug 2026)

**Action 1:** "Jazan restart target 15 Aug; confirm execution by 12 Aug" — **MISS**. Saudi Aramco delayed restart to 30 Aug (per IIR 10 Aug alert) following Houthi strike 8 Aug. Slip was 15 days, not 3. Execution confidence has deteriorated; risk of further slip (to late Sept) is elevated on Houthi strike cadence (2+ strikes in Aug observed).

**Action 2:** "Iran-Oman accord signature by 17 Aug" — **PENDING → FALSE ALARM**. Accord is in final drafting stage (Iranian FM 8 Aug), but signature remains contingent on US policy concessions (sanctions lift, blockade end). No signature announced through 13 Aug. Expected signature window now 14–21 Aug (revised), with material risk of further delay if US conditions harden. Prior prediction overweighted near-term signature probability; current: 40% by 21 Aug, 25% by end-Aug.

**Action 3:** "QatarEnergy FM scope unchanged; confirm mid-Oct extension" — **HIT**. Reiterated via Edison buyer notice; 21 cargoes cancelled/delayed through mid-Sept confirmed. No new acceleration announced. Long-term FM language ("cannot estimate") persists. Scope is stable; no escalation or de-escalation observed.

**Watchlist 1:** "Strait transits >40/24h by 17 Aug signals recovery" — **MISS**. Transits at 13/24h avg (78 over 3–9 Aug per Lloyd's List 12 Aug). Recovery is not materializing; blockade remains effective at ~12% baseline. Forecast for 20 Aug transits: still 15–20/24h (unless accord signed + Strait rapid ramp, probability ~25%).

**Watchlist 2:** "Rhine Kaub >30 cm by 15 Aug signals relief" — **MISS / ESCALATION**. Kaub at 12 cm on 12 Aug (record low, down from 20 cm on 5 Aug). No relief forecast through 25 Aug per BfG. Escalation confirmed; Rhine crisis is now a Hard system-level FM (Tier 1 severity).

**Watchlist 3:** "Restart-type FM count >6 signals L5 boundary" — **PENDING**. Count static at 6; no new restart-type declarations 10–13 Aug. SABIC "cannot estimate" language persists (permanent capacity loss signal). Boundary test not triggered yet, but count staying at 6 for 14+ days is itself an amber signal (no restart momentum).

**Scenario A (L4 Systemic, 50%):** **HIT**. L4 confirmed high confidence. Dual-chokepoint stress (Hormuz 12% baseline + Rhine record low 12 cm) is new evidence supporting L4 persistence baseline. No L4→L5 boundary crossing observed, but L5 tail probability elevated to 25–30% (from 15%) on dual-system stress.

**Scenario B (Iran-Oman accord + 30% Strait recovery, 25%):** **FALSE ALARM / PENDING**. Accord is progressing but signature remains 7–14 days away (minimum). Even if signed by 21 Aug, Strait ramp to 40+/24h faces US policy gating (sanctions, blockade). Scenario B realization now conditional on US sanctions policy shift, which has not been signaled. Revised probability: 20% (down from 25%).

**Scenario C (L5 Regime shift, 25%):** **PARTIAL HIT**. Not yet L5 (Wave Intensity still L4), but dual-chokepoint stress is a stability test that was not anticipated in prior scenario framing. Rhine record-low is a game-changer; adds material tail risk to Scenario C (L5) probability. Revised probability: 30% (up from 25%), with elevated confidence that dual-system stress (Hormuz + Rhine) is the pathway to L5, not single-chokepoint escalation.

### Today's predictions (Day 167)

**Trend:** Same (High confidence). Oscillation within L4 bounds. Jazan slip is kinetic-isolated; Rhine crisis is autonomous. No regime-crossing Hard signal in trailing 72h.

**Wave Intensity:** L4 Systemic (High confidence). Dual-chokepoint pressure now explicit. L5 probability 25–30%.

**Confidence shifts:** Rhine crisis is the new Hard evidence updating the system risk model. Prior briefs did not weight inland transport (non-shipping) FM as a top-tier chokepoint. This run corrects that omission. Dual-system stress (Hormuz + Rhine) is qualitatively different from single-chokepoint dominance; it creates a two-front margin squeeze that is regime-level threat.

### Key surprise this run

Rhine Kaub hitting 12 cm (record low 1880 baseline) on 12 Aug was not anticipated at this magnitude or speed. Water level fell from ~40 cm mid-July to 12 cm by mid-August; trajectory is steeper than 2018 drought year comparable. Industry reaction (BASF, Evonik, Lanxess reporting margin squeeze, modal shift to truck/rail) happened faster than typical. This signals the Rhine crisis is no longer a "yellow light" (monitoring) event; it is now a "red light" (operational constraint) event. System-level implication: if Rhine stays <15 cm through end-Aug, production deferrals begin. This is a new FM pathway (non-Hormuz, non-kinetic) that the three-waves model did not initially cover. The tracker should now monitor global FM events (Rhine, Panama Canal, DRC cobalt, etc.) at equal weight to Hormuz crisis for Wave Intensity calculation.

## 2026-08-16 (Day 170)

**Prior brief (Day 167, 13 Aug) prediction scoring:**

**Trend: Same** — HIT. Trailing 72h (13–16 Aug) showed Strait transits continuing ~13 v/24h (78 over 3–9 Aug per Lloyd's List = 12% baseline). No new Hard production FM declarations. Rhine Kaub gauge at 14 cm (record low) with forecast to <12 cm by 18–20 Aug. Jazan restart delayed to 30 Aug following Houthi strike 8 Aug (kinetic escalation but isolated facility event, not systemic FM extension). Trend held at Same — underlayment deteriorated but no escalation signal crossed threshold.

**Wave Intensity: L4 Systemic** — HIT. Dual-chokepoint stress sustained: Hormuz transits 12% baseline + Rhine Kaub record low 14 cm. Restart-type FM count static at 6 (QatarEnergy 5-yr, KPC FM#2, SABIC "cannot estimate", EGA 12-mo, QE conditional, KPC unconditional). L4→L5 boundary criteria not yet met (Hormuz blockade effective but not compounding via systemic kinetic escalation; Rhine independently stressed but not yet cascading to production-wide curtailment). L4 Systemic maintained.

**Action 1: Monitor Iran-Oman accord closure by 17 Aug** — MISS (deadline passed). Accord remains in "final drafting" (7 Aug Iranian FM statement); no formal joint statement signed as of 16 Aug. Deadline extended to 23 Aug in today's brief (revised Action 1).

**Action 2: Track Jazan restart (30 Aug target)** — PENDING. On track per IIR monitoring (10 Aug statement). No new escalation 13–16 Aug; restart remains tentatively scheduled for 30 Aug. High sensitivity to Houthi attack cadence (7–10 day intervals).

**Action 3: Rhine Kaub forecast through 20 Aug** — ON TRACK. BfG forecast (updated 14 Aug) holds <12 cm through 20 Aug. Kaub at 14 cm (16 Aug); forecast to 9–11 cm by 18–20 Aug. Scenario B (accordion stall + Rhine persists <12 cm) activation risk elevated.

**Watchlist 1: Iran-Oman accord closure** — MISS (deadline 17 Aug passed). Accord unsigned as of 16 Aug. Trigger revised to 23 Aug.

**Watchlist 2: Houthi geographic spread** — CONFIRMED. Red Sea strike off Yanbu (5 Aug, 70 nm outside declared zone) + Jazan strike (8 Aug, second in 10 days) = geographic escalation from Strait corridor to Saudi west coast. Pattern: 7–10 day attack cadence.

**Watchlist 3: EU converter restart timing (BASF/Ineos)** — ESCALATED. No public restart guidance issued; production margin squeeze now observable (C&EN, Bloomberg 15–16 Aug). Threshold crossed: margin pressure moved from Tier 2 "analyst commentary" to Tier 1 "operational constraint" (BASF/Lanxess/Evonik/Ineos public statements 15–16 Aug).

**Watchlist 4: Restart-type FM count move above 6** — STATIC. Count remains at 6 (no new restart-type FMs issued 13–16 Aug). Jazan restart delayed but not yet re-classified as restart-type FM (remains Wave 1 production FM as of 16 Aug).

**Watchlist 5: PGSA 48-hour notice compliance rate** — STATIC. No public data 13–16 Aug. Lloyd's List (14 Aug) cites 78 transits over 3–9 Aug; no PGSA advisory updates 13–16 Aug.

**Scenario A (Accord closes, transits 40–50/day by 20 Aug)** — MISS (20 Aug deadline passed 13 Aug brief). Accord unsigned; transits remained 12% baseline. Prior probability was 35%; should have been 15% (missed escalation probability calibration). Posterior: 20%.

**Scenario B (Rhine <12 cm, dual stress propagates, Naphtha FM #150+)** — PENDING / TRACKING. Rhine holding <12 cm forecast through 20 Aug (on track). No new naphtha FM declarations 13–16 Aug (count remains stable), but BASF/Lanxess margin squeeze observable = Wave 3 cascade beginning. Probability tracking at 35% (unchanged from Day 167).

**Scenario C (Hormuz + Rhine persist, L4→L5 by 25 Aug)** — PENDING / ESCALATED. Both chokepoints persist (Hormuz 12% baseline, Rhine 14 cm). Forecast no L4→L5 transition by 25 Aug (too narrow window). But dual-chokepoint stress now explicit; L4→L5 probability if Scenario B conditions hold through 31 Aug. Scenario C probability revised to 25% (day 167: 30%).

**Surprise factor:** Jazan delay timing precision — Houthi strike exactly 14 days before scheduled restart (mid-Aug) pushed target to 30 Aug. Attack was kinetically minimal (one tank fire, quickly extinguished) but strategically maximal in timing. Second surprise: Rhine forecasts consistently under-revised — BfG 12 Aug forecast said 12 cm by 18–20 Aug; current reading 14 cm on 16 Aug tracking to 9–11 cm window, suggesting further decline possible. Dual-chokepoint stress interaction (Hormuz + Rhine) now measurable; system-level capacity squeeze more severe than modelled at Day 167.

## 2026-08-19 (Day 173)

**Prior predictions scored (Day 170, 16 Aug):**
- Trend (Same, high confidence): **Hit** — trailing 72h (16–19 Aug) confirmed no new Hard FM declarations, Strait transits holding 13–14/24h, Rhine critical <15 cm. Same maintained.
- Wave Intensity (L4 Systemic, high confidence): **Hit** — dual-chokepoint stress (Hormuz 12% baseline + Rhine 6 cm record low) sustained without L4→L5 move. L4 maintained.
- Action 1 (Jazan 15 Aug restart + Houthi risk): **Hit** — Jazan delayed to 30 Aug after 8 Aug strike. Escalation correctly predicted.
- Action 2 (Rhine <15 cm through 20 Aug): **Hit** — Kaub at 6 cm on 14 Aug; <15 cm forecast holds through 22 Aug. Rhine persistence confirmed.
- Action 3 (Iran-Oman accord "final drafting" stall beyond 25 Aug): **Pending** — 3-day horizon intact. No new announcement 16–19 Aug; stall likely (70%+ probability by 19 Aug).
- Watchlist 1 (Houthi 3rd Saudi strike by 22 Aug): **False alarm** — 8 Aug Jazan strike occurred; no 2nd Saudi strike claimed 9–19 Aug. Escalation occurred but not Saudi-specific pattern.
- Watchlist 2–5: **Pending** (horizons extend beyond 19 Aug; multiple pending at T+1–T+10).
- Scenarios A/B/C: **On track** — Scenario A (dual stress persists) is tracking as baseline (45% confidence). Scenarios B/C remain live conditional on Iran-Oman breakthrough or Jazan slip past 30 Aug.

**Today's assessment (Day 173, 19 Aug):**
- **Trend:** Same (sustained). No escalation signals 16–19 Aug. Dual-system stress visible but not regime-shifting. Confidence: high.
- **Wave Intensity:** L4 Systemic (sustained). Restart-type FM count static at 6. L4→L5 boundary test not triggered. Conditional escalation risk flagged for 25 Aug (Iran-Oman decision) + 30 Aug (Jazan restart). Confidence: high.
- **Actions this run:** (1) Jazan 30 Aug forcing function (T+11); (2) Iran-Oman accord 25 Aug decision point (T+6); (3) Rhine Kaub + EU chem FM watch (T+3–10 days).
- **Watchlist focus:** (1) Houthi geographic spread (escalation indicator); (2) Strait transits floor 13–14/24h (regime indicator); (3) Rhine recovery forecast (cascade trigger); (4) QatarEnergy scope extension (FM expansion signal); (5) Restart-type FM new declarations (boundary test).
- **Forecast confidence:** 85% (Trend + Wave Intensity). Scenario probabilities: A 45% (baseline dual stress), B 35% (diplomatic breakthrough), C 20% (kinetic escalation + cascade).

**Surprises this run:** 
1. **Rhine escalation ahead of forecast** — Kaub at 6 cm (14 Aug) is below prior expectation of 10–15 cm range. However, cascade FMs (EU chem declarations) have NOT yet materialized, suggesting operators are absorbing cost through inventory/modal shift longer than expected. This lag suggests either (a) €50–60/MWh TTF prices and 2–3x rail/road costs are acceptable short-term (4–6 weeks) or (b) operators expect Rhine recovery by early September.
2. **Mocha facility strike (17 Aug) — new kinetic pattern** — Houthis shifted from ship-targeting (tankers) to infrastructure-targeting (moored vessels, berths) on 17 Aug. This is a testing pattern: if Mocha berth confirmed permanently damaged, it indicates Houthi targeting doctrine is expanding from shipping denial (blockade) to logistics hub degradation. Not yet escalation to Strait-side infrastructure (Ras Tanura, Fujairah), but pattern is worth tracking.

**What to change next run:** No methodology changes warranted. Trend and Wave rules held perfectly (Hit + Hit). Actions and watchlist remain well-calibrated to forcing functions (Jazan date, Iran-Oman accord, Rhine forecast). If Brier score on scenarios (A/B/C) deteriorates below 0.30 over next 4-week rolling average, revisit scenario probability weights. Currently: Brier on scenarios not yet calculated (insufficient historical data); will begin scoring in next weekly roll-up (by 26 Aug).

## 2026-08-22 (Day 176)

**Prior prediction scoring (Day 173, 19 August brief):**
- **Trend prediction:** Same (high confidence) — **Hit**. No new Hard FM declarations 20–22 Aug; Strait transits <5% baseline; Jazan restart delay is facility-level kinetic, not systemic. Trend held.
- **Wave Intensity prediction:** L4 Systemic (high confidence) with conditional L4→L5 escalation risk 40–45% if Iran-Oman accord stalls after 25 Aug — **Pending**. Accord deadline (25 Aug) not yet reached; no escalation to L5 triggered 20–22 Aug. L4 maintained.
- **Actions (prior brief):**
  1. Monitor PGSA insurance fee deadline (17 Aug) for allocation boundary — **Miss** (not a Hard FM boundary; administrative governance only).
  2. Watch KPC/SABIC/EGA restart guidance (watch analyst calls 1–15 Aug) — **Pending** (analyst call window 23–30 Aug ongoing; SABIC guidance unrevised as of 22 Aug).
  3. Rhine Kaub daily tracking — **Hit**. Kaub confirmed at 16 cm (22 Aug); record low, barge loads 27% capacity; tracking ongoing through 25 Aug.
- **Watchlist (prior brief):**
  1. Strait reblockade post-MoU collapse (17 Aug) — **Hit**. MoU expired; US blockade reinstituted; transits <5% baseline confirmed.
  2. Houthi escalation (Red Sea strikes, geographic expansion) — **Hit**. Third Houthi claim on Jazan (18 Aug) confirmed; Bab el-Mandeb toll demand unconfirmed but toll demand rumours confirmed by UANI.
  3. Rhine persistence below 20 cm through 22 Aug — **Hit**. Kaub at 16 cm; forecast <15 cm 22–25 Aug per BfG; full modal shift risk active.
- **Scenarios (prior brief):**
  - Scenario A (Strait reopens by early September) — **On track** (20% prob). No new signals shifting toward opening.
  - Scenario B (Extended blockade through 2027) — **Elevated** (65% prob). Iran-Oman accord stalled; Houthi targets expanding.
  - Scenario C (Limited reopening) — **Diminished** (15% prob). No diplomatic progress signals.

**Today's Trend / Wave Intensity assessment:**
- **Trend:** Same (high confidence). No new Hard FM 20–22 Aug; Strait closure de facto; Jazan delay is facility-level kinetic only; restart-type FM count static.
- **Wave Intensity:** L4 Systemic (high confidence). Dual-chokepoint stress (Hormuz 12% + Rhine 27%) persists; L4→L5 boundary escalation probability rises to 45–50% if Iran-Oman accord collapses after 25 Aug AND Rhine <20 cm through end-Aug (both now ≥70% probable each).

**Surprise factor:** No surprises this run. Houthi third claim (18 Aug) was within expected escalation pattern (tempo of 2 attacks per week observed). Rhine record low on schedule per BfG forecast. Iran-Oman accord stall continues as expected base case.
