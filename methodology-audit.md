# Force Majeure Tracker — Methodology Audit

**Status:** Internal post-build review. Day 78 · 16 May 2026.
**Posture:** Independent critique applied at the level expected by MIT systems-engineering, Harvard policy-analysis, and Santa Fe Institute complex-systems review. The audit is adversarial on purpose — every finding is something the current tracker gets wrong or hides.

This file lives alongside `methodology.md`. The methodology is the rule the tracker runs by; this file is the rule's confrontation with reality.

---

## Executive summary

Seven methodological foundations are currently weak. Most are common to ad-hoc crisis-intelligence pipelines; none are unique to this build. Concrete fixes are listed in Section 9 with implementation cost vs analytical lift.

| # | Finding | Severity |
|---|---|---|
| 1 | Signal-tier weights (5/3/1/0) are asserted, not derived | High |
| 2 | Trend rule is regime-blind (fails in equilibrium phases) | High |
| 3 | Wave Intensity scale is ordinal-used-as-cardinal; no probability mapping | High |
| 4 | Three Waves model lacks transition probabilities — descriptive, not predictive | Medium |
| 5 | Source coverage has 9 specific blind spots (Chinese, Korean, AIS, SEC 8-K, ECHA, …) | High |
| 6 | Volume-weighting absent — a 1,300 kt/yr FM and a 5 kt/yr FM count equally | High |
| 7 | No abstention rule — system is structurally biased toward publication | Medium |
| 8 | Learning loop logs reflections but doesn't change rules automatically | High |

---

## 1. Signal-tier framework critique  *(systems-engineering register)*

**Current rule.** Hard ×5, Medium ×3, Soft ×1, Noise ×0. Trend rule uses Hard only. Wave Intensity moves only on operative-test-passing Hard signals.

**What's wrong.**

1. The 5:3:1:0 ratio is **asserted, not derived**. No empirical basis is given. In control-theoretic terms, this is a hand-tuned gain with no closed-loop verification of stability.
2. The classification is **binary in practice**. Hard moves the needle; nothing else does. The ×3 and ×1 weights have no observable effect because the trend rule and Wave Intensity tests gate on Hard-only. Medium and Soft are decorative.
3. "Hard" is **internally heterogeneous**. A 1,300 kt/yr methanol shutdown (Methanex Damietta) and a 5 kbpd specialty-refinery FM are both "Hard" — but the information value of those two events differs by ~250×. The current framework cannot distinguish them.
4. **No signal-to-noise floor.** When the model classifies 20 events in a run, the framework has no way to express "this whole bag is low-quality, fall back to abstention".

**Improvement (implementing).** Replace the flat tier weight with a two-axis classifier:

- **Source-tier (confidence-of-occurrence):** Tier 1 = 1.0 · Tier 2 = 0.7 · Tier 3 = 0.4 · Tier 4 = 0.2 · Tier 5 = 0.1 · Tier 6 = 0.0
- **Impact-volume class:** small (<10 kt/yr) = 1 · medium (10–100) = 3 · large (100–1000) = 10 · mega (>1000) = 30 · sovereign (multi-operator / contract-level) = 50
- **Effective weight** = confidence × volume_class
- **Wave-Intensity move threshold:** cumulative effective weight ≥ X over 72h, where X is calibrated against the backtest hit-rate.

The 5:3:1:0 ratio disappears; in its place is a number that can be measured, tested, and tuned. The current `methodology.md` keeps the old language for now; the new framework will be wired into the prompt and the script.

---

## 2. Trend rule critique  *(time-series / regime-conditional reasoning)*

**Current.** Trailing 72h vs prior 72h. Worse if ≥2 Hard escalation OR 1 regime event.

**What's wrong.**

1. The 72h window is **fixed**. It works in active phases (Days 1–20) but degrades in equilibrium phases (Days 70+). The Day-73 reflection flagged this: "absence of new FMs is itself the signal" — but the trend rule has no mechanism to read absence as information.
2. The rule is **direction-asymmetric in a hidden way**. Worse requires ≥2 events; Better requires ≥1 de-escalation. So Worse is harder to reach than Better — but the empirical population of crisis events tilts heavily Worse. Net effect: the rule **under-detects de-escalation** when de-escalation is rare.
3. The 72h-vs-prior-72h comparison assumes the prior window is the right baseline. **It isn't.** Day-5 prior-72h was Wave 1 onset (zero baseline rate); Day-78 prior-72h is equilibrium (low rate). They're not comparable, but the rule treats them as the same kind of window.
4. **Volume-blind.** The rule counts events, not impact. Two trivial FMs trigger Worse; one sovereign-level FM at the same volume as those two combined does not, by itself.

