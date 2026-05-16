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

## New hypotheses for this run (Day 78)

**H-012 · Created 2026-05-16 (Day 78) · Stop-out 2026-05-23 (Day 85)**
- **Hypothesis:** Maritime operator bunker FM will be declared by a top-3 carrier (MSC, Maersk, CMA CGM) by 23 May 2026, formalizing Type 4 Distribution signal.
- **Discriminating observable:** Formal FM notice (email to customers or regulatory filing) naming "force majeure" + "bunker fuel" from MSC, Maersk, or CMA CGM, published before 23 May. If not published by EOD 23 May, hypothesis is False.
- **Prior probability:** 0.35 (bunker prices at $800, reserves dwindling, shipping pain visible in financial metrics; but carriers have absorption capacity and may delay FM declaration to preserve customer relationships).
- **Status:** Open.

**H-013 · Created 2026-05-16 (Day 78) · Stop-out 2026-05-20 (Day 80)**
- **Hypothesis:** KPC or SABIC will extend multi-year force majeure language (or issue a new "cannot estimate" / "even when reopens" FM) by 20 May 2026, signalling multi-quarter restart dependency.
- **Discriminating observable:** Tadawul / KPC regulatory filing or press statement containing exact phrase "cannot estimate return" OR "even when" OR "contingent on geopolitical" + specific date clause extending past 20 May 2026. If not filed by EOD 20 May, hypothesis is False.
- **Prior probability:** 0.25 (grace-period windows expire mid-May; operators may wait for Strait partial reopening signal before extending language; no strong incentive to formalize multi-year FM if diplomatic talks ongoing).
- **Status:** Open.

**H-014 · Created 2026-05-16 (Day 78) · Stop-out 2026-05-29 (Day 89)**
- **Hypothesis:** Lotte Chemical restart will slip again past 29 May 2026 (second delay), signalling sustained naphtha feedstock gap extending to June.
- **Discriminating observable:** Lotte Chemical or parent company official announcement (press release, stock exchange filing, or media statement in Seoul Economic Daily / Hankyung) confirming restart date > 29 May. If restart confirmed on 29 May or earlier, hypothesis is False.
- **Prior probability:** 0.40 (naphtha feedstock gap is structural, not logistical; refining recovery dependent on Strait reopening; Maybank June halt risk flag suggests multi-week additional delay likely).
- **Status:** Open.

**H-015 · Created 2026-05-16 (Day 78) · Stop-out 2026-06-01 (Day 94)**
- **Hypothesis:** No new primary-operator FM declarations (Hard, Tier 1) will be announced in the 72-hour windows of 16–19 May, 19–22 May, or 22–25 May 2026; FM count remains static at 114 through May 25.
- **Discriminating observable:** Zero Hard FM declarations from operators in the official Tier 1 list (QatarEnergy, KPC, SABIC, BAPCO, EGA, ALBA, Qatalum, Saudi Aramco, OMV, Orlen, Shell, TotalEnergies, LyondellBasell, Chevron Phillips Chemical, Dow, Mitsubishi Chemical, etc.) in formal press releases or stock exchange filings dated 16–25 May. If one or more new Hard FM is published, hypothesis is False.
- **Prior probability:** 0.70 (Wave 1–2 cluster has stabilized; no new escalation expected absent geopolitical event; Trend = Same rule supports stability).
- **Status:** Open.

## Resolutions for hypotheses whose stop-out dates have passed

None. All hypotheses in this run are forward-looking (stop-out dates ≥ 23 May). No prior-run hypotheses are retroactively resolved on Day 78.

---
