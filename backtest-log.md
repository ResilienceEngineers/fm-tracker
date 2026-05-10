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