**Improvement (Phase 2).** Move to a **regime-conditional trend test**:

- Define regime by Wave-Intensity level + observable indicators (Aramco OSP delta, AIS Hormuz transit ratio, restart-type FM count).
- For each regime, maintain an **expected event-rate distribution** (Poisson-like prior, λ tuned by backtest).
- Compute trend as `observed_72h_rate − expected_72h_rate_given_regime`, scaled by the regime's standard deviation.
- This is a Bayesian-flavoured detector — it reads absence as evidence (low rate against a high λ prior means the regime is decaying).

For Day-78 today: implementing partial version — add the **regime-event-rate baseline** to `knowledge-base.md` (computed from historical data) so the model can compare observed rate to baseline manually. Full Bayesian filter is Phase 2.

---

## 3. Wave Intensity scale critique  *(measurement theory)*

**Current.** L1 Watch → L5 Regime, with operative tests per boundary.

**What's wrong.**

1. The operative tests have **escape valves**. "Confirmed cluster across ≥2 chains" is observable. But "physical-absence dominant" (L4→L5 boundary) is subjective. The reflection log already flagged this.
2. The scale is **ordinal but used as cardinal**. Differences between levels are treated as equal; they aren't. L1→L2 is a watchful uptick; L4→L5 is a regime shift implying multi-quarter physical absence. Different beasts.
3. **No probability mapping.** "Wave Intensity L4" doesn't tell you P(major-FM-30d-out) or P(restart-in-Q3). It's a category; categories don't help decisions.
4. **Sticky.** The level has held at L4 for 6+ runs. The reflection log noted "absence of surprise is itself a signal" — but Wave Intensity has no mechanism to recognize stuck states.

**Improvement (implementing).** Map Wave Intensity to **outcome distributions** rather than thresholds. Each level corresponds to a forward-looking probability table that the model carries into the brief:

| Level | P(major-FM ≤30d) | P(restart ≤30d) | P(regime-shift ≤90d) |
|---|---|---|---|
| L1 Watch | 0.10 | 0.30 | 0.05 |
| L2 Elevated | 0.30 | 0.20 | 0.10 |
| L3 Cascade | 0.55 | 0.10 | 0.20 |
| L4 Systemic | 0.70 | 0.05 | 0.35 |
| L5 Regime | 0.85 | 0.02 | 0.55 |

These priors update as the backtest accumulates Hits / Misses. The level is then *defined by* the distribution it maps to, not by an operative test alone. This converts the scale from category to probabilistic forecast — a decision-relevant object.

---

## 4. Three Waves model — operational vs formal  *(Markov chain register)*

**Current.** Wave 1 production / Wave 2 allocation / Wave 3 physical absence. Time-to-FM patterns are observed empirically.

**What's wrong.**

The model is **descriptive but not predictive**. It says "Wave 1 → Wave 2 takes 3–10 days" because that's what was observed in *this* crisis. Without transition probabilities estimated across comparable historical events, the time-to-cascade is not a parameter — it's an anecdote.

**Improvement (Phase 2 — deferred).** Cast as a discrete-time Markov chain:

- States: {Wave 0 = pre-crisis · Wave 1 · Wave 2 · Wave 3 · Recovery}
- Transition matrix `P[i→j]` estimated from this crisis plus comparable historical events:
  - 2008 Hurricane Ike + US Gulf petrochemicals
  - 2011 Sendai earthquake + Japanese auto parts cascade
  - 2018 Aramco Khurais/Abqaiq + Saudi crude
  - 2022 Russia/Ukraine + ammonia/wheat/nickel
- Use the forward algorithm to compute the posterior over current state and project to T+30.
- Wave Intensity becomes a **posterior over states given observed evidence** — proper Bayesian filtering.

Phase-1 partial: document the four reference events in `knowledge-base.md` so the model can pattern-match against them.

---

## 5. Coverage completeness audit  *(empirical critique)*

