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

## Hypotheses Created & Resolutions (Day 81)

### New Hypotheses

**H-001 · Created 2026-05-19 (Day 81) · Stop-out 2026-06-02 (Day 96)**

**Hypothesis:** If KPC and SABIC both file FM extensions to 30 June on Tadawul by 23 May, Wave Intensity escalates to L5 Systemic by 26 May.

**Discriminating observable:** Twin Tadawul filings (KPC + SABIC) using phrase "force majeure extended" or "restart date uncertain, awaiting Strait access" or "unable to estimate return" (repeating SABIC 9 Apr language). Source: Tadawul exchange (direct regulatory filings), Tier 1. Threshold: Both operators, same filing window (20–23 May), same restart-type FM language.

**Prior probability:** 0.65 (KPC FM#2 language "even when reopens" + SABIC "cannot estimate" on 9 Apr suggest political caution; extension likely if Strait talks stall by 20 May; Strait talks have made "great progress" per Trump 6 May, but stalled by 16 May per briefings).

**Status:** Open.

---

**H-002 · Created 2026-05-19 (Day 81) · Stop-out 2026-05-26 (Day 88)**

**Hypothesis:** Singapore bunker fuel inventory falls below 30 days or price exceeds $850/tonne sustained 3+ consecutive days by 26 May, triggering formal Type 4 Distribution FM from Maersk or MSC.

**Discriminating observable:** Platts bunker report (daily spot quote) + Port Authority Singapore weekly inventory bulletin. Bunker price >$850/tonne for 3 calendar days (e.g., 23–25 May) OR inventory <30 days stock reported in weekly bulletin (next release ~22 May). Source: Platts OPIS, S&B, Singapore Port Authority, Tier 1.

**Prior probability:** 0.55 (Singapore currently ~45 days, prices $800/tonne, trending upward; cutoff at 30 days is operational threshold for shipping lines to declare FM; current trajectory (bunker +$20/tonne per week, inventory -2 days per week) suggests 25–26 May crossing).

**Status:** Open.

---

**H-003 · Created 2026-05-19 (Day 81) · Stop-out 2026-05-23 (Day 85)**

**Hypothesis:** Iran foreign ministry or IRGC announces Strait reopening timeline (any date: June, July, "when conditions allow") OR announces permanent closure / expanded operational zone by 23 May.

**Discriminating observable:** Official statement from Iran Foreign Ministry (Araghchi) or IRGC Navy command, reported by Reuters, Bloomberg, AP, or Iranian state media (IRNA). Language specificity: "reopening timeline X", "closure permanent", "operational zone expanded to [new coordinates]". Source: Iranian state media + Western wire reports, Tier 1.

**Prior probability:** 0.70 (Iran often signals via official statements to manage insurance markets & investor confidence; 15 days have passed since Strait redefinition (7 May, Wikipedia entry); signaling window is open; Pakistan-mediated talks suggest de-escalation momentum, increasing likelihood of reopening-timeline signal rather than permanence signal).

**Status:** Open.

---

**H-004 · Created 2026-05-19 (Day 81) · Stop-out 2026-06-18 (Day 112)**

**Hypothesis:** By 18 June (T+30), Scenario B (stalemate entrenches, Trend Worse, Wave Intensity L5) has become observed reality (not just probability forecast).

**Discriminating observable:** (a) KPC + SABIC FM extended to 30 June OR later (Tadawul filings), (b) Strait traffic remains 5–10% (Kpler AIS), (c) Maersk or MSC formal Type 4 bunker FM filed (company announcement), (d) At least one naphtha trader or secondary supplier declares FM on feedstock starvation (Tier 2–3 source). Four conditions; need 3/4 met by 18 June for "Scenario B observed."

**Prior probability:** 0.55 (Current brief Scenario B probability; if KPC/SABIC extend on 20–23 May, posterior probability rises to 0.75+ by 26 May; 18 June gives 3-week window for maritime FM + naphtha trader FM to materialize).

**Status:** Open.

## New hypotheses for this run

**H-001 · Created 2026-05-19 (Day 81) · Stop-out 2026-05-29 (Day 91)**

**Hypothesis:** If Lotte Chemical Yeosu restarts on schedule (29 May), naphtha feedstock scarcity is not binding enough to prevent primary-operator restart; Strait reopening assumption (June pickup) is gaining market credibility.

**Discriminating observable:** Seoul Economic Daily or ICIS formal confirmation that production resumed at Lotte Yeosu on or before 29 May 2026, with nameplate capacity ≥90% utilization within 48h.

**Prior probability:** 0.70 (based on Day 78 Seoul Economic Daily reporting and absence of extension announcements 16–19 May).

**Status:** Open.

---

**H-002 · Created 2026-05-19 (Day 81) · Stop-out 2026-05-20 (Day 82)**

**Hypothesis:** Trump-Iran ceasefire will NOT be extended past 20 May 2026; collapse will trigger Scenario B (July closure).

**Discriminating observable:** No new ceasefire agreement or extension announced by Trump administration or Iran IRGC by end of 20 May 2026 (24:00 UTC). Absence = ceasefire collapse.

**Prior probability:** 0.35 (based on Trump 11 May statement "on life support" + zero agreement signals 12–19 May).

**Status:** Open.

---

**H-003 · Created 2026-05-19 (Day 81) · Stop-out 2026-05-26 (Day 88)**

**Hypothesis:** No maritime operator (MSC, Maersk, Hapag, CMA CGM, Evergreen, Zim) will file formal Type 4 bunker FM by 26 May despite $800/tonne Singapore bunker price; operators absorb cost within contractual variation clauses.

**Discriminating observable:** Zero Type 4 FM filings from Tier 1 shipping operators on Lloyd's List, Splash247, company IRs, or regulatory databases (CFTC, FCA) by 23:59 UTC 26 May.

**Prior probability:** 0.50 (observationally, maritime operator FM lag is 10–14 days behind commodity signal; bunker signal emerged 12 May; threshold is 23–26 May).

**Status:** Open.

---

## Resolutions for hypotheses whose stop-out passed

None this run. All three hypotheses are forward-looking (stop-out dates 20 May onward; today is 19 May).
