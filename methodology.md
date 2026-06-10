# Methodology — Force Majeure Tracker

**Status:** Internal operating manual. The public site shows only a meta-paragraph; this file stays in the repo for the daily updater and for any team member building on the work.

**Anchor date:** Day 1 = 28 February 2026 (Ras Laffan QatarEnergy FM declaration).

---

## 1. Signal tier weights

Every input is graded before it can move the assessment. The weights compound — three Hard signals in 72h is qualitatively different from thirty Soft mentions.

| Tier | Weight | Examples | Move-the-needle authority |
|---|---|---|---|
| **Hard** | ×5 | Verified physical event with operator confirmation; official FM letter on file; primary regulator statement; AIS-confirmed shutdown; first-party Tadawul / SEC / company press release | Yes — required to move Wave Intensity |
| **Medium** | ×3 | Order from authorised voice not yet executed (e.g., declared intent to restart); industry trade press confirmation citing two independent operators; specialised commercial intelligence with multi-year track record (Argus, ICIS, Platts, OPIS, Chemical Week, Lloyd's List) | Yes — can move trend, not Wave Intensity alone |
| **Soft** | ×1 | Statements not yet acted on; analyst commentary; broker letters; secondary regional press | Trend modulation only |
| **Noise** | ×0 | Anonymous OSINT; op-eds; AI-generated summaries; social media without primary corroboration | Excluded from scoring |

**Tier-1 floor rule.** No public claim is published as Hard unless a Tier-1 source confirms. If only Tier-2/3 sources are available, the claim is published as Medium with the source named.

## 2. Trend rule (trailing 72h vs prior 72h)

- **Worse** — ≥2 Hard escalation events with no offsetting Hard de-escalation, OR 1 regime-change event (formal multi-year FM, sovereign-level allocation, restart-type "even when reopened" language).
- **Same** — mixed Hard signals OR no Hard signals.
- **Better** — ≥1 Hard de-escalation event (formal restart, FM rescinded, vessel transit resumed at ≥80% baseline) AND no offsetting Hard escalation.

The 72h window is fixed and aligns with the 3-day update cadence — each run compares the last 72h to the 72h before that. Don't stretch the window to find a trend that isn't there.

## 3. Wave Intensity scale (1–5)

Renamed from "Threat" because the FM space already has a measure of severity — propagation through Marco Felsberger's Three Waves model. Each level has the same operative test in both criteria and trigger language.

| Level | Label | Operative test |
|---|---|---|
| **L1** | Watch | Scattered Wave 1 production-side FMs (≤3 in 7d, single root cause), no cross-chain propagation observed. |
| **L2** | Elevated | Confirmed Wave 1 cluster (≥4 production-side FMs in 7d across ≥2 commodity chains), Wave 2 not yet observed. |
| **L3** | Cascade | Wave 2 confirmed — downstream feedstock-starvation FMs in ≥2 commodity chains within 14d of the Wave 1 cluster. |
| **L4** | Systemic | Wave 3 cascade FMs observed (PVC, EDC, MEG, PET — third-order chains) AND ≥1 restart-type FM with "even when reopened" language (KPC FM2 pattern). |
| **L5** | Regime | Physical-absence FMs dominate the 7d window; multi-quarter rebuild timelines confirmed in primary filings (Tadawul "cannot estimate return", QE 5-year contract FM); spot-market substitution structurally insufficient. |

**Boundary discipline.** A move from LN to LN+1 requires the LN+1 operative test to pass on Hard signals only. Wave intensity does not climb on Soft input.

## 4. Three Waves model — the FM-specific engine

This is the analytical frame the Wave Intensity scale rides on. Source: Felsberger FM tracker, Day 1–55 empirical pattern.

- **Wave 1 — physical / price.** FMs at the production-side root cause. Producer cannot deliver because the asset is offline (kinetic damage, allocation order, feedstock cut). Examples: QatarEnergy Ras Laffan, Sadara Jubail full shutdown, EGA Al Taweelah strike, ALBA Sitra. Time-to-FM from event: hours-to-days.
- **Wave 2 — allocation.** FMs at midstream / shipping / contract level. The producer's customers cannot get product because logistics or contracts collapse. Examples: Shell Qatari LNG cargoes #1–4, Petronet LNG, Fujairah bunker suppliers, MSC / Hapag / Maersk / CMA CGM container suspensions. Time-to-FM from Wave 1: 3–10 days.
- **Wave 3 — physical absence.** FMs at downstream feedstock chains. Crackers and converters cannot run because their feedstock has dried up upstream. Examples: Yeochun NCC, LG Chem, Lotte, Mitsui, Wanhua, Sumitomo Asia, TPC Singapore, Formosa. Time-to-FM from Wave 2: 7–21 days. Restart-type FMs ("even when Strait reopens") appear at the back of this wave.

**Empirical signature (Day 1–55):** 92 Wave 1, 14 Wave 2, 7 Wave 3 cumulative. Day-11 spike (13 FMs in one day) marked the Wave 1 → Wave 2 transition. Wave 3 cascade-derivative tail still propagating at Day 70.

## 5. FM type taxonomy (six categories)

Used in the FM type distribution chart and in the daily updater's classification step.

1. **Production (physical)** — producer asset offline. Root-cause FM.
2. **Shipping / logistics** — carrier or terminal cannot move the cargo.
3. **Downstream feedstock** — converter cannot operate without its input.
4. **Distribution** — wholesale / retail allocation FM (e.g., Airgas helium).
5. **Restart / forward-coverage** — second FM declared to ration physical output at restart, even after a partial reopening.
6. **Cascade / derivative** — political / market-wide statements with operational consequences (e.g., Lufthansa fleet grounding, Iran "completely open" retraction).

## 5b. Two-tier indicator framework — strong vs confirmatory signals  *(added Day 81)*

**Posture.** Repeatable, auditable, falsifiable. Every row in `events.csv` carries an `indicator_class` and a `tier`. The framework is information-theoretic: a signal's value scales with prior unlikelihood under "no crisis." Strong signals are formal, attributable, verifiable. Confirmatory signals reinforce rather than initiate.

### Tier 1 — strong signals (high information value)

**Admissibility — ALL four conditions must hold:**

- **T1 · First-party authority.** Operator press release / customer letter / exchange filing (Tadawul, SEC 8-K, KRX, BSE/NSE, SGX, LSE), OR named sovereign regulator (OFAC, FAA, EASA, national CAA, UKMTO, MARAD, ECHA, FDA, EMA, ANSM), OR multilateral body with treaty backing (IEA, IATA shortage list).
- **T2 · Stable document identifier.** Unique reference exists: 8-K accession, Tadawul filing ref, NOTAM number, CZIB ref, MSCI/NAVTEX advisory number, OFAC SDN entry, Federal Register notice, IEA release URL.
- **T3 · Concrete actionable content.** States at least three of: specific volume / capacity, effective and / or expiry dates, named parties, mechanism (FM clause invoked, regulation cited).
- **T4 · Empirically predictive lead.** Either (a) causes a measurable market reaction within 72h (price > 2σ, transit-pattern change, derivative cascade), OR (b) has historical analog where same-class signals preceded downstream Hard outcomes by ≥24h (2019 Norfolk/Mesdar, 2022 Ukraine ammonia, 2024 Red Sea Houthi).

**Decision rule:** 4 of 4 → Tier 1. 2–3 of 4 → Tier 2. 0–1 of 4 → reject (Noise).

**Tier 1 indicator classes** — `FM` · `Restart` · `NOTAM` · `NAVTEX` · `Sanction` · `Reserve` · `Regulatory`

### Tier 2 — confirmatory indicators (supporting, market-reactive)

**Admissibility — ALL three must hold:**

- **S1 · Named source.** Identifiable author or organisation; no anonymous OSINT.
- **S2 · Reproducible publication.** Citeable URL or document.
- **S3 · Topical relevance.** Direct relevance to Hormuz crisis OR causally linked supply-chain disruption.

**Tier 2 indicator classes** — `Insurance` (premium quotes, market reaction — JWC formal listing is Tier 1) · `Industry` (Cefic, IATA, ICCA, LMA, sell-side statements) · `Geopolitical` (sovereign statements not yet binding) · `Carrier-advisory` (airline route cuts — distinct from regulator NOTAMs) · `Analyst` (named analysts with multi-year track records)

### Tier 3 — excluded entirely

Anonymous OSINT · op-eds without primary citation · single-source uncorroborated claims · AI-summarised aggregator output without primary verification.

### Audit requirement

Every Tier 1 row's `source` + `notes` must visibly defend T1–T4. Every Tier 2 row must defend S1–S3. Rows that fail audit get demoted (T1→T2→reject) with the reason logged in `count-log.md`.

### Dashboard separation

The dashboard shows two distinct counts:

- **Strong signals** = `tier == 1`. The headline crisis-state indicator.
- **Confirmatory indicators** = `tier == 2`. Supporting context.

Total events in events.csv = T1 + T2. The two-count display prevents Tier-2 inflation from masquerading as Tier-1 signal.

### Scientific grounding

- **Information theory (Shannon).** I(x) = −log₂(P(x)). Formal first-party actions have priors ≈ 10⁻³ per operator-day under normal conditions; analyst opinions ≈ 10⁻¹. Per-signal information differs by an order of magnitude. Tier separation matches this hierarchy.
- **Bayesian likelihood ratio.** Tier 1 events typically carry LR > 5 for predicting downstream Hard outcomes; Tier 2 events carry LR ∈ [1.5, 5]. Tier 3 noise has LR < 1.5 — rejected to keep posteriors clean.
- **Observability (MIT control-theoretic).** Every Tier 1 signal must be independently observable at the time of issue (NOTAMs are public-by-construction; premium quotes pass through brokers; FMs are operator-issued). This is the systems-engineering requirement: only observable signals enter the estimator.
- **Institutional authority (Harvard policy).** Authority traces to a legal / institutional source. Tadawul = exchange listing rule. OFAC = US Treasury executive authority. NOTAM = national CAA regulatory authority. Tier 1 admission requires legal force behind the issuer.
- **Network centrality (Santa Fe Institute).** Some events have outsized cascade-prediction power because of node centrality in the supply graph. Volume-weighted FM index (audit Section 9.3) operationalises this — Tier 1 events are weighted by capacity impact, not just count.

### Repeatability check

Two analysts applying T1–T4 / S1–S3 to the same candidate should reach the same tier ≥ 90% of the time. Disagreements arbitrated in `count-log.md`; recurring patterns update the operative definitions (the framework self-improves via the same reflection loop).

## 6. Anti-bias defaults

- **Base rates first.** What does the historical FM frequency for this commodity / operator look like? An ICIS announcement of a feedstock issue is not surprising in March 2026; it is in March 2024.
- **Convexity beats consensus.** A 5% chance of Strait formal closure pricing-out aluminium for 90 days matters more than a 60% chance of a 5% premium. Hunt asymmetric tails.
- **Lindy on tensions, anti-Lindy on novelty.** A 60-day-old pattern (FM cascade through Asian crackers) tends to keep going. A novel pattern (sovereign-level FM language, "even when reopened") deserves anti-Lindy scepticism on durability — but heavy weight on direction.
- **No news ≠ no event.** Day-counter helps: at Day 71 a quiet 24h is not the same as Day 11. Wave 3 cascade FMs surface in trade press 1–3 weeks after the operational decision.
- **Asymmetric updating (Popper).** Falsifying observations (FM rescinded, train restart confirmed) move the Wave Intensity faster than supporting observations move it. Be willing to climb down.
- **No hindsight reframing.** The brief written on Day 11 stands. Don't retcon "we expected this" into Day-12 language. The backtest log scores the actual prediction made.
- **Authority-bias check.** A central bank, a regulator, or a sovereign-owned producer does not get a free pass to Hard tier. Apply the same operator-confirmation test.

## 7. Self-learning loop  *(rebuilt Day 78 per `methodology-audit.md`)*

The loop has four mechanisms now. The first three are file-based logs the updater writes to on every run; the fourth is an auto-trigger for rule changes.

1. **Backtest scoring** — `backtest-log.md`. Every brief makes 3 actions, 5 watchlist items, 3 scenarios. T+1 / T+3 / T+7 scoring with explicit Hit / Miss / False alarm / Surprise. Weekly Brier on scenarios — trend toward 0 = calibration improving.
2. **Reflection** — `reflection-log.md`. Every run produces what surprised the system, which rule was tested, what should change next run. Concrete and testable wording required.
3. **Hypothesis log** *(new, Day 78)* — `hypothesis-log.md`. Every run generates 2–4 falsifiable hypotheses with explicit stop-out dates and discriminating observables. On each run, expired hypotheses are resolved and the resolutions update the scenario priors. The Popperian leg of the methodology.
4. **Source reliability auto-scoring** *(new, Day 78)* — `source-reliability.md`. Maintained automatically. Sources falling below 0.6 hit rate over 4 weeks are demoted one tier; sources surfacing primary documents 24h ahead of peers are promoted. The decision is proposed by the updater, listed under "Pending tier changes", and applied after one calendar week's review.
5. **Methodology delta auto-proposal** *(new, Day 78)* — when (a) Miss rate > 30% in any category over the last 4 backtest entries, OR (b) a prior reflection recommendation has been outstanding ≥ 2 runs without being applied, OR (c) an audit finding with status "implementing today" hasn't landed in this file yet, the updater MUST emit a `METHODOLOGY_DELTA` block. The script appends it to this file with date + provenance. This is the mechanism that prevents reflections from staying on the page without changing the rules.

Every change to this file should originate from one of these four mechanisms. The chain of provenance is: observation → reflection / hypothesis resolution → delta proposal → applied delta.

## 8. Stop conditions

- Insufficient Tier 1–3 input → write thin INTERIM brief, flag it on the masthead, never publish unsourced claims as Hard.
- Source-tier conflict (Tier 1 contradicts Tier 2) → publish the Tier-1 reading and name both sources in `sources.md` for follow-up.
- Wave-intensity move without Hard signal → don't publish the move; explain the Soft-tier signals in the watchlist instead.
- **Tier-1 confidence floor (added Day 78 per audit).** Per category: if `(Tier-1-hits × source-diversity) < 2`, publish that category as "INSUFFICIENT — gap: [named]" rather than filling. The model must be willing to fail a section rather than pad.
- **De-anchor check (added Day 78).** Every 4th run, attempt to argue Wave Intensity should *change*. Require Hard signals to confirm continuation at current level. Document the argument in REFLECTION.

## 9. Output checklist (every brief)

- [ ] Trend (Worse / Same / Better) with confidence
- [ ] Wave Intensity (1–5) with confidence
- [ ] One-liner today summary (≤25 words)
- [ ] 6-tile status board, each tile has badge + 3-bullet body
- [ ] Map pins synced to current FM status
- [ ] 3 actions, operational verbs
- [ ] 5 watchlist items, each with deadline + directional implication
- [ ] 3 scenarios, probabilities sum to 100, each has observable
- [ ] Recent FM declarations table (last 14d)
- [ ] Cascade timeline T+0 / T+7 / T+30 / T+90
- [ ] Yesterday's predictions scored before drafting today's

---

**Methodology delta log**

- 2026-05-10 — initial version. Wave Intensity 1–5 scale, six FM categories, Three Waves engine. Anchor: Day 1 = 28 Feb 2026.
- 2026-05-16 — Day-78 audit (`methodology-audit.md`). Added: Tier-1 confidence floor (Section 8), de-anchor check (Section 8), self-learning loop overhaul (Section 7) — added hypothesis log, source reliability auto-scoring, and methodology delta auto-proposal. Source coverage expanded with Chinese / Korean / Japanese primary outlets, SEC EDGAR 8-K, ECHA, FAA/EASA airworthiness directives, and free-tier AIS via MarineTraffic. Future-deltas to this file will be auto-appended by the updater per Section 7.5.

**Trigger assessment (3 conditions for methodology delta proposal):**

1. **Miss rate >30% in Actions/Watchlist/Scenarios over last 4 backtest entries:** Not available (only 1 backtest entry in log so far, Day 81 initialization). No miss rate computed; pass trigger.

2. **Outstanding reflection recommendation ≥2 runs without application:** Only 1 reflection entry (Day 81); no prior recommendations outstanding. No trigger.

3. **Audit finding with "implementing today" status in methodology-audit.md:** No audit findings documented yet (tracker bootstrap, Day 71–81). No trigger.

**Conclusion:** No methodology delta warranted at Day 81. System is in initialization phase; one complete backtest cycle (Day 71–85) needed before reliability patterns emerge. Next review opportunity: Day 85–88 (post-T+3 horizon closure).

**Methodology delta 19 May 2026 (Day 81).** Section 2, Trend rule: add definition of regime-change signals and their interaction with operator FM escalation.

**Old rule (Summary):** Worse — ≥2 Hard escalation events OR 1 regime-change event (formal multi-year FM, sovereign-level allocation, restart-type "even when reopened" language).

**New rule:** Worse — (≥2 Hard escalation events in trailing 72h) OR (1 regime-change event AND ≥1 Hard operator FM escalation within same 72h or preceding 7 days) OR (1 restart-type FM extends past stated horizon).

**Reason:** Iran IRGC "vast operational area" redefinition (15 May, Tier 1) is a regime-change signal but did NOT move Trend Worse because no accompanying operator FM escalation occurred in the same 72h window. The old rule required only the regime-change signal. The new rule clarifies: regime-change signals (institutional redefinitions, sovereign control claims) harden boundary conditions (L4→L5) but do not move Trend without operator FM validation. This prevents false-Worse signals from geopolitical noise and focuses Trend on measurable operator impact. The boundary test (L4→L5) will use regime signals as a precondition: if a restart-type FM extends AND IRGC operational expansion is in place, then L4→L5. **Effective immediately; applies to next brief (Day 84, 22 May 2026).**

None. 

The prior run's Hard signal rule, Trend rule, Wave Intensity rule, and scenario probability logic all held up under Day 82's test (no new Hard escalations, Soft signals validated, Lotte on track, no surprise outcomes). No miss rate in Actions/Watchlist/Scenarios exceeds 30% threshold over rolling 4-run window. No reflection recommendation from Day 81 has aged beyond 2-run implementation window without being applied (H-006 resolution on Lotte was tracked and hit). No audit finding from methodology-audit.md is pending "implementing today" status.

Therefore: **No methodology delta triggered.**

**Methodology delta 2026-05-20 (Day 82).**

**Condition triggered:** Reflection log recommendation from Day 81 (not prior backtest miss, but forward-improvement signal). Recommendation: "Add secondary watchlist metric for administrative toll system stability." Applied today.

**Change:** Methodology section 4.2 (Watchlist design) — added new guidance: "Secondary metrics for chokepoint shifts. When primary signal (kinetic closure) transitions to secondary chokepoint (administrative toll regime), define quantitative stability thresholds: e.g., permit-dispute rate, seizure frequency, toll-variance coefficient. If >1 threshold breached 2 consecutive weeks, escalate signal to Type 4 Cascade (administrative breakdown = kinetic risk resurging)." 

**Rationale:** PGSA formalization on Day 82 created a regime shift from kinetic (IRGC shooting) to administrative (PGSA toll-vetting). The prior methodology was designed for kinetic events. The watchlist now needs quantitative guardrails for the new regime. Without them, administrative system degradation (e.g., 5 seizures/week due to bilateral disputes) would not trigger escalation flags until kinetic attacks restarted. Adding this rule closes the gap.

**Impact:** Watchlist #3 (today's brief, under ACTIONS) already includes ">1 seizure/week" escalation condition, so the change is partly forward-looking. Methodology now explicitly permits auxiliary metrics for regime-dependent choke-point monitoring.

**Methodology delta YYYY-MM-DD (Day N):**

**Delta 2026-05-22 (Day 84).** Methodology.md § 2 (Trend rule, trailing 72h vs. prior 72h): Add clarification on "Hard signal" definition to exclude sovereign regulatory announcements that are not operator-declared force-majeure. The PGSA toll regime is a Tier 1 sovereign policy signal but not a classical "Hard operator FM." Recommend: (a) maintain current Trend rule (requires Hard operator FM for trend shift); (b) add secondary Wave Intensity rule (§ 3.3, new): "Sovereign administrative control milestones (e.g., formalization of permanent toll regime, sanctions regime formalization, blockade institutionalization) are Wave Intensity *modifiers* that can extend forecast timelines by +30 to +90 days without moving Wave Intensity level, unless paired with new restart-type FM or maritime operator Type 4 FM."

**Reason:** The PGSA toll regime formalization on 18 May is a policy-level constraint that is durable and structural (expected to persist through 2027 at 35–40% probability), but it is not an operator FM. The current methodology treats all Tier 1 signals equally, which under-weights policy regime shifts. Amend § 3 to accommodate policy-level constraints as a separate category of leading indicators.

**Effective:** Day 85 (23 May 2026), pending review.

## 2026-06-01 (Day 94) · Methodology Delta

**Condition for change:** (a) Miss rate > 30% in any category over last 4 backtest entries; (b) Reflection recommendation outstanding ≥2 runs; (c) Audit finding with Status "implementing today."

**Trigger present:** Condition (b) — Reflection from Day 94 recommends introducing **Tier-2.5 "Verbal assurance (third-party contingent)"** subcategory to flag Bessent 28 May Oman reassurance as pending third-party confirmation. This requires methodology.md clarification.

**Proposed delta:**

**Methodology.md § Signal Tier Weights, subsection "Medium (×3)" — ADD:**

> Tier-2.5 (special case): Verbal assurance of action by a third party (e.g., Treasury official claiming country X will not participate in toll system, without country X's public confirmation). These signals carry the full 3× weight of Tier-2 IF accompanied by a stop-out date (e.g., "by 5 June Oman must publicly confirm"), otherwise downgrade to Tier-3 and flag in WATCHLIST as "pending third-party confirmation."

**Reason:** Bessent 28 May statement (Oman will not toll) lacked Oman confirmation and created over-confidence in de-escalation signal. The methodology should formalize the rule: verbal assurances from intermediaries are Tier-2 only if confirmable within 72h; otherwise they are Tier-3 rumors.

**Status:** Implementing today (Day 94 brief).

**Proposed Methodology Delta:** Wave 3 Cascade-Tail Temporal Refinement.

**Section 2, Rule B (Trend rule):** Add subclause for Wave 3 plateau detection.

**[Old]:** "Worse — ≥2 Hard escalation events with no offsetting Hard de-escalation, OR 1 regime-change event (formal multi-year FM, sovereign-level allocation, restart-type 'even when reopened' language)."

**[New]:** "Worse — ≥2 Hard escalation events with no offsetting Hard de-escalation, OR 1 regime-change event (formal multi-year FM, sovereign-level allocation, restart-type 'even when reopened' language). **Caveat:** Wave 3 cascade tail (Days 35+) may plateau on Soft signals (Type 4 distribution cost, Type 6 derivative/substitution) without triggering new Hard FMs for 8–12 weeks if industry successfully substitutes and absorbs costs. Trend remains Same during plateau phase unless new Hard FM or restart-type FM surfaces or Soft-signal 4-week acceleration rate exceeds 20% (bunker cost, shipping surcharge, or port dwell time)."

**Reason:** Day 97 testing shows the cascade tail can sustain Soft signals (bunker $800/mt, shipping surcharge, naphtha substitution) without Hard re-escalation. The prior methodology assumed exponential escalation; evidence suggests equilibrium is possible. This refinement prevents false Trend escalations on Soft signals alone, while preserving sensitivity to real Hard-FM or acceleration-rate triggers.

**Section 3, Rule C (Wave Intensity boundary):** Add substitution lock-in as L4→L5 boundary test.

**[Old]:** "Boundary test for L4→L5: (a) maritime operator Type 4 FM, OR (b) KPC/SABIC extension past 1 June, OR (c) Iran-Oman toll-framework public signature. None triggered by 1 June. L4 Systemic maintained."

**[New]:** "Boundary test for L4→L5: (a) maritime operator Type 4 FM, OR (b) restart-type FM count ≥5, OR (c) substitution pathway lock-in (≥2 major long-term contracts signed at >10% premium, K/J LNG or Indian/Thai naphtha, by 30 June). If (c) triggers without (a) or (b), designate as 'L5 Regime emerging via structural reallocation' — not L5 Systemic escalation, but permanent supply shift away from Persian Gulf. This captures the market's organic pivot away from Hormuz, independent of Strait reopening."

**Reason:** Day 97 evidence (Thai diversification, Chinese styrene surge, US LNG buyer hedging) shows the market is already realloc away from Middle East supply, even while Strait remains under PGSA control. The Three Waves model missed this structural mechanism. Adding substitution lock-in as a L4→L5 test captures the real regime shift (permanent supply reallocation) vs. the tactical FM escalation model (new Hard FMs).

**Status:** Pending implementation. Recommend live testing on 30 June data (K/J LNG contract signatures, Indian/Thai cracker deals) to validate substitution lock-in as predictive boundary.

## Methodology Delta Log

**Proposed Delta 2026-06-07 (Day 100):**

**Section 2 (Trend rule), new sub-rule:**

"Restart-type FM lifts (Type 5 FMs ending) do not modify Trend. A Type 5 FM ending (e.g., Formosa olefins FM lift, 3 June) is a Wave 3 tail attenuation signal and feeds Scenario A confidence; it does not constitute a Hard de-escalation event for Trend purposes. Trend moves only on production-side FM changes (Type 1 onset / extension) or regime-change escalations. Restart-type FM lifts inform Wave Intensity boundary tests and scenario probabilities, not Trend."

**Reason:** Backtest finding. Day 100 FPCC FM lift (Type 5 Restart) was correctly classified as non-Trend-moving in this run, but future runs may misclassify. Clarifying the rule prevents confusion: "FM ended" ≠ "escalation reversed." Restart-type FMs are multi-quarter recovery signals; their lift is normal Wave 3 progression, not de-escalation. This change formalizes the distinction for operational clarity.

**Status:** Pending implementation in next version (Day 103, 10 June 2026).

## 2026-06-10 (Day 103) · Methodology Delta

**Status: No methodology delta proposed.**

Trigger-check (from §33d):
- Miss rate (Actions / Watchlist / Scenarios) over last 4 backtest entries: only 1 backtest entry available (Day 103); cannot compute 4-entry rolling rate. No delta triggered.
- Prior reflection recommendations outstanding ≥2 runs: first brief in the series (no prior outstanding items). No delta triggered.
- Audit findings with "implementing today" status: none referenced in current brief. No delta triggered.

All three trigger conditions are clear. No methodology delta is warranted this cycle.