**Documented blind spots:**

| Gap | What's missed | Action |
|---|---|---|
| Chinese-language primary | 21st Century Business Herald, Caixin, China Chemical Reporter — surface Chinese operator FMs 12–48h before Reuters | Add to prompt search-target list, instruct query in Chinese when Chinese operator is the topic |
| Korean disclosures | KRX (Korean Exchange) regulated filings — Yeochun NCC restructuring hit KRX before Seoul Economic Daily | Add KRX disclosure portal to source list |
| Japanese commercial wire | Mainichi, Iyaku Shokai (pharma), Nikkei proper | Add to source list |
| AIS data | Lloyd's List Intelligence is in the sources file but not search-accessible (paid). Free workaround: MarineTraffic, VesselFinder | Instruct model to cite MarineTraffic for Hormuz transit counts |
| SEC 8-K filings | US-listed operators (LyondellBasell, Chevron Phillips, Olin, Trinseo) file material events within 4 business days | Add SEC EDGAR full-text search to prompt |
| Tadawul | Listed but only SABIC has been cited; Bursa Saudi has 6 listed chemical operators | Add Tadawul-FM-disclosure query to prompt |
| BSE/NSE Schedule III | Indian operators — bot has cited some, but inconsistently | Standardize via prompt |
| EU REACH / ECHA | Chemical operators in EU file ECHA notifications on capacity changes | Add to source list |
| Insurance pricing | P&I clubs (Britannia, Gard, Skuld) post war-risk premiums that move *before* FMs | Add insurance-rate query to prompt |
| Cargo tracking | Project44, FourKites, MarineTraffic | Add to prompt |

**Quantified language bias.** Of the ~24 events the bot surfaced on this run, ~21 were English-primary, 3 were translated from Korean/Japanese. Chinese / Korean / Japanese operators are underrepresented relative to their share of global FM volume (Asia-Pacific is ~45% of global petchem capacity).

**Implementation (now).** The system prompt is being expanded with explicit Chinese / Korean / Japanese source instructions plus SEC EDGAR + ECHA + P&I insurance signals. Source-reliability auto-scoring (Section 8) will reveal whether the new sources actually produce Hits.

---

## 6. Translation quality risks  *(catalogued from actual outputs)*

**Wave-assignment errors observed.**

- MRPL gasoline export FM (D4) — dataset has `wave=2`; bot has at times treated as Wave 1.
- Inovyn PVC FM (D7) — dataset has `wave=3`; bot's output occasionally Wave 1.
- Restart-type FMs (KPC FM2, QE 5-yr) — sometimes counted as new Wave-1 production FMs rather than as forward-coverage signals.

**Source-tier inflation.**

- Polymerupdate has appeared as "Tier 1" in bot output; it is Tier 2 in `sources.md`.
- Bloomberg's secondary reports on operator statements have been treated as Tier 1 even when the operator hasn't independently confirmed.

**Country-of-origin ambiguity.**

- ALBA: Bahrain (origin), global aluminium market (impact). Geo-tag inconsistent.
- Chevron Phillips: USA (origin), export halt affects global SM market.

**Volume bias.** All FMs counted equally. Sadara Jubail (2.98 Mt/yr across 26 units) and Trinseo Tessenderlo (PS-HI specialty, ~50 kt/yr) both = 1 in the cumulative count. This dilutes the signal.

**Implementation (now).** Volume-weighted FM index (Section 9.3) addresses the volume bias. The other errors require periodic backtest review — added as standing items in the per-run reflection prompt.

---

## 7. Bias inventory  *(cognitive science register)*

**Recency bias.** Stats strip and trend rule implicitly favor recent events. A 70-day-old still-active FM and a fresh restart-type FM carry the same dashboard weight, despite vastly different information content. The new Volume-Weighted Index partly fixes this; full fix is regime-conditional trend (Phase 2).

**Availability bias.** The web-search tool privileges accessible (English, indexed, recent) sources. The bot doesn't know what it's not seeing.

**Authority bias.** Sovereign producers (QatarEnergy, Aramco) get implicit Tier-1 treatment even when their statements have been contradicted by AIS data historically. The audit recommends a routine "authority-statement vs independent-verification" check in the system prompt.

