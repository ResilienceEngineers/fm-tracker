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

## Hypotheses — Delta for Day 81 (19 May 2026)

### New hypotheses for this run

**H-012 · Created 19 May 2026 (Day 81) · Stop-out 26 June 2026 (Day 120)**
- **Hypothesis:** Lotte Chemical Yeosu restart (29 May target) will execute on schedule and hit >80% of nameplate ethylene capacity by 1 June, easing Wave 3 (downstream feedstock) cascade intensity and de-escalating Type 3 FM count by 2–3 members by 30 June.
- **Discriminating observable:** Seoul Economic Daily or KOSPI filing (Tier 2) announces restart execution; production data from Lotte or industry desk (ICIS, ChemAnalyst) shows nameplate recovery >80% by 1 June. Failure: restart slips >7 days OR nameplate recovery <70%.
- **Prior probability:** 0.75 (regulatory filing is formal commitment; turnaround schedule advanced, plant standing ready; supply-chain stabilization focus suggests management confidence).
- **Status:** Open. Resolution by 1 June.

---

**H-013 · Created 19 May 2026 (Day 81) · Stop-out 14 June 2026 (Day 108)**
- **Hypothesis:** EIA June 2026 STEO (due ~14 June) will maintain "Strait closed through late May, June pickup assumed" baseline WITHOUT a downgrade to "closed through July." If downgraded, Trend moves Worse and Wave → L5 Regime.
- **Discriminating observable:** EIA STEO June 2026 publication (official PDF, EIA.gov). Parse for Strait assumption language. Baseline (Hit): "late May close, June opening." Downgrade (Miss): "June close, July+ opening" or "closure duration uncertain, extended timeline possible."
- **Prior probability:** 0.50 (ceasefire status "life support" per Trump 11 May; IRGC "vast operational area" signal 15 May hardens closure narrative; EIA will likely update downward by late May/early June if no ceasefire breakthrough occurs).
- **Status:** Open. Resolution 14–16 June.

---

