# Hypothesis log — Force Majeure Tracker

**Status:** Internal. Every brief generates ≥1 falsifiable hypothesis with an explicit stop-out date. On each subsequent run, open hypotheses with passed stop-outs are resolved (Hit / Miss / False alarm / Surprise) and the resolution feeds back into scenario priors. This is the Popperian leg of the methodology — predictions that cannot be falsified are not predictions.

The hypothesis log differs from the backtest log in three ways:
1. **Explicit stop-out date.** A hypothesis without a date by which it must resolve is not a hypothesis.
2. **Discriminating observable.** What specific signal would prove this false? Generic "the situation may worsen" is rejected.
3. **Prior + posterior.** What was the probability at hypothesis-creation; what is it after resolution.

---

## Format

```
## H-NNN  ·  Created YYYY-MM-DD (Day N)  ·  Stop-out YYYY-MM-DD (Day N+k)

**Hypothesis.** Single declarative sentence. No hedges. ≤ 25 words.

**Discriminating observable.** What specific data point would prove this false? Name the source. Specify the threshold value.

**Prior probability.** 0.NN (estimated at creation).

**Status.** Open · Pending stop-out · Resolved [Hit | Miss | False alarm | Surprise]

**Resolution note (filled at stop-out).** One paragraph. Posterior probability. What this taught the methodology.
```

---

## Acceptance criteria for a hypothesis to be admitted

- **Falsifiable.** A specific observable would falsify it.
- **Dated.** Specific calendar date by which the resolution is observable.
- **Independent.** Not a restatement of an already-open hypothesis.
- **Decision-relevant.** Resolution would shift the brief's actions, watchlist, or scenarios.

Hypotheses failing any of these are rejected and not logged. The model is instructed not to pad.

---

## Open hypotheses

_(populated by the daily updater on each run; resolved here when stop-out passes)_

---

## Resolved hypotheses

_(populated as stop-outs pass)_

---

## Calibration view

| Bucket | Predicted P | Actual hit rate | Count | Brier contribution |
|---|---|---|---|---|
| 0.0–0.2 | 0.10 | _tbd_ | 0 | _tbd_ |
| 0.2–0.4 | 0.30 | _tbd_ | 0 | _tbd_ |
| 0.4–0.6 | 0.50 | _tbd_ | 0 | _tbd_ |
| 0.6–0.8 | 0.70 | _tbd_ | 0 | _tbd_ |
| 0.8–1.0 | 0.90 | _tbd_ | 0 | _tbd_ |

A well-calibrated forecaster has actual-hit-rate ≈ predicted-P in each bucket. Systematic over- or under-confidence shows up as the diagonal drifting from the 1:1 line.
