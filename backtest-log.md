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