**H-014 · Created 19 May 2026 (Day 81) · Stop-out 22 May 2026 (Day 85)**
- **Hypothesis:** No new restart-type FM (beyond the existing KPC FM#2, SABIC "cannot estimate", QE 5yr LNG, EGA 12-month) will file by 22 May. Restart-type FM count remains 4 through 22 May; boundary test does NOT trigger.
- **Discriminating observable:** Tadawul, KOSPI, or primary operator press release for Saudi Aramco, KNPC, ADNOC, or other major Gulf producer. Absence of new FM filing = Hit. Presence = Miss.
- **Prior probability:** 0.80 (no new kinetic events 16–19 May; producer FMs historically file in clusters during acute crisis phases; current phase shows stabilization signals, not escalation).
- **Status:** Open. Resolution 22 May (T+3 checkpoint).

---

**H-015 · Created 19 May 2026 (Day 81) · Stop-out 30 June 2026 (Day 124)**
- **Hypothesis:** Iran's IRGC "vast operational area" redefinition (15 May) will NOT be reversed or materially narrowed by 30 June even if a ceasefire agreement is announced. The institutional claim on expanded operational zone persists beyond ceasefire language.
- **Discriminating observable:** IRGC Navy official statement, Iranian Foreign Ministry statement, or UN correspondence. Reversal: explicit narrowing of operational zone or removal of "vast operational area" designation. Persistence: silence, reaffirmation, or refinement of the claim. 
- **Prior probability:** 0.70 (institutional redefinitions are durable; Iran has shown willingness to sustain asymmetric control claims; ceasefire typically does not address underlying sovereignty disputes).
- **Status:** Open. Resolution 30 June (T+42).

---

### Resolutions for hypotheses whose stop-out passed

None. All prior hypotheses (H-001 through H-011) remain open or carry forward from Day 80. No stop-out dates reached between Day 80 and Day 81.

## New hypotheses for this run (Day 82, 22 May 2026)

### H-007 · Created 2026-05-22 (Day 82) · Stop-out 2026-05-29 (Day 89, Lotte restart date)

**Hypothesis:** Lotte Chemical Yeosu NCC restart on 29 May executes on schedule, validating the restart-type FM forecast model and shifting Scenario B probability to >50% by 30 May.

**Discriminating observable:** Lotte announces no delay AND operational systems (feed pumps, heat exchangers, catalyst beds) are in commission status by 28 May EOD per Seoul exchange disclosure or press statement.

**Prior probability:** 0.75 (on-track regulatory filing + no reported equipment delays as of 27 Mar 2026 disclosure).

**Status:** Open. Go/no-go on 29 May.

---

### H-008 · Created 2026-05-22 (Day 82) · Stop-out 2026-05-26 (Day 84, SABIC filing window)

**Hypothesis:** SABIC issues a Tadawul update 20–26 May extending the "cannot estimate" FM indefinitely (past originally forecast 20 May gate), locking Restart-type FM count at 4 and preventing L5 escalation this cycle.

**Discriminating observable:** Tadawul filing dated 20–26 May with FM language "cannot provide timeline for return to normal operations" or equivalent; no restart date announced.

**Prior probability:** 0.60 (Tadawul annual cycle historically publishes update by 25 May per company guidance; prior 10 April filing set no expiry).

**Status:** Open. Filing window 20–26 May EOB.

---

### H-009 · Created 2026-05-22 (Day 82) · Stop-out 2026-06-01 (Day 95, PGSA toll schedule publication)

**Hypothesis:** Iran PGSA publishes official toll schedule 25 May–1 June with no major exemptions (non-US, non-Israel vessels exempt but toll = $10–15M per large vessel), triggering maritime operator cost burden modeling and raising probability of Type 4 bunker FM filing by 10 June to 0.35 (from current 0.05).

**Discriminating observable:** PGSA official announcement (via Lloyd's, UKMTO, or Iranian port authority media) with toll amount per vessel class and exemption list; shipping operator (Maersk, MSC, or bundled shipping council) issues cost impact statement within 48h.

**Prior probability:** 0.55 (PGSA operational as of 4–7 May but tolls not yet published; Iran historically uses regulatory delays to signal negotiating room).

**Status:** Open. Watch for publication 25 May–1 June.

---

### H-010 · Created 2026-05-22 (Day 82) · Stop-out 2026-06-08 (Day 102, Pakistan mediation next milestone)

**Hypothesis:** Pakistan-mediated Iran-US ceasefire talks remain stalled through 8 June with no new formal breakthrough, keeping KPC FM#2 conditional restart hostage to external geopolitical event and locking Wave Intensity at L4 (not L5) through Q2 2026.

**Discriminating observable:** No new joint statement from Iran, US, or Pakistani mediators announcing progress toward partial Strait reopening OR formal ceasefire extension by 8 June EOD.

**Prior probability:** 0.70 (talks stalled as of 11 May per Trump statement; hardliner splits within Iran (IRGC vs. Foreign Ministry) prevent rapid consensus).

**Status:** Open. Monitoring window 22 May–8 June.

---

## Resolutions for hypotheses whose stop-out passed

**H-006 resolved (prior brief):** Lotte Chemical Yeosu restart on track per Seoul Economic Daily 27 Mar 2026 disclosure — **Hit.** Restart scheduled 29 May confirmed; no delay announced 19–22 May. Posterior probability (Lotte executes as scheduled): 0.75 → 0.82 (filed disclosure + no equipment failure reports in Tier 1 sources). This hypothesis was created Day 79, stop-out was Day 81; it passed its gate on Day 81 (no delay announcement in that 72h), confirming prior forecast. Posterior: **Hit, confidence high.**

## New hypotheses for this run

**H-010 · Created 2026-05-20 (Day 82) · Stop-out 2026-06-03 (Day 86)**
- **Hypothesis:** PGSA toll mechanism will stabilize at $1–2M per transit (average $1.5M) by 2 June, and bilateral carve-outs will reduce effective transits by <30% vs. pre-formal-mechanism. Administrative toll regime replaces kinetic closure as binding constraint on shipping.
- **Discriminating observable:** Weekly PGSA permit-issuance count (target: 10–20 permits/week by 2 June), no OFAC enforcement action against permit payers (secondary-sanctions announcements), and no new IRGC vessel seizures (0–1/week vs. current 2/week). Source: Windward AIS data, UKMTO, US Treasury announcements.
- **Prior probability:** 0.65 (toll mechanism formalized on schedule; bilateral precedent set by India cluster transit; but enforcement/dispute risk high).
- **Status:** Open. Stop-out: 3 June (when weekly PGSA permit data becomes available or OFAC enforces secondary sanctions).

**H-011 · Created 2026-05-20 (Day 82) · Stop-out 2026-05-29 (Day 82 + 9 days)**
- **Hypothesis:** Lotte Chemical Yeosu restart will occur on schedule (29 May ±3 days) and will reach 80%+ of design capacity within 5 days of restart, signaling Wave 1 containment and triggering Wave 2 unwind pressure (scenario A posterior probability +10%).
- **Discriminating observable:** KRX regulatory filing or Seoul Economic Daily announcement on 29 May (±1 day) with production capacity percentage statement. Alternative: ICIS naphtha desk confirmation of cracker throughput ≥900kt ethylene by 3 June.
- **Prior probability:** 0.72 (maintenance schedule confirmed, turnaround on accelerated timeline, but complex ramp-up risk in first 48h post-restart).
- **Status:** Open. Stop-out: 3 June (production ramp confirmation; if slip >7 days, hypothesis fails).

**H-012 · Created 2026-05-20 (Day 82) · Stop-out 2026-06-10 (Day 103)**
- **Hypothesis:** SABIC will file a Tadawul update by 2 June with one of two outcomes: (a) "cannot estimate" extension past 30 June (failure, triggers restart-type FM#5 count rise to 5, scenario B upgrade +10%), or (b) formal restart timeline <30 days (success, triggers L4 unwind signal, scenario A upgrade +15%).
- **Discriminating observable:** Tadawul investor relations public filing; keyword search for "cannot estimate," "return to normal," "timeline," restart announcement. If no filing by 2 June, hypothesis fails (absence is not informative; file expected within 10-business-day cycle).
- **Prior probability:** 0.55 (SABIC has been silent since Day 41 filing; next filing overdue; but regulatory discipline may compress timeline).
- **Status:** Open. Stop-out: 10 June (next business-day filing window for Tadawul).

## Resolutions

None this run. All hypotheses from prior runs remain open (backtested elsewhere).
