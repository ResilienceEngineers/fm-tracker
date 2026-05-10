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

## 6. Anti-bias defaults

- **Base rates first.** What does the historical FM frequency for this commodity / operator look like? An ICIS announcement of a feedstock issue is not surprising in March 2026; it is in March 2024.
- **Convexity beats consensus.** A 5% chance of Strait formal closure pricing-out aluminium for 90 days matters more than a 60% chance of a 5% premium. Hunt asymmetric tails.
- **Lindy on tensions, anti-Lindy on novelty.** A 60-day-old pattern (FM cascade through Asian crackers) tends to keep going. A novel pattern (sovereign-level FM language, "even when reopened") deserves anti-Lindy scepticism on durability — but heavy weight on direction.
- **No news ≠ no event.** Day-counter helps: at Day 71 a quiet 24h is not the same as Day 11. Wave 3 cascade FMs surface in trade press 1–3 weeks after the operational decision.
- **Asymmetric updating (Popper).** Falsifying observations (FM rescinded, train restart confirmed) move the Wave Intensity faster than supporting observations move it. Be willing to climb down.
- **No hindsight reframing.** The brief written on Day 11 stands. Don't retcon "we expected this" into Day-12 language. The backtest log scores the actual prediction made.
- **Authority-bias check.** A central bank, a regulator, or a sovereign-owned producer does not get a free pass to Hard tier. Apply the same operator-confirmation test.

## 7. Learning loop (private)

- **T+1, T+3, T+7 prediction scoring.** Every brief makes 3 actions, 5 watchlist items, 3 scenarios. Each item is scored Hit / Miss / False alarm / Surprise on the relevant horizon. Logged in `backtest-log.md`.
- **Per-run reflection.** Every updater run produces a `REFLECTION` block: what surprised it, which rule was tested, what changes next run. Logged in `reflection-log.md`. The reflection must be concrete and testable — "promote Polymerupdate to Tier-1 for European cascade" beats "consider broader sources."
- **Friday Brier on scenario probabilities.** Weekly Brier score logged. Trend toward 0 = calibration improving.
- **Source reliability tally.** Tier-2/3 sources tracked for hit rate. A source dropping below 0.6 hit rate over 4 weeks is downgraded; one consistently surfacing primary documents 24h ahead of peers is promoted.
- **Methodology delta log.** Every change to this file is dated with a one-line reason. Most deltas should originate from a reflection entry — that is the chain of provenance.

## 8. Stop conditions

- Insufficient Tier 1–3 input → write thin INTERIM brief, flag it on the masthead, never publish unsourced claims as Hard.
- Source-tier conflict (Tier 1 contradicts Tier 2) → publish the Tier-1 reading and name both sources in `sources.md` for follow-up.
- Wave-intensity move without Hard signal → don't publish the move; explain the Soft-tier signals in the watchlist instead.

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