**Confirmation bias.** Wave Intensity has held at L4 for 6+ runs. The reflection log noted this; the rules haven't propagated the insight into a forced re-examination. Added to `methodology.md` as a routine de-anchor check: every 4th run, attempt to argue Wave Intensity should *change*, and require Hard signals to confirm continuation.

**Survivorship bias.** Public, English-speaking, listed operators announce FMs. Private, non-English, small operators don't. The tracker sees a non-random sample. Documented; partial mitigation through expanded source coverage.

**Reflexive prediction (Soros).** When operators read intelligence briefings, they may hedge earlier — which would change the cascade timing the tracker is predicting. Worth monitoring as adoption grows. No fix today; flagged for review when subscriber count reaches a threshold.

---

## 8. Calibration & learning loop integrity

**Current.** Backtest log scores predictions T+1 / T+3 / T+7. Weekly Brier on scenario probabilities. Reflection log proposes methodology deltas (manual).

**What's working.**

- The backtest entries are honest (Misses are logged as Misses, including the Lotte False alarm).
- Reflection log already proposed 5 concrete improvements on Day 73 — meaning the loop is generating insight.

**What's broken.**

- The proposed improvements **haven't actually changed the methodology**. Day-73 reflection said "add a Signal Velocity card" — never built. "Promote operator restart-date slippage to Hard weight" — not in `methodology.md`. The loop generates recommendations but the system doesn't auto-apply them.
- Brier scoring exists in concept but **no resolved scenarios yet** — first scoring date is 9 June. The framework is dormant.
- Reliability diagrams, sharpness, discrimination — none of these are computed.

**Implementation (now).** Three changes:

1. **Methodology delta auto-proposal.** When Miss rate > 30% in any category (Actions / Watchlist / Scenarios) over 4 consecutive runs, the system MUST propose a specific delta in the REFLECTION block and APPEND it to `methodology.md` with a date and reason. The append is automatic via the script.

2. **Source reliability auto-scoring.** New file `source-reliability.md` maintained by the script. For each named source: citations, confirmed-downstream-events, hit rate. Sources below 0.6 over 4 weeks → downgrade one tier; sources surfacing primary documents 24h ahead → promote.

3. **Hypothesis log with falsification dates.** Every brief generates ≥1 falsifiable hypothesis with explicit stop-out. Logged in `hypothesis-log.md`. On each run, open hypotheses are resolved; resolutions feed scenario priors.

---

## 9. Recommended upgrades, prioritised

| # | Upgrade | Cost | Lift | Status |
|---|---|---|---|---|
| 1 | Hypothesis log with falsification dates | 1h | High | **implementing today** |
| 2 | Source reliability auto-scoring | 1.5h | High | **implementing today** |
| 3 | Volume-weighted FM index | 1h | High | **implementing today** |
| 4 | Methodology delta auto-proposal | 0.5h | High | **implementing today** |
| 5 | Chinese / Korean / Japanese source instruction in prompt | 0.3h | Medium | **implementing today** |
| 6 | Tier-1 confidence floor + abstention rule | 0.7h | Medium | **implementing today** |
| 7 | Regime-conditional trend test | 3h | High | Phase 2 |
| 8 | Markov chain on Three Waves | 8h | High | Phase 2 |
| 9 | AIS data integration (MarineTraffic via prompt) | 0.5h | Medium | **implementing today** |
| 10 | Outcome-distribution mapping for Wave Intensity | 4h | High | Phase 2 |
| 11 | Causal DAG framework (Pearl) | 12h | Medium | Phase 3 |

---

## 10. What I'm not implementing today (and why)

- **Full Markov chain on Three Waves.** Requires comparable-historical-event database I don't yet have. Recommend Phase 2.
- **Lloyd's List Intelligence AIS** — paid. Workaround: free MarineTraffic via prompt.
- **Causal DAG library.** Pearl-style requires explicit graph + intervention variables. Too heavy for this build; Phase 3.
- **Translation pipeline for Chinese/Korean/Japanese primary sources.** Requires either Anthropic translation calls or external service. Defer; system prompt now directs the model to query Chinese-language outlets when a Chinese operator is the topic, relying on Claude's multilingual capability rather than a separate pipeline.

---

## 11. Audit delta log

- 2026-05-16 — initial audit (Day 78). 7 findings, 11 ranked upgrades. 7 of 11 implementing today.
