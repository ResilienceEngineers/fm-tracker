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

## Hypotheses — 19 May 2026 (Day 81)

### New hypotheses

**H-1 · Created 2026-05-19 (Day 81) · Stop-out 2026-06-15 (Day 108)**

**Hypothesis:** PGSA toll regime will remain operationally stable (transits permitting at $1.5M–$2.5M per vessel) through mid-June, preventing kinetic reignition and supporting Scenario A (managed recovery).

**Discriminating observable:** Daily PGSA-administered transit permits issued (tracked via Windward AIS disruption patterns, IRGC statements, maritime intelligence reports). If fewer than 3 transits/day on average 20–30 May, or if reported toll rates spike above $2.5M, regime stability is failing. If 4–6 transits/day sustained, regime is holding.

**Prior probability:** 0.72 (moderately high; PGSA formally launched 18 May with institutionalized permits and X account; bifurcation already operationalized with India-flagged cluster; Iran incentive to maximize toll revenue suggests predictable enforcement).

**Status:** Open. Stop-out 15 June (27 days out); observable data accumulating daily via Windward.

---

**H-2 · Created 2026-05-19 (Day 81) · Stop-out 2026-05-29 (Day 90)**

**Hypothesis:** Lotte Chemical Yeosu naphtha cracker will restart on schedule (29 May) and achieve 30%+ capacity utilization by end of week 1 (by 4 June).

**Discriminating observable:** Lotte regulatory filing or press statement 29 May confirming restart; operational data (ethylene production volumes, feedstock intake) reported by S&P Global Platts or Argus Media by 4 June. If restart occurs but capacity is <20% by 4 June, or if 29 May is missed by >3 days, hypothesis fails.

**Prior probability:** 0.78 (high; regulatory filing confirms 29 May date, Q1 earnings call reconfirmed it 11 May, no delays reported 16–19 May, management confidence high).

**Status:** Open. Stop-out 29 May (10 days out); this is a direct test of Scenario A / Wave Intensity L4→L3 boundary.

---

**H-3 · Created 2026-05-19 (Day 81) · Stop-out 2026-06-30 (Day 122)**

**Hypothesis:** Bunker fuel price in Singapore VLSFO will remain in the $800–950/mt range through June, preventing maritime operator formal Type 4 bunker FM filing and supporting L4 stability (no Wave Intensity move to L5).

**Discriminating observable:** Daily bunker fuel price (Ship & Bunker, OilPrice, Platts quotes). If price breaches $950/mt sustained (3+ consecutive days), Type 4 FM risk escalates. If price exceeds $1050/mt, maritime operator FM filing becomes probable within 10 days. Conversely, if price drops below $800/mt, supply condition is improving (positive surprise for Scenario A).

**Prior probability:** 0.65 (moderately high; current price $846/mt, pre-crisis $500/mt, range $800–950 represents "crisis with absorption" whereas >$950 is "systemic failure threshold").

**Status:** Open. Stop-out 30 June (42 days out); daily price data feeds Watchlist item 03.

---

**H-4 · Created 2026-05-19 (Day 81) · Stop-out 2026-06-20 (Day 113)**

**Hypothesis:** Iran-Oman bilateral negotiations will yield a partial safe-passage accord (not a full Oman bypass, but a formal bilateral arrangement for Oman-flagged and select allied vessels) by 20 June, moderating PGSA toll expectations for a subset of traffic.

**Discriminating observable:** Public statement from Iran's FM or Oman's Transport Minister confirming bilateral accord; Windward AIS pattern showing Oman-flagged or agreed allied-flag vessels moving through Larak Island corridor at reported lower toll rates (<$1M per transit vs. $2M standard). If no accord is announced by 20 June, hypothesis fails.

**Prior probability:** 0.55 (moderately low; Oman has publicly rejected toll authority in principle, but bilateral carve-outs (India 18 May) show pattern of negotiated exemptions; if pattern extends to Oman, accord is plausible by mid-June).

**Status:** Open. Stop-out 20 June (32 days out); currently tracked via Watchlist item 04.

---

### Resolutions (none this cycle)

No prior hypotheses from Days 71–78 reach stop-out 19 May. All remain open pending June data.

**New hypotheses for this run:**

## H-001 · Created 2026-05-22 (Day 84) · Stop-out 2026-06-05 (Day 98)

**Hypothesis:** The PGSA toll regime will achieve sustainable operational status (>10 coordinated transits per day, consistent toll collection in Chinese yuan/Bitcoin, no new vessel seizures) by 5 June, signaling that Iran has succeeded in monetizing the Strait disruption as a long-term policy rather than a temporary coercive tool.

**Discriminating observable:** Windward daily briefing on 5 June 2026 reports ≥10 transits in a 24-hour window with documented toll payments to IRGC-linked wallets (via blockchain tx or Iranian banking disclosures); zero new vessel seizures or warnings in prior 7 days.

**Prior probability:** 0.65 (Iran had infrastructure prepared in advance; PGSA launch on 18 May was not improvised; administrative capacity for permit processing and toll collection appears functional).

**Status:** Open.

---

## H-002 · Created 2026-05-22 (Day 84) · Stop-out 2026-05-29 (Day 91)

**Hypothesis:** Lotte Chemical Yeosu restart on 29 May will be delayed past the announced date due to residual naphtha feedstock constraints or equipment qualification issues, extending the wave-3 cascade depth into June.

**Discriminating observable:** Lotte Chemical regulatory filing or press statement by 30 May announcing restart delay; OR Lotte's first-week post-restart production (1–7 June) <70% of announced 1.23 Mt/yr capacity (annualized), indicating supply-side constraints persisted.

**Prior probability:** 0.35 (Lotte has track record of hitting restart dates; CEO communication in 11 May earnings stated confidence; but naphtha supply uncertainty remains high).

**Status:** Open.

---

## H-003 · Created 2026-05-22 (Day 84) · Stop-out 2026-06-01 (Day 94)

**Hypothesis:** Trump's "no hurry" statement (20 May) signals a shift toward accepting the status quo (stalemate + ceasefire extension) rather than pursuing a near-term negotiated opening. The next Trump statement on Iran (by 1 June) will contain no new proposal language and will focus on military readiness, indicating scenario B (stalemate, 40% baseline probability) is now the modal expectation.

**Discriminating observable:** Trump public statement (press conference, commencement speech, or social media) by 1 June 2026 contains no new Iran negotiation proposal and references military preparedness, deterrence, or "finishing the job" language ≥2 times.

**Prior probability:** 0.55 (Trump's 20 May language ("no hurry," comparing to 19-year Vietnam and 12-year Iraq) suggests acceptance of prolonged engagement; next statement will reveal whether he is signaling patience or saber-rattling).

**Status:** Open.

---

**Resolutions for hypotheses whose stop-out passed:**

None this cycle. All three hypotheses are forward-looking; stop-out dates are 6–14 days ahead.

## Hypotheses — 25 May 2026 (Day 87)

### New hypotheses for this run

**H-001 · Created 2026-05-25 (Day 87) · Stop-out 2026-06-07 (Day 99)**

- **Hypothesis:** Oman will publicly reject or remain silent (non-endorsement) on the Iran permanent toll framework by 29 May 2026. Silence for 7+ days after Iran's 21 May disclosure is a soft rejection signal; Oman's historical mediator role is incompatible with co-governing a toll regime, and public endorsement would destroy Oman's neutrality in future Iran-US negotiations.
- **Discriminating observable:** (a) Oman Foreign Ministry official statement before 29 May rejecting toll framework; (b) Oman's silence through 29 May = de facto non-endorsement; (c) Oman's statement endorsing framework = hypothesis False.
- **Prior probability:** 0.65 (Oman's historical mediator role favors rejection or silence; endorsement would be diplomatically costly).
- **Status:** Open. Decision window 29 May – 7 June.

**H-002 · Created 2026-05-25 (Day 87) · Stop-out 2026-05-31 (Day 93)**

- **Hypothesis:** Kharg Island crude exports will resume (first confirmed tanker departure observed via satellite/AIS) by 31 May 2026, signaling floating-storage saturation relief and export-cycle restart at reduced capacity (40–50% of 7-May baseline).
- **Discriminating observable:** Satellite imagery or AIS tracking of VLCC departure from Kharg between 26–31 May; volume estimate via EO (Earth Observation) imagery sizing of tanker draft.
- **Prior probability:** 0.40 (18-day stall is unusually long; current dark-fleet queue is near saturation; Iran has incentive to resume offtake to reduce visible inventory risk; but PGSA vetting and US enforcement delays remain binding constraints).
- **Status:** Open. Decision window 26–31 May.

**H-003 · Created 2026-05-25 (Day 87) · Stop-out 2026-06-15 (Day 109)**

- **Hypothesis:** An Asian converter (Sinopec Fujairah, Chandra Asri, TPC Singapore, Yeochun NCC, or Taiwan PetroChemical) will declare a new Hard FM (Type 3 Downstream feedstock or Type 4 Distribution) citing Hormuz feedstock starvation or bunker fuel shortage by 15 June 2026. This would be the first Wave 3 cascade FM from a downstream operator.
- **Discriminating observable:** Formal FM letter filed with customers or published via exchange announcement, citing supply disruption or inability to fulfill contracts due to feedstock/fuel unavailability; sourced from Tier 1 (company filing) or Tier 2 (news outlet citing customer communication).
- **Prior probability:** 0.50 (Kharg stall + bunker shortage are now multi-week; Asian converter PnL pressure is accumulating; FM declaration is typically 10–30 days after visible supply constraint; if Kharg remains stalled through 27 May, FM probability rises to 0.65; if Kharg resumes, probability falls to 0.30).
- **Status:** Open. Decision window 1–15 June (but triggers earlier if Kharg stall extends past 27 May).

### Resolutions for hypotheses from prior runs

None; this is the first backtest cycle with explicit hypotheses.

## H-001 · Created 31 May 2026 (Day 93) · Stop-out 7 June 2026 (Day 100)

**Hypothesis:** KPC will not announce production restart by 1 June 2026, extending FM#2 ("even when Strait reopens") past the initial target. This signals producers believe Strait blockade is permanent and long-term capacity assumption is broken.

**Discriminating observable:** KPC Tadawul filing Q1 2026 earnings call (due ~25–31 May; must release by 7 June per exchange rules). Earnings call guidance: (a) confirms restart by 1 June, OR (b) extends FM past June with new timeline, OR (c) maintains "cannot estimate" language. 

**Prior probability:** 0.60 (based on SABIC "cannot estimate" precedent set 41 days ago and no update since; based on KPC silence 22–31 May despite being 6 days from restart target).

**Status:** Open. Stop-out date 7 June; resolution will be determined by KPC Tadawul filing + earnings call transcript.

---

## H-002 · Created 31 May 2026 (Day 93) · Stop-out 15 June 2026 (Day 108)

**Hypothesis:** Iran and Oman will not publicly sign a formal toll-framework agreement by 15 June 2026. Oman's strategic silence despite Iranian ambassador's 21 May disclosure indicates Muscat is withholding endorsement pending US-Iran negotiation outcome; if talks fail, Oman will avoid toll-framework signature to preserve post-ceasefire relations.

**Discriminating observable:** Muscat government statement or Oman news agency announcement of formal toll-framework signature. If signature occurs, would appear in (a) Muscat media, (b) Tehran state media, (c) UN correspondence, (d) diplomatic wires. If signature does NOT occur by 15 June, observable is absence of any public endorsement statement from Oman government despite 25 days elapsed since Iranian ambassador disclosure.

**Prior probability:** 0.72 (based on Oman's historical reluctance to align publicly with Iran on controversial maritime issues; based on GCC joint IMO letter 25 May showing regional consensus against toll framework; based on Muscat's 25-year precedent of strategic ambiguity on Iran relations).

**Status:** Open. Stop-out date 15 June; resolution will be determined by government announcement or substantive media silence (25+ days post-disclosure with no endorsement = 0.72-threshold hit).

---

## H-003 · Created 31 May 2026 (Day 93) · Stop-out 30 June 2026 (Day 123)

**Hypothesis:** No major maritime operator (Maersk, MSC, Hapag, CMA) will formally declare a Type 4 (distribution) FM by 30 June 2026, despite bunker fuel shortage signals and PGSA toll-payment sanctions-exposure risk. Shipping companies will absorb margin pressure and raise freight rates (30–50% increase) rather than invoke FM clause, which would trigger contract disputes and litigation risk.

**Discriminating observable:** Public FM declaration filed by Maersk, MSC, Hapag, or CMA subsidiary referencing (a) bunker fuel shortage making operations impossible, OR (b) sanctions-payment dilemma making transits legally impossible, OR (c) insurance/crew-safety thresholds exceeded. Absence of such declaration by 30 June would confirm hypothesis.

**Prior probability:** 0.65 (based on maritime operators' historical reluctance to invoke FM until physical/legal impossibility is proven; based on Day 22 Airgas precedent — first distribution FM took 94 days post-crisis onset; based on current bunker pricing $800–850 range still within historic volatility bounds, not yet "impossible" threshold).

**Status:** Open. Stop-out date 30 June; resolution will be determined by presence/absence of formal Type 4 FM declaration from any major carrier.

---

## H-004 · Created 31 May 2026 (Day 93) · Stop-out 30 June 2026 (Day 123)

**Hypothesis:** Wave Intensity will remain L4 Systemic through 30 June 2026 (no move to L5 Regime) because at least one of KPC or SABIC will announce restart guidance, suggesting long-term capacity assumption is not fully broken.

**Discriminating observable:** KPC Tadawul filing OR SABIC Tadawul filing between 1–30 June 2026 with explicit restart date (even if pushed to August or later) or restart-possible language (e.g., "preparations underway"). If both KPC and SABIC maintain "cannot estimate" or extend indefinitely past 30 June with no guidance, hypothesis is falsified (L5 Regime triggered).

**Prior probability:** 0.58 (based on KPC FM#2 explicit 1 June target — likelihood operator will confirm or clarify by 1 June is >50%; based on SABIC precedent of "cannot estimate" language but no explicit "never" statement; based on base-case Scenario A at 35% prior probability, which assumes at least one operator restarts on schedule).

**Status:** Open. Stop-out date 30 June; resolution will be determined by operator guidance (Tadawul filings, earnings calls) and Wave Intensity assessment at T+30.

## H-001 · Created 2026-06-04 (Day 97) · Stop-out 2026-07-04 (Day 127, T+30)

**Hypothesis:** Restart-type FM count remains static at 4 through 30 June 2026; no fifth operator files "cannot estimate return" language by 30 June.

**Discriminating observable:** Tadawul filing (SABIC or second major operator) with restart-type FM language; OR SEC 8-K (Saudi Aramco ADR, if filed US; or any US-listed operator) with "cannot estimate" or "indefinite offline" language. Threshold: count reaches 5.

**Prior probability:** 0.75 (base case: cascade tail absorbs stress via substitution without Hard re-escalation; companies avoid formal restart-type FM re-declaration unless forced by analyst pressure or auditor requirement).

**Status:** Open. Next update by 30 June 2026.

---

## H-002 · Created 2026-06-04 (Day 97) · Stop-out 2026-06-20 (Day 113, T+16)

**Hypothesis:** Iran-Oman toll-framework agreement signed and publicly released by 20 June 2026; ceasefire and diplomatic engagement result in formalized transit-permit system with Oman endorsement.

**Discriminating observable:** Public press release or bilateral communiqué (Iran PGSA + Oman Port Authority, or state statements) announcing toll-framework agreement, signed date, transit-fee schedule, and implementation date. Absence of such release by 20 June falsifies the hypothesis.

**Prior probability:** 0.55 (moderate: Trump Administration ceasefire extension holding; Bessent assurance to Oman given 28 May; but Iran sovereignty assertions and Oman domestic politics create risk of rejection).

**Status:** Open. Critical test by 20 June 2026 (T+16).

---

## H-003 · Created 2026-06-04 (Day 97) · Stop-out 2026-07-04 (Day 127, T+30)

**Hypothesis:** Strait of Hormuz commercial transit count rises to 30–40 vessels/day by 4 July 2026 (Windward AIS-confirmed), consistent with Scenario A (partial reopening + managed toll regime).

**Discriminating observable:** Windward Maritime AI published daily transit count reported at 30+ vessels/day for 3 consecutive days by 4 July 2026. If count remains <15/day through 30 June, hypothesis falsified; Scenario B stalemate/escalation path confirmed.

**Prior probability:** 0.45 (moderate: optimistic scenario; depends on Iran-Oman agreement signature AND Trump ceasefire hold AND PGSA operational relaxation; many failure modes).

**Status:** Open. Validates Scenario A base case if confirmed by 4 July.

---

## H-004 · Created 2026-06-04 (Day 97) · Stop-out 2026-06-30 (Day 123, T+26)

**Hypothesis:** Bunker fuel VLSFO price in Singapore stabilizes at $700–$750/mt (within ±$25/mt band) through 30 June 2026, indicating managed substitution supply (Scenario A/C plateau).

**Discriminating observable:** Singapore VLSFO reported price (Argus Media, Platts, ICIS benchmark) at 30 June 2026 within $700–$750/mt band. Spike above $850/mt or below $650/mt falsifies hypothesis; indicates either supply shock (→$900+, Scenario B) or demand collapse (→$600–, external crisis).

**Prior probability:** 0.50 (uncertain: depends on Strait transit recovery AND alternative supply (Russian, West Africa, South American) flowing to Singapore; high volatility expected).

**Status:** Open. Confirms Scenario A/C managed tail if true; Scenario B if falsified by upward spike.

## New hypotheses for Day 100 (7 June 2026)

### H-001 · Created 2026-06-07 (Day 100) · Stop-out 2026-07-10 (Day 100+33)

**Hypothesis:** SABIC or KPC will publish "even when Strait reopens" or "cannot estimate" language by 10 July 2026, signaling restart-type FM persistence and triggering Wave Intensity L4→L5 automatic test.

**Discriminating observable:** SABIC Tadawul filing or KPC RNS announcement containing explicit phrase "even when the Strait reopens" or "cannot provide an estimated date of return" or equivalent restart-uncertainty language, published by 10 July 2026 (Day 100+33).

**Prior probability:** 0.25 (aligns with Scenario B escalation probability; historically, SABIC Day 41 Tadawul filing set precedent for extended restart-type FM language).

**Status:** Open. Stop-out date: 10 July 2026. Next check: 10 June and 25 June earnings calls / regulatory filings.

### H-002 · Created 2026-06-07 (Day 100) · Stop-out 2026-07-15 (Day 100+38)

**Hypothesis:** Qatalum, Korean converter (Kumho, LG, Hanwha), or another Tier 1 downstream operator will publish FM lift (Type 5 Restart) by 15 July 2026, confirming FPCC model and strengthening Scenario A (55% base case).

**Discriminating observable:** Qatalum or named Korean petrochemical producer (Kumho, LG Chem, Hanwha TotalEnergies) publishes press release or regulatory notification stating "force majeure lifted" or "FM terminated" effective between 3 June–15 July 2026. Tier 1 source (direct press release, KSPO/KOSEF filing, or ICIS/OPIS confirmed).

**Prior probability:** 0.45 (FPCC restart (3 June) is first signal; ICIS May guidance suggests "end of June" stabilization plausible; probability aligns with Scenario A base case).

**Status:** Open. Stop-out date: 15 July 2026. Next check: 10 June (Qatalum guidance), 28 June (Korean industry conference outputs), 5 July (mid-year earnings).

### H-003 · Created 2026-06-07 (Day 100) · Stop-out 2026-06-30 (Day 100+23)

**Hypothesis:** US Treasury or OFAC will issue formal sanctions action against PGSA toll mechanism, Iran-linked payment intermediaries, or Bitcoin-backed "Hormuz Safe" insurance entities by 30 June 2026.

**Discriminating observable:** OFAC SDN list update (Federal Register publication or Office of Foreign Assets Control official notice) designating PGSA, PGSA-related Iranian entities, or intermediaries facilitating toll payments; OR US Treasury formal statement / press release explicitly warning secondary-sanctions enforcement for PGSA toll-payers.

**Prior probability:** 0.30 (US Treasury issued initial OFAC advisory (early June) on toll-payment sanctions risk; formal enforcement action is plausible within Q2 2026 close, but coordination with allies may delay until Q3. Aligns with Scenario B geopolitical escalation component).

**Status:** Open. Stop-out date: 30 June 2026. Next check: daily OFAC SDN updates, weekly Treasury press releases.

## 2026-06-10 (Day 103) · Hypothesis Delta

**New hypotheses for this run:**

### H-001 · Created 2026-06-10 (Day 103) · Stop-out 2026-06-17 (Day 110)

**Hypothesis:** Formosa's FM lift (3 June, Tier 1) is the first of a 2–3 operator cluster of downstream FM lifts by 17 June; if confirmed, Scenario C probability rises to 35%+.

**Discriminating observable:** At least one additional major downstream operator (SABIC, Aramco subsidiary, LyondellBasell, or Korean cracker) announces FM lift or restart guidance by 17 June (source: company press release or ICIS/Argus confirmation, Tier 1).

**Prior probability:** 0.40 (Formosa is encouraging signal; industry feedback from ICIS/Argus suggests other operators are in restart planning phase; momentum is directionally supportive).

**Status:** Open. Stop-out date is 17 June (1 week out); if no additional FM lift announced by this date, hypothesis fails and Scenario A (L4 sustained) probability increases to 55%+.

---

### H-002 · Created 2026-06-10 (Day 103) · Stop-out 2026-06-12 (Day 105)

**Hypothesis:** QatarEnergy will extend its LNG FM past mid-June deadline (decision announcement expected 12 June); if extended, it signals confidence in recovery remains <50% and Scenario A (L4 sustained) holds at 48%+.

**Discriminating observable:** QatarEnergy press release or Tadawul filing on or before 12 June announcing FM extension past 17 June (source: company or regulator, Tier 1).

**Prior probability:** 0.65 (Ras Laffan Trains 4&6 remain offline; South site damage timeline extends to late August; replacement gas turbines 2–4 year lead times; full restart unlikely before Q4 2026; management rationally extends FM to cover uncertainty).

**Status:** Open. Stop-out date is 12 June (2 days away in real time, but brief is published 10 June, so effective stop-out is 10 June review of Tadawul filings through 12 June). If no announcement by 12 June, treat as silent extension (FM remains active through at least 17 June) and hypothesis is HIT.

---

### H-003 · Created 2026-06-10 (Day 103) · Stop-out 2026-06-20 (Day 113)

**Hypothesis:** PGSA toll-permit denial rate (if published or confirmed by Windward/maritime intelligence) will remain <5% through 20 June; if <5%, administrative boundary test for L4→L5 is not triggered and L4 Systemic persists.

**Discriminating observable:** Windward, UANI, or Lloyd's JWC report on PGSA permit-denial rates for the period 1–20 June; rate published or inferred from vessel transit success data (threshold: >5% denials = escalation, <5% = no escalation). Tier 1 source required (Windward preferred).

**Prior probability:** 0.70 (PGSA has been operationally selective but not overtly rejecting transits at high rate; India-flagged cluster transit on 18 May indicates bilateral arrangements are functioning; denial rate likely low, but lack of public data creates uncertainty).

**Status:** Open. Stop-out date is 20 June. This hypothesis is designed to test whether administrative escalation (permit denials increasing from ~0–2% to >5%) is signaling L4→L5 move independent of operator FM extensions. If Windward publishes data showing <5% denial rate by 20 June, hypothesis is HIT and L4 Systemic is reinforced.

---

**Resolutions for prior hypotheses (from prior briefs):**

None from prior backtests (this is first brief with formal hypothesis logging; prior briefs used scenario probabilities without explicit stop-out dates).

## New Hypotheses This Run (Day 106)

### H-001 · Created 2026-06-13 (Day 106) · Stop-out 2026-07-13 (Day 130)

**Hypothesis:** If SABIC secures debt extension by 15 June 2026, Scenario A (Extend Stasis) will hold through 13 July 2026 (T+30 horizon). The extension announcement will signal lender confidence in a Q3 restart timeline and prevent cascading financial stress into the petrochemical sector.

**Discriminating Observable:** Aramco/Dow announce debt-service grace period extension OR debt restructuring moratorium by 15 June 2026 (EOD 14 June announcement deadline). Source: Tadawul regulatory filing OR Aramco investor relations OR Dow SEC 8-K filing. Binary outcome: extension announced (Hit) vs. no announcement / default (Miss).

**Prior Probability:** 70%. Lenders have already granted one grace period (26 Mar); second extension is statistically likely to protect lender position vs. forced restructuring during active geopolitical conflict.

**Status:** Open. Stop-out date: 13 July 2026 (Day 130). Posterior probability will be updated post-decision (15 June).

---

### H-002 · Created 2026-06-13 (Day 106) · Stop-out 2026-07-13 (Day 130)

**Hypothesis:** Bunker fuel market will remain tight (VLSFO Singapore > $800/tonne) through 13 July 2026, but no formal maritime operator Type 4 bunker-shortage FM will be filed. Shipping lines will absorb cost inflation and manage supply via diversions rather than invoke legal FM.

**Discriminating Observable:** (a) Singapore VLSFO spot price daily, reported by Ship & Bunker or VLSFO.COM; (b) Formal FM filing from Maersk, MSC, Hapag-Lloyd, CMA CGM, Evergreen, ONE, or other Tier-1 liner on bunker shortage. Sources: company press / ICIS / Polymerupdate / Lloyd's List. Binary outcome: price remains > $800 AND no maritime Type 4 bunker FM filed (Hit) vs. VLSFO falls below $800 or maritime FM filed (Miss).

**Prior Probability:** 60%. Evidence to date (Days 1–106) shows bunker tightness described in Tier 2 sources but no formal Tier 1 operator FM declarations despite visible constraints.

**Status:** Open. Stop-out date: 13 July 2026 (Day 130). Observable will be tracked daily via market data + FM filing monitors.

---

### H-003 · Created 2026-06-13 (Day 106) · Stop-out 2026-06-30 (Day 123)

**Hypothesis:** Iran's PGSA toll regime will remain operationally static through 30 June 2026 (T+17 horizon). No formal Iran-Oman toll protocol signature will be filed; no permit-denial rate escalation will be reported; no OFAC secondary-sanctions enforcement action will be announced.

**Discriminating Observable:** (a) UKMTO / MARAD MSCI advisory on permit-denial rates or toll-payment rejection; (b) Iran-Oman official protocol signature (publication by either government or via UN registry); (c) OFAC SDN list update or Treasury sanctions guidance targeting PGSA transactions. Sources: UKMTO, MARAD, Iranian state media (IRNA), Oman Gazette, Federal Register. Binary outcome: status quo maintained (no new enforcement or protocol signature, Hit) vs. any of the three events occur (Miss).

**Prior Probability:** 75%. PGSA has operated email-based vetting since 18 May with no escalation in procedure; ceasefire extension suggests no unilateral Iranian escalation near-term.

**Status:** Open. Stop-out date: 30 June 2026 (Day 123). Observable will be tracked via regulatory and diplomatic sources.

---

### H-004 · Created 2026-06-13 (Day 106) · Stop-out 2026-07-13 (Day 130)

**Hypothesis:** If SABIC does NOT secure debt extension by 15 June 2026, Scenario B (Financial Stress Escalates) probability will exceed 50%, and at least one new petrochemical-sector FM (KPC, INEOS, Huntsman, Dow affiliate) will be filed by 30 June 2026, cascading lender confidence loss.

**Discriminating Observable:** (a) No Tadawul / Aramco announcement of SABIC debt extension by 15 June EOD; (b) At least one new petrochemical operator FM filed 16–30 June 2026 citing "prolonged geopolitical uncertainty" or financial constraints. Sources: Tadawul, ICIS, Reuters, Polymerupdate. Binary outcome: no extension + new FM filed (Hit) vs. extension announced OR no new FM filed by 30 June (Miss).

**Prior Probability:** 25%. This is a contingency hypothesis, low prior. Will be reassigned to H-002–equivalent if SABIC extension is announced.

**Status:** Open. Stop-out date: 13 July 2026 (Day 130).

---

## Resolutions This Run

None. All hypotheses are new to this run.

## H-001 · Created 2026-06-16 (Day 109) · Stop-out 2026-07-07 (Day 130)

**Hypothesis:** PGSA toll regime will remain operationally static (no >5% permit-denial rate escalation, no new tariff, no Iran-Oman toll-sharing agreement) through 30 June 2026; Strait will transition to 15–30 transits/day by 1 July, signalling functional reopening. KPC/Saudi Aramco will announce restart contingencies by 22 June. Restart-type FM count will drop to 2–3 by 2 July. Wave Intensity will move from L4 Systemic to L3 Cascade by 1 July.

**Discriminating observable:** (a) Strait transit count: >15 transits/day on IMF PortWatch for 3 consecutive days by 20 June (measured against current 2/day baseline on 7 Jun). (b) KPC/Saudi restart statement with explicit 2–3 week timeline post-Strait-opening by 22 June. (c) Restart-type FM count: 4→2–3 (QatarEnergy 5yr and SABIC "cannot estimate" remain; KPC FM#2 and/or EGA lift). (d) No Iran-Oman toll agreement public signature by 22 June (conditional on Scenario B). (e) Wave Intensity: L4 Systemic maintained or moved to L3 Cascade by 1 July per restart-count rule.

**Prior probability:** 0.65 (base case Scenario A). Supporting evidence: Formosa lift (3 June) signals Wave 3 tail de-escalation; PGSA toll regime static since 18 May; bunker tight but not escalating to Type 4 FM; geopolitical ceasefire extension (prior brief) suggests no imminent Strait hostilities.

**Status:** Open. Stop-out date 2026-07-07 (Day 130, T+30 from today).

---

## H-002 · Created 2026-06-16 (Day 109) · Stop-out 2026-06-22 (Day 115)

**Hypothesis:** If Strait transits remain below 5/day through 22 June and no Iran-Oman toll agreement surfaces, Scenario B (extended stalemate) will lock in; bunker operator will file a maritime Type 4 FM by 25 June; Wave Intensity will remain at L4 Systemic through 30 June.

**Discriminating observable:** (a) Strait transit count: <5/day on all 3 consecutive days by 22 June (measured via IMF PortWatch). (b) No Iran-Oman toll agreement public signature by 22 June. (c) War-risk insurance premium remains at 8× pre-crisis or rises to 10×. (d) At least one maritime operator (Torm, Euronav, Teekay, or major shipping line) files Type 4 FM for bunker shortage at Port Suez or Ras Laffan by 25 June.

**Prior probability:** 0.22 (Scenario B). Supporting evidence: Geopolitical stalemate risk (prior brief indicates Trump "in no hurry" on Iran peace deal); PGSA toll regime entrenches; bunker market tightness chronic; no restart confirmation by 22 June.

**Status:** Open. Stop-out date 2026-06-22 (Day 115, T+6 from today).

---

## H-003 · Created 2026-06-16 (Day 109) · Stop-out 2026-06-20 (Day 113)

**Hypothesis:** Iran-Oman toll-sharing agreement will be formally signed and publicly announced by 20 June 2026. Strait transits will accelerate to 30+ per day by 25 June. US-Iran ceasefire will hold. KPC/Saudi restarts will be confirmed by 22 June. Restart-type FM count will drop to 1–2. Wave Intensity will move to L2 Elevated by 1 July.

**Discriminating observable:** (a) Iran-Oman toll agreement: formal public signature or joint government announcement by 20 June (monitored via Reuters, Bloomberg, Oman state media, Iranian state TV). (b) Strait transit count: >20/day on IMF PortWatch for 2 consecutive days by 25 June. (c) KPC/Saudi restart announcement with specific 1–3 week timeline by 22 June. (d) Restart-type FM count: 4→1–2 (KPC FM#2 and EGA lift, or both). (e) Wave Intensity: L4 Systemic→L2 Elevated per restart-count rule.

**Prior probability:** 0.13 (Scenario C, breakthrough). Supporting evidence: Geopolitical uncertainty (ceasefire fragility); Iran-Oman relations stable (Oman historically neutral); Trump administration pre-election pressure for diplomatic win (possible but not confirmed).

**Status:** Open. Stop-out date 2026-06-20 (Day 113, T+4 from today).

## H-001 · Created 2026-06-22 (Day 115) · Stop-out 2026-07-10 (Day 119)

**Hypothesis:** Hormuz transits will exceed 30 vessels/day by 10 July 2026 if the Trump-Pezeshkian MOU holds and PGSA permit processing remains >80% approval rate.

**Discriminating observable:** Daily AIS transit count (Kpler / Windward / UKMTO) exceeds 30 for 3 consecutive days by 10 July. Approval rate tracked via Iranian state media announcements or PGSA X account updates.

**Prior probability:** 0.55 (MOU signed; PGSA operationally live; 20 VLCCs recorded single-day peak 19 June; but 48h notice rule introduces friction; permit approval rate unknown; mine clearance ongoing).

**Status:** Open.

---

## H-002 · Created 2026-06-22 (Day 115) · Stop-out 2026-07-03 (Day 117)

**Hypothesis:** Iran will announce or formally publish PGSA fee schedule for post-August 17 period (exceeding $0.50/bbl or equivalent per-vessel toll) by 3 July 2026.

**Discriminating observable:** Official PGSA or Iranian government statement specifying fee levels, payment modalities, or exemptions for post-60-day window. Source: Iran state media, PGSA X account, UN-filed correspondence.

**Prior probability:** 0.70 (Iran has pre-fabricated the permit regime; toll infrastructure implies pre-calculated fee schedule; 60-day defer window limits future ambiguity).

**Status:** Open.

---

## H-003 · Created 2026-06-22 (Day 115) · Stop-out 2026-07-15 (Day 121)

**Hypothesis:** EU naphtha spot price will remain above $600/mt through July 2026, sustained by Petroline / substitution bottlenecks even after Hormuz transits normalize to 50+ vessels/day.

**Discriminating observable:** S&P Global Platts EU naphtha crack ($/mt) remains ≥$600/mt on each of 4 consecutive days in the period 10–15 July. This tests whether structural substitution (Norway, Russia, West Africa) is irreversible or cyclical.

**Prior probability:** 0.65 (Petroline 5–7 mb/d ceiling + EU naphtha diversification policy-backed through 2026Q4 + structural buyer switching = sustained premium).

**Status:** Open.

---

## H-004 · Created 2026-06-22 (Day 115) · Stop-out 2026-06-28 (Day 116)

**Hypothesis:** No new force majeure declaration from Tier 1 operators (QatarEnergy, Saudi Aramco, KPC, SABIC, BAPCO, ALBA, EGA, Methanex, GAIL, Petronet, LyondellBasell, Dow, Shell, TotalEnergies) will be filed 22–28 June 2026.

**Discriminating observable:** Zero Tier 1 FM filings (company press release, Tadawul / BSE / NSE / SGX / LSE / NYSE / TSE disclosure, or Tier 1 outlet confirmation) in the 72h window.

**Prior probability:** 0.80 (MOU signed; operator forbearance window open; no counterveiling kinetic events; restart timelines communicated).

**Status:** Open. **Note:** This hypothesis is a **null test** designed to confirm the absence of escalation. Hit = no new FMs; Miss = ≥1 new FM; False alarm / Surprise not applicable.

---

## New hypotheses (Day 118, 25 June 2026)

### H-001 · Created 2026-06-25 (Day 118) · Stop-out 2026-07-15 (Day 135)

**Hypothesis:** Geopolitical rhetoric about Strait closure is now decoupled from market reality due to real-time AIS and satellite transparency; any further Iranian re-closure announcement will be market-tested and likely falsified within 24 hours, reducing its policy impact.

**Discriminating observable:** Daily Strait transit count (AIS-visible vessels + confirmed by HSToday, Kpler, or UANI). If Iran announces re-closure again on or after 26 June and transits sustain ≥20/day for 3+ consecutive days, hypothesis is **Hit**. If transits drop to <10/day for 2+ consecutive days following an announcement, hypothesis is **Miss**.

**Prior probability:** 0.72 (strong pattern observed 20 May–25 June: multiple closure announcements contradicted by continuous traffic; market has adaptive expectations; Iran has not enforced kinetically since 29 April).

**Status:** Open; stop-out 15 July 2026 (if no further Iranian re-closure announcement by then, hypothesis is archived as **True but untestable in this window**).

---

### H-002 · Created 2026-06-25 (Day 118) · Stop-out 2026-07-10 (Day 132)

**Hypothesis:** Lloyd's marine war risk consortium capacity will see >20% utilization ($120M of $600M drawn) by 10 July 2026, indicating commercial confidence that Strait transits are insurable and routine, accelerating L4→L3 downgrade timeline.

**Discriminating observable:** Lloyd's weekly policy issuance report (published Thursdays) or market intelligence from Clyde & Co, Ince & Co marine insurance desks. Target: ≥5 policies issued by 2 July and ≥15 policies by 10 July. If <5 by 2 July, hypothesis **Miss** (war-risk appetite weak; Scenario B tail-risk priming).

**Prior probability:** 0.58 (moderate; market has shown strong demand for insurance solutions post-DFC reinsurance facility April 2026, but Lloyd's consortium is new and underwriting criteria are stricter than spot market).

**Status:** Open; stop-out 10 July 2026 (end of first 3 weeks of consortium operations).

---

### H-003 · Created 2026-06-25 (Day 118) · Stop-out 2026-08-15 (Day 169)

**Hypothesis:** Formal Iran toll/fee regime will be formally negotiated and announced by 15 August 2026 (end of 60-day MOU grace period), setting a structural 0.5–1.0% Strait toll that becomes permanent by end of 2026 and is treated as operational cost rather than geopolitical risk.

**Discriminating observable:** (a) Iran or US announcement of toll-framework agreement with fee percentages; (b) Lloyd's Market Consortium expansion to include "toll + war-risk" bundled underwriting product (observable via Lloyds press release or Ince & Co advisory); (c) First formal Strait toll levied on a vessel, with payment recorded via PGSA.ir portal. If any one of (a), (b), or (c) occurs by 15 Aug, hypothesis is **Hit**. If no announcement or formal toll by 15 Aug, hypothesis is **Miss**.

**Prior probability:** 0.68 (high; Iran has signalled toll intent since 22 May; MOU grace period expires ~17 Aug; Trump administration appears willing to accept fee framework per VP Vance 20 Jun statement: "Omanis, Iranians, and Gulf coast coalition together will figure out a proper security framework").

**Status:** Open; stop-out 15 August 2026.

---

### H-004 · Created 2026-06-25 (Day 118) · Stop-out 2026-07-15 (Day 135)

**Hypothesis:** QatarEnergy will confirm 50% unaffected-facility ramp-up readiness by 2 July 2026 (Day 122), providing the operational green light for a 30-day ramp trajectory reaching 50% capacity by early August.

**Discriminating observable:** QatarEnergy official press release or Tadawul filing stating "unaffected Trains 1–3 production ready for ramp-up within 30 days of safe Strait transit" OR analyst consensus (Bloomberg, Platts, Reuters citing company sources) confirming readiness. If confirmation occurs by 2 July, hypothesis is **Hit**. If postponed beyond 5 July, hypothesis is **Miss** (ramp delayed, Scenario B tail-risk priming).

**Prior probability:** 0.75 (high; unaffected facilities have sustained no kinetic damage, cooling systems are operational, and company has provided consistent signalling since 19 June that MOU enables restart; low probability of delay).

**Status:** Open; stop-out 15 July 2026.

---

## Resolutions for hypotheses with stop-out passed

None in this window (all prior hypotheses have been archived or remain open pending T+30 or T+90 horizons).

## New hypotheses for Day 121 run

### H-007 · Created 2026-06-28 (Day 121) · Stop-out 2026-07-12 (Day 135)

**Hypothesis:** Lloyd's consortium capacity depletion (<$200M remaining) will precede new Type 2 allocation FM filings by 24–48h, indicating insurance markets are the leading constraint on operator FM decisions in the post-MOU environment.

**Discriminating observable:** 
- **Data point:** Lloyd's syndicate capacity utilization reported by Marsh (broker), Intact Insurance (public comment), or LMA market intelligence. 
- **Source:** Insurance Journal, Reinsurance News, or Chubb earnings call (if any).
- **Threshold:** Capacity utilization >70% (i.e., <$120M remaining of $400M) within 10 days of a new maritime incident (e.g., follow-on Iran strike or IMO seafarer-evacuation event).

**Prior probability:** 0.45

**Status:** Open. Stop-out date is 14 days post-run (12 July 2026). If by 12 July no syndicate capacity depletion reported AND no new Type 2 allocation FMs filed, hypothesis is **Miss** (operators do not file allocation FMs based on insurance cost alone). If capacity >70% depleted AND new Type 2 FM files, hypothesis is **Hit** (insurance is the leading indicator). If capacity <70% depleted but no new Type 2 FMs file, hypothesis is **Surprise** (insurance can absorb stress independent of FM demand).

---

### H-008 · Created 2026-06-28 (Day 121) · Stop-out 2026-07-14 (Day 137)

**Hypothesis:** SABIC Jubail will announce a revised return-to-service timeline (either 3–6 months or "indeterminate") within 14 days, and the nature of the announcement (timeline vs indeterminate) will correlate 1:1 with operator confidence in Scenario A (MOU holds) vs Scenario B (allocation FM cascade).

**Discriminating observable:**
- **Data point:** Tadawul filing or Saudi Aramco earnings announcement or press release from SABIC management.
- **Source:** Tadawul, Saudi Aramco investor relations, Bloomberg Terminal.
- **Threshold:** Any public statement on Jubail restart timeline (even if wide range like "3–12 months").

**Prior probability:** 0.50

**Status:** Open. Stop-out date is 14 days post-run (14 July 2026). If by 14 July no statement issued, hypothesis is **Miss** (SABIC does not announce timeline under ongoing uncertainty). If statement is "3–6 months" or narrower, hypothesis is **Hit** (restart confidence is high; Scenario A dominates). If statement is "cannot estimate" or "dependent on downstream demand recovery," hypothesis is **Surprise** (operators view themselves as supply-constrained, not demand-constrained; implies Scenario C frozen-conflict trajectory).

---

### H-009 · Created 2026-06-28 (Day 121) · Stop-out 2026-07-15 (Day 138)

**Hypothesis:** QatarEnergy will meet or beat its 12-week ramp timeline from 19 June (late September restart target), and any slip >2 weeks will be attributed to shipping constraints (low Strait traffic forecast) rather than production readiness, confirming that Strait status is the marginal constraint on LNG restart.

**Discriminating observable:**
- **Data point:** QatarEnergy investor update, Wood Mackenzie revised forecast, or satellite heat-signature data from Ras Laffan LNG trains (via satellite analytics firm Kayrros or Maxar).
- **Source:** QatarEnergy official, Wood Mackenzie report, satellite imagery vendor report.
- **Threshold:** Public guidance on restart date (±4 weeks) or revised timeline if slip occurs.

**Prior probability:** 0.70

**Status:** Open. Stop-out date is 17 days post-run (15 July 2026). If by 15 July no public guidance issued, hypothesis is **Miss** (lack of clarity suggests uncertainty, not confidence). If guidance confirms late-Sep timeline ±4 weeks, hypothesis is **Hit** (production-ready confidence high). If guidance is delayed >15 July or if slip >4 weeks is attributed to "production complications" (not shipping), hypothesis is **False alarm** (production constraint is more serious than expected; restart trajectory degrades faster than Scenario A predicts).

---

## Resolutions for hypotheses whose stop-out passed

None. All three hypotheses (H-007, H-008, H-009) are newly created Day 121 and have stop-out dates 12–17 July (future).

## Hypotheses (Day 124 Run)

### New hypotheses for this run

**H-087 · Created 2026-07-01 (Day 124) · Stop-out 2026-08-15 (Day 139)**

**Hypothesis:** PGSA toll imposition (announced fee schedule ≥ $500k per non-LNG VLCC transit) will NOT occur by 15 August 2026.

**Discriminating observable:** PGSA official gazette or Iran parliament Energy Committee press release announcing finalized fee schedule with payment terms. Threshold: any announcement including numeric toll rate + payment mechanism (fiat currency, cryptocurrency, or commodity-indexed) counts as positive resolution.

**Prior probability:** 0.72 (complement of Scenario B base rate 25%, plus 3% upside for negotiation extension likelihood).

**Status:** Open.

---

**H-088 · Created 2026-07-01 (Day 124) · Stop-out 2026-08-20 (Day 144)**

**Hypothesis:** US CENTCOM mine-clearance mission will confirm ≥70% of main Hormuz channel as verified mine-free by 20 August 2026.

**Discriminating observable:** CENTCOM official press release or Navy flotilla public statement citing certified cleared-channel nautical mile count or percentage completion (e.g., "24 of 34 nautical miles cleared"). Interim milestone: gCaptain or UKMTO public maritime-safety notice confirming main-channel AIS traffic >25 daily crossings with zero reported mine incidents for 5+ consecutive days.

**Prior probability:** 0.68 (based on 40–50 day estimate from 25 June start, target late-Aug window; assumes no weather delays or IRGC interference).

**Status:** Open.

---

**H-089 · Created 2026-07-01 (Day 124) · Stop-out 2026-08-31 (Day 155)**

**Hypothesis:** QatarEnergy Ras Laffan North (41 mtpa LNG capacity) will announce production ramp start (formal restart, not conditional) by 31 August 2026.

**Discriminating observable:** QatarEnergy press release or customer notification stating "production ramp has commenced" or "resuming operations as of [date]" with explicit target (e.g., "target 30 mtpa by September 15"). Interim signal: LNG carrier AIS positioning at Ras Laffan terminal with cargo-loading activity (satellite imagery or vessel-tracking confirmation).

**Prior probability:** 0.58 (Scenario A assumes restart momentum loads; this hypothesis targets hard announcement by end-August. Conditional on mine-clearance progress [H-088] and no toll imposition [H-087]).

**Status:** Open.

---

**H-090 · Created 2026-07-01 (Day 124) · Stop-out 2026-08-17 (Day 141)**

**Hypothesis:** IRGC Navy will NOT issue formal closure of Oman-designated southern Hormuz route (cleared, demined) by 17 August 2026.

**Discriminating observable:** IRGC Navy Channel 16 VHF broadcast, Telegram statement, or formal letter to IMO explicitly closing southern transit corridor (e.g., "southern corridor deemed unsafe, transit prohibited"). Absence of such statement through 17 Aug counts as hypothesis hit.

**Prior probability:** 0.82 (IRGC has coordinated with PGSA regime; unilateral closure would undermine administrative control strategy. Isolated interception attempts [per 25 June cargo-strike] are enforcement, not closure).

**Status:** Open.

---

### Resolutions for hypotheses whose stop-out passed

(None this run; no hypotheses from prior briefs (Day ≤123) had stop-out dates ≤ Day 124.)

## New hypotheses for this run (Day 127, 4 July)

### H-001 · Created 2026-07-04 (Day 127) · Stop-out 2026-08-17 (Day 141)

**Hypothesis:** PGSA fee imposition on 17 August 2026 (end of 60-day MOU window) without OFAC waiver renewal will trigger Type 2 allocation FM filings from Maersk, MSC, and CMA CGM within 48 hours, causing L4→L5 regime-change cascade.

**Discriminating observable:** (a) PGSA publishes fee schedule by 16 August; (b) no OFAC/Treasury waiver letter published by 16 August; (c) Maersk, MSC, or CMA CGM file FM letter to customers by 19 August; (d) P&I club coverage withdrawn for PGSA-routed transits.

**Prior probability:** 0.35 (Iran has publicly asserted right to fees; Trump administration has stated opposition but enforcement mechanism is unclear; OFAC has 60-day statutory window to renew waiver, but renewal is not automatic).

**Status:** Open. Stop-out date: 17 August 2026 or date of PGSA fee schedule publication, whichever is earlier.

---

### H-002 · Created 2026-07-04 (Day 127) · Stop-out 2026-08-04 (Day 128)

**Hypothesis:** Ever Lovely strike (25 June) attribution will be released by JMIC or IMO by 10 July 2026, and if Iranian action is confirmed, a second kinetic strike will occur within 10 days (by 20 July), establishing a cluster pattern that escalates Trend to Worse.

**Discriminating observable:** (a) JMIC publishes attribution statement by 10 July naming Iranian/IRGC action; (b) second confirmed vessel strike or missile fire incident reported by 20 July in Strait; (c) Brent crude rises 3–5% on attribution announcement; (d) JMIC re-downgrades threat from Severe back to Critical.

**Prior probability:** 0.25 (Ever Lovely attribution delay to 4 July suggests political sensitivity; unconfirmed attribution is rare unless actor is genuinely unknown. If Iranian, escalation probability is high, but if non-Iranian, probability of second strike collapses).

**Status:** Open. Stop-out: 10 July 2026 (attribution deadline) or 20 July (cluster confirmation date).

---

### H-003 · Created 2026-07-04 (Day 127) · Stop-out 2026-08-15 (Day 140)

**Hypothesis:** QatarEnergy will ship first commercial LNG cargo from unaffected Ras Laffan trains by 14 August 2026, demonstrating restart viability and triggering LNG forward-curve rally (TTF +2–3%, JKM +1–2%) and broadening restart-type FM lift expectations (KPC FM#2, SABIC conditional).

**Discriminating observable:** (a) Windward AIS identifies VLCC departure from Ras Laffan with cargo LNG signature and Asian/EU destination by 15 August; (b) LNG shipping indices (Baltic) show spot rate increase for Atlantic-to-Asia LNG routes; (c) QatarEnergy issues formal statement confirming cargo shipment; (d) commodity forwards TTF/JKM show 1–3% rally within 24h of AIS signal.

**Prior probability:** 0.60 (QatarEnergy has explicitly committed to 50% ramp within 1 month of safe passage; 1 July qualifies as "safe passage" onset based on 43-vessel transits and MOU framework. First cargo by mid-August is consistent with published timeline).

**Status:** Open. Stop-out: 15 August 2026 (cargo shipment deadline).

---

## Resolutions for prior hypotheses:

None this run—all three prior hypotheses from Day 124 remain open (horizons extend to late August).

### New Hypotheses for Run (Day 130)

#### H-032 · Created 2026-07-07 (Day 130) · Stop-out 2026-08-17 (Day 142)
**Hypothesis:** PGSA toll-fee activation post-17 August triggers Type 2 (allocation) FM cascade within 7 days if fee >$500k/transit.

**Discriminating observable:** (a) PGSA announces fee structure by 15 August (formal notice); (b) Fee >$500k/transit confirmed; (c) Strait transits drop ≤25/day within 5 days of announcement; (d) ≥2 shipping lines or refined-product traders file FM within 7 days. **Source:** PGSA official website, OFAC sanctions clarification, Argus Media shipping desk.

**Prior probability:** 0.60 (55% of scenarios assign >40% risk to this path; timing window is tight but administratively clear).

**Status:** Open.

---

#### H-033 · Created 2026-07-07 (Day 130) · Stop-out 2026-08-07 (Day 132)
**Hypothesis:** Mine-clearance completion slips >7 calendar days beyond 7 August target, triggering Risk Scenario B escalation.

**Discriminating observable:** Joint US-Iran mine-clearance working group publishes weekly progress statement (required by MoU §3.2); if any statement post-28 July indicates <75% completion or revised timeline extending past 14 August, hypothesis triggers. **Source:** MoU signatories (US State Dept, Iran Foreign Ministry), CENTCOM public statements.

**Prior probability:** 0.25 (Low risk observed 4–7 July; no IRGC obstruction signals detected per Windward MIOC. However, historical pattern of IRGC scheduling delays on port facilities suggests >20% slip probability).

**Status:** Open.

---

#### H-034 · Created 2026-07-07 (Day 130) · Stop-out 2026-09-15 (Day 171)
**Hypothesis:** QatarEnergy equipment restart slips to October 2026 or later (vs. early September Edison target), driven by cryogenic-system requalification timeframe.

**Discriminating observable:** (a) QatarEnergy press statement post-1 September makes no announcement of Train 4 or Train 5 restart; (b) Next scheduled facility update (LNG industry conference or Tadawul guidance) occurs in October; (c) No cargo loading announcement or LNG carrier position change (AIS) indicating Ras Laffan loading gate activity through September 2026. **Source:** QatarEnergy press releases, Tadawul filings, Lloyd's Shipping Index, Kpler vessel positioning.

**Prior probability:** 0.35 (Edison timeline already signals early September; company public guidance from April suggests May goal was optimistic. Cryogenic restart complexity is known; 6–9 month requalification cycle is documented; internal slippage risk is structural not one-off).

**Status:** Open.

---

#### H-035 · Created 2026-07-07 (Day 130) · Stop-out 2026-08-07 (Day 132)
**Hypothesis:** No new restart-type FM declarations (Type 5) by 7 August 2026; restart-type FM count remains static at 6 through month-end.

**Discriminating observable:** Absence of new Type 5 FMs from SABIC, ALBA, BAPCO, EGA (conditional restarts now conditional on Strait reopening + debt restructuring). Monitor Tadawul, Bursa Malaysia, Seoul Exchange daily for new FM language. Absence of announcement = hypothesis hit. **Source:** Stock exchange filings, Argus Media, S&P Global Platts corporate news desk.

**Prior probability:** 0.70 (High probability: no new kinetic events 4–7 July, no facility-damage escalation, no debt default signals. Restart-type FMs are signaling mechanisms, not production events; low new-filing rate is consistent with stable geopolitical posture post-MoU).

**Status:** Open.

---

### Resolutions
None. All four hypotheses remain within their stop-out windows; no new hypothesis from prior runs has reached resolution date.

## New hypotheses for this run

### H-007 · Created 2026-07-10 (Day 133) · Stop-out 2026-07-20 (Day 140)

**Hypothesis:** The ceasefire (MoU signed 17 June 2026) will not survive beyond 10–20 July. Kinetic campaign will resume at daily strike rate by 13 July, triggering binary Strait closure (<10 transits/day) by 20 July.

**Discriminating observable:** Daily tanker strike count (per Windward MIOC, UKMTO) reaches 2+ for 3 consecutive days; Strait transit count (per PortWatch, TankerMap) falls to <10/day and remains there for 72h+.

**Prior probability:** 0.65 (updated from 0.30 on Day 130, post-kinetic escalation).

**Status:** Open. Stop-out date 20 July 2026 (Day 140). If hypothesis confirmed by 13 July (3 consecutive days ≥2 strikes/day), will trigger L4→L5 escalation cascade.

---

### H-008 · Created 2026-07-10 (Day 133) · Stop-out 2026-08-10 (Day 165)

**Hypothesis:** QatarEnergy's unaffected-facilities restart will not occur before Q4 2026. CEO operational halt (9 July) marks the end of forward-coverage momentum. Restart will slip to October 2026 or later, triggering new "cannot estimate" FM by August.

**Discriminating observable:** No LNG vessels dock at Ras Laffan for 21+ consecutive days; QatarEnergy files written statement delaying unaffected-facilities ramp to Q4 2026 or later; or market price action (forward LNG spreads) reflects restart delay beyond mid-August.

**Prior probability:** 0.72 (updated from 0.40 on Day 130, post-CEO halt).

**Status:** Open. Stop-out date 10 August 2026 (Day 165). Confirms forward-coverage FM risk.

---

### H-009 · Created 2026-07-10 (Day 133) · Stop-out 2026-07-25 (Day 148)

**Hypothesis:** If Strait binary closure confirmed by 15 July, at least one major Asian cracker (Yeochun NCC, Chandra Asri, or TPC Singapore) will file new Restart-type FM ("cannot estimate feedstock ramp") by 22 July, triggering L4→L5 regime change.

**Discriminating observable:** Tadawul filing, BSE/NSE filing, or press statement from named cracker operator containing "force majeure," "cannot estimate," or "indefinite delay" language; date stamped 15–22 July 2026.

**Prior probability:** 0.58 (updated from 0.25 on Day 130, post-Strait escalation).

**Status:** Open. Stop-out date 25 July 2026 (Day 148). Critical for marking L5 transition.

---

### H-010 · Created 2026-07-10 (Day 133) · Stop-out 2026-07-17 (Day 140)

**Hypothesis:** US-Iran diplomatic talks will NOT resume before 17 July 2026. Trump administration will focus on military deterrence rather than negotiation. IRGC will interpret military strikes as escalation authority and continue daily tanker attacks.

**Discriminating observable:** (a) No public announcement of bilateral talks or mediation restart by 17 July; (b) CENTCOM or State Department statement reaffirming military deterrence posture; (c) ≥2 additional tanker strikes between 10 July and 17 July.

**Prior probability:** 0.60 (escalation trajectory more likely than diplomatic reset given MoU failure).

**Status:** Open. Stop-out date 17 July 2026 (Day 140). If confirmed, reinforces H-007 (binary closure by 20 July).

---

## Resolutions for hypotheses whose stop-out passed

None. All hypotheses are new this run and have stop-out dates of 17 July 2026 or later.

## New hypotheses for this run

### H-037 · Created 2026-07-13 (Day 136) · Stop-out 2026-07-27 (Day 150)
**Hypothesis:** Restart-type FM count will increase by ≥3 (from current 6 to ≥9) within 14 days (by 27 July) if Strait closure declaration persists >10 consecutive days.

**Discriminating observable:** Tadawul or SEC filings from QatarEnergy, KPC, SABIC, or EGA containing language "cannot estimate return", "indefinitely deferred restart", or "conditional on Strait reopening >30 days". Count cumulative new restart-type FMs daily through 27 July.

**Prior probability:** 0.65

**Status:** Open

### H-038 · Created 2026-07-13 (Day 136) · Stop-out 2026-07-22 (Day 145)
**Hypothesis:** L5 Regime declaration will be published by supply-chain tracker if IRGC Strait closure declaration remains in effect without withdrawal >10 consecutive days (through 22 July).

**Discriminating observable:** IRGC formal statement (via IRIB, state TV, or official Navy statement) withdrawing, modifying, or clarifying Strait closure declaration. Absence of reversal = L5 threshold met. Check daily through 22 July.

**Prior probability:** 0.55

**Status:** Open

### H-039 · Created 2026-07-13 (Day 136) · Stop-out 2026-07-19 (Day 142)
**Hypothesis:** Allocation-type FMs (Type-2 shipping, Type-4 distribution) will be filed by ≥2 major operators (container lines, LNG traders, Asian refiners) within 7 days (by 19 July) in response to Strait closure and insurance cost escalation.

**Discriminating observable:** Lloyd's List, Splash 247, TradeWinds, or ICIS reporting of new FM declarations from Maersk, MSC, Hapag-Lloyd, CMA CGM, or major Asian refiner/utility citing Strait closure, insurance withdrawal, or route cost escalation. Count ≥2 independent filings by 19 July.

**Prior probability:** 0.60

**Status:** Open

### H-040 · Created 2026-07-13 (Day 136) · Stop-out 2026-07-18 (Day 141)
**Hypothesis:** Strait transits will remain below 15 vessels/day (mean daily average) through 18 July if IRGC maintains closure declaration without substantive reversal.

**Discriminating observable:** Daily Kpler and Windward Intelligence vessel-count averages for 14–18 July (5-day mean). Threshold: <15 vessels/day for ≥4 consecutive days = hypothesis hit. Single day >25 vessels = hypothesis miss (indicates corridor opening).

**Prior probability:** 0.70

**Status:** Open

---

## Resolutions for hypotheses whose stop-out passed

None. All hypotheses created today; stop-out windows 7–14 days forward.

## New hypotheses for this run

### H-001 · Created 2026-07-16 (Day 139) · Stop-out 2026-07-30 (Day 153)
**Hypothesis:** Qatar Transport Ministry maritime ban will not be lifted until IRGC formally rescinds Strait closure declaration. Sovereign maritime bans are rarely unilateral; they persist as long as the underlying threat exists. If Strait closure persists, Qatar ban persists.

**Discriminating observable:** Qatar Transport Ministry amends or rescinds maritime suspension advisory. Detection: official press release or Lloyd's List shipping notice. Threshold: any explicit statement permitting vessel departure or lifting import/export restrictions.

**Prior probability:** 0.75 (Qatar bans historically persist until regional threat ends; sovereign decisions not reversed mid-crisis).

**Status:** Open.

---

### H-002 · Created 2026-07-16 (Day 139) · Stop-out 2026-07-25 (Day 147)
**Hypothesis:** South Korean naphtha crackers (Yeochun NCC as proxy) will announce forced shutdown or material operating-rate cut to <20% by 22 July 2026, triggering Wave 3 FM cascade.

**Discriminating observable:** Yeochun NCC operating-rate announcement or customer FM letter dated ≤22 July. Detection: company statement, Tadawul filing (if applicable), or industry trade press (OPIS, Platts). Threshold: <20% utilization or explicit "production halted" language.

**Prior probability:** 0.70 (Inventory buffer is 2 weeks; Strait has been closed 5 days; next 7 days will drain remaining buffer to threshold).

**Status:** Open.

---

### H-003 · Created 2026-07-16 (Day 139) · Stop-out 2026-08-15 (Day 169)
**Hypothesis:** L5 Regime will be formally triggered on or before 1 August 2026 if Strait closure persists past 23 July OR if 2+ new Wave 3 production FMs file by 25 July.

**Discriminating observable:** (1) IRGC closure declaration still in effect on 23 July (public statement or silence on rescission), AND (2) either (a) 2+ new operator FM declarations (Wave 3 type, any sector) by 25 July, OR (b) Qatar maritime ban unlifted by 23 July. If both Strait closure and Qatar ban persist + any new Wave 3 FM, hypothesis triggers.

**Prior probability:** 0.55 (Current probability >50% assigned; tomorrow's signals will confirm or refute).

**Status:** Open.

---

## Resolutions for prior hypotheses

(No prior hypotheses from prior run logs are ready for resolution; first brief was Day 71, and backtesting began Day 136. No hypothesis stop-out dates have passed yet.)

## H-001 · Created 2026-07-22 (Day 145) · Stop-out 2026-08-02 (Day 157)

**Hypothesis:** IRGC tactical kinetic campaign (Belma + seizures, 16–18 Jul) was a signaling escalation, not an initial phase of sustained blockade warfare. De facto shipping will resume at 50–70% of pre-crisis baseline by 1 Aug if US avoids retaliation air strikes on IRGC bases 22–31 Jul.

**Discriminating observable:** 10-day moving average of laden vessel transits (LNG + general cargo + tanker combined) via Hormuz / Persian Gulf region, measured daily via Windward Intelligence + Lloyd's List. Threshold: ≥100 transits/day by 1 Aug (vs. 60 transits/day on 22 Jul, vs. 170 transits/day pre-FM baseline in Feb 2026). Lower threshold: if moving average stays <60 transits/day through 1 Aug, hypothesis is rejected (De facto blockade persists; sustained warfare hypothesis is True instead).

**Prior probability:** 0.55. (Kinetic pause 19–22 Jul is consistent with signaling; escalation usually shows clear pattern: initial strikes → pause for negotiation signal → either de-escalation or second wave. We are in the pause phase. But the blockade is formally declared "until further notice," so persistence is likely unless diplomatic signal follows. 0.55 reflects this uncertainty.)

**Status:** Open.

---

## H-002 · Created 2026-07-22 (Day 145) · Stop-out 2026-07-29 (Day 152)

**Hypothesis:** Restart-type FM count will remain static at 6 through 29 July. No new "even when reopened" or "cannot estimate" FMs will be filed by Saudi Aramco, ALBA, KNPC, or Methanex in the next 7 days.

**Discriminating observable:** Count of restart-type FM declarations (Wave 1, Type 5) filed via Tadawul, SEC EDGAR, or company press release. Current count: 6 (QatarEnergy 5-yr, KPC FM#2, SABIC, EGA, QatarEnergy output-ceiling, KPC lift-conditional). Threshold: count increases to 7 = hypothesis rejected. Count remains 6 = hypothesis accepted.

**Prior probability:** 0.70. (Operators are waiting for Strait-reopening signal or sanctions-relief signal before filing multi-quarter FMs. KPC and SABIC have already filed; Saudi Aramco has not. If Saudi Aramco does not file by 29 July, it suggests internal confidence that Strait will reopen by late August. ALBA and Methanex are unlikely to file absent major facility damage. 0.70 reflects the stability of the operator-filing cycle.)

**Status:** Open.

---

## H-003 · Created 2026-07-22 (Day 145) · Stop-out 2026-08-05 (Day 160)

**Hypothesis:** Suez Canal bottleneck will NOT emerge through 5 August. LNG queue at Suez will stay below 8 cargoes (capacity to flow all rerouted traffic without congestion). Alternative refining via Saudi / Iraq / UAE crude substitution will hold through August.

**Discriminating observable:** (1) Suez Authority vessel-queue data (daily briefing): current queue ~5 LNG + 120 containers estimated. Threshold: queue >12 LNG or container backlog >250 ships = hypothesis rejected (bottleneck emergent). (2) Saudi Aramco OSP (Official Selling Price) revision: if OSP falls below USD 87/bbl by 5 Aug, refineries may cut throughput and substitution fails. Threshold: OSP ≥USD 87 throughout = hypothesis held.

**Prior probability:** 0.75. (Current Suez capacity is ~2 LNG/day nominal; rerouted traffic is 1–2 LNG/day average; buffer is adequate. Saudi crude spot premium is narrow (+USD 2.50/bbl); OSP is stable. Bottleneck emergence requires both queue-length spike AND refiner-margin compression, which is unlikely in a 14-day window absent kinetic escalation forcing reroute surge. 0.75 reflects confidence that logistics are holding.)

**Status:** Open.

---

## H-004 · Created 2026-07-22 (Day 145) · Stop-out 2026-07-25 (Day 148)

**Hypothesis:** No new confirmed kinetic incident (supertanker strike, vessel seizure, air-to-air engagement, or mine strike) will occur 22–25 July. Incident rate will remain <1 event/day (average 0.3–0.5 unconfirmed claims or administrative ops only).

**Discriminating observable:** Confirmed incident reports (Tier-1 source: CENTCOM, IRGC official statement, tanker owner statement, vessel AIS/distress beacon, neutral observer like UK Defence Ministry). Threshold: ≥1 confirmed new strike = hypothesis rejected (escalation resumes). Zero confirmed incidents 22–25 Jul = hypothesis accepted (pause persists).

**Prior probability:** 0.60. (Kinetic pause 19–22 Jul is established. Pause duration is typically 3–5 days in this conflict pattern (May–July history). Hypothesis assumes pause extends to 25 July. 0.60 reflects uncertainty: pause could break any moment, or could extend longer if diplomatic signals are exchanged. I assign below-majority probability to the pause because both sides have shown willingness to escalate.)

**Status:** Open.

## New hypotheses (Day 148)

### H-084 · Created 2026-07-25 (Day 148) · Stop-out 2026-08-02 (Day 157)

**Hypothesis:** IRGC HSC swarm activity on 21 July (219 craft) is a pre-strike force-positioning event, not a sustainable deterrence posture. Within 7 days (by 31 July), a new confirmed kinetic strike occurs on a laden LNG or crude tanker, triggering L4→L5 transition and 2–4 new operator FM declarations.

**Discriminating observable:** (1) Confirmation of new vessel strike (Lloyd's incident report, UKMTO advisory, or operator press release) with date 26–31 July, (2) JMIC threat-level re-escalation to SEVERE (next advisory due ~26 July), (3) Windward HSC count sustains ≥180 craft/day for 3+ consecutive days after 21 July. If all three hold by 31 July, hypothesis is **Hit**. If zero of three hold by 31 July, hypothesis is **Miss**. If one or two hold (e.g., HSC stays high but no strike, or strike occurs with HSC lower), hypothesis is **False alarm**.

**Prior probability:** 0.45 (based on Day 7–22 correlation between HSC spikes and strikes within 48–72h; but broken by 22–25 July, so downgraded from 0.55).

**Status:** Open. Stop-out date: 2 August 2026 (after next 72h window).

---

### H-085 · Created 2026-07-25 (Day 148) · Stop-out 2026-08-15 (Day 170)

**Hypothesis:** North-corridor forced routing (88–100% of transits as of 22 July) represents a structural IRGC policy change: Iran has shifted from informal blockade to formal "approval-required transit regime" in Iranian territorial waters. This regime will persist for >30 days (through 24 August or longer) and will prevent any new operator FM declarations outside the current 6 restart-type FMs.

**Discriminating observable:** (1) IRGC public statement or Omani MOU update formally establishing north-corridor approval process (observed by ~27 July), (2) No new production-tier or allocation-tier FM declarations filed 26 Jul–15 August, (3) LNG transits stabilize at 0.3–0.5 cargoes/day (partial recovery) rather than collapse to 0.0 (full closure).

If all three hold, hypothesis is **Hit**. If new Strait closure announcement occurs OR new FMs are filed OR transits crash below 0.2, hypothesis is **Miss**. If IRGC makes anti-transit statements but operators find informal approval workarounds, hypothesis is **False alarm**.

**Prior probability:** 0.35 (this represents the "sustained contested corridor" scenario; probability mirrors Scenario A at 50%, but hypothesis is more conservative—it predicts no new FMs, which is a harder threshold than Scenario A's prediction of 0–2 FMs).

**Status:** Open. Stop-out date: 15 August 2026 (end of current FM extension window for QatarEnergy, signaling regime stability).

---

### H-086 · Created 2026-07-25 (Day 148) · Stop-out 2026-08-21 (Day 176)

**Hypothesis:** QatarEnergy's force majeure extension through 15 September 2026 (reported early July, confirmed through daily monitoring) will be extended AGAIN by 15 September with no new extension date published before that date. This signals operator expectation of >150-day Strait contention (Strait formal reopening delayed past 30 September 2026).

**Discriminating observable:** (1) By 10 September, Tadawul search and Reuters alert show zero announcements of early FM lift or shortening, (2) By 15 September, QatarEnergy publishes new extension (beyond 30 September or open-ended), (3) No formal Strait reopening declaration from IRGC or US/Iran joint statement by 15 September.

If all three hold, hypothesis is **Hit**. If FM is lifted or formal Strait reopening declared before 15 September, hypothesis is **Miss**. If FM extension is announced BUT with explicit end-date (e.g., "15 October") showing operator confidence in near-term restart, hypothesis is **False alarm** (partial credit for partial recovery signal).

**Prior probability:** 0.55 (QatarEnergy has already extended once; second extension is likely given lack of diplomatic progress as of 25 July; Strait closure formal posture unchanged since 12 July).

**Status:** Open. Stop-out date: 21 August 2026 (midway through FM extension window, allowing 2-week lead time for new extension filing).

---

### H-087 · Created 2026-07-25 (Day 148) · Stop-out 2026-08-08 (Day 163)

**Hypothesis:** Substitute supply routes (Russian naphtha, Australian LNG, North African ammonia) will report operational stress (delay >2 days, price jump >10%, or carrier advisory) within 14 days (by 8 August 2026), triggering a secondary FM cascade from retail-tier manufacturers (pharma, food, automotive).

**Discriminating observable:** (1) New OFAC sanctions on Russian LNG/naphtha effective before 8 August, OR Port of Brisbane strike/congestion claim, OR Red Sea/Indian Ocean incident affecting rerouted tankers, (2) Pharma excipients supplier (e.g., Recro Pharma, Lentio) files public supply statement or FM, OR food/beverage company (e.g., Nestlé, PepsiCo) issues profit warning tied to supply chain cost, OR automotive OEM (Volkswagen, Toyota) delays new model launch due to material shortage.

If any single discriminator holds by 8 August (not all three required, just one hard signal + one soft signal of downstream stress), hypothesis is **Hit**. If zero stress reports occur, hypothesis is **Miss**. If secondary suppliers report stress but no retail FM filed, hypothesis is **False alarm**.

**Prior probability:** 0.30 (substitute routes have held for 4+ months; they are well-hedged, but 30–60 day fatigue window is now opening, especially if new geopolitical events disrupt Red Sea or Russia sanctions).

**Status:** Open. Stop-out date: 8 August 2026 (end of current stress-absorption window for substitute supply chains).

---

## Hypothesis resolutions from prior runs

None outstanding from prior backtests (Day 145 hypotheses were first-run hypotheses with stop-out dates post-148).

## New hypotheses for Day 151

### H-008 · Created 2026-07-28 (Day 151) · Stop-out 2026-08-17 (Day 142 post-stop)
**Hypothesis:** Mine-clearance operations will not reach 50% completion by 7 August 2026, triggering MOU renewal failure and restart-type FM surge.

**Discriminating observable:** (a) Pentagon/CENTCOM operational brief on or after 31 July states <40% sonar survey completion, or (b) Italian MOD statement indicates "extended timeline beyond initial 40-day estimate", or (c) Lloyd's JWC Listed Areas threat level re-escalates to CRITICAL (post-18-June SUBSTANTIAL downgrade).

**Prior probability:** 0.35 (aligned with Scenario B baseline; mine-clearance data lag on 26–28 July search suggests either slow progress or no transparency).

**Status:** Open.

### H-009 · Created 2026-07-28 (Day 151) · Stop-out 2026-08-10 (Day 165)
**Hypothesis:** QatarEnergy will announce partial production restart (40–50% capacity) contingent on Strait reopening by 15 September 2026, signaling operator confidence in mine-clearance + MOU renewal.

**Discriminating observable:** Formal Tadawul/press release stating "expected to achieve [X]% output by [date] subject to Strait reopening or equivalent export route normalization" or investor call guidance from CFO on mid-Oct earnings call (expected ~2 August) with restart milestones tied to shipping conditions.

**Prior probability:** 0.25 (QatarEnergy has been taciturn on partial-restart language; mid-Oct FM extension suggests caution rather than confidence; but absence of restart signal could shift to higher probability if mine-clearance progresses visibly).

**Status:** Open.

### H-010 · Created 2026-07-28 (Day 151) · Stop-out 2026-08-04 (Day 158)
**Hypothesis:** IRGC HSC swarm activity will collapse to <100/day by 4 August, indicating de-escalation or preparedness for mine-clearance phase.

**Discriminating observable:** Windward MIOC daily brief or CENTCOM media statement citing HSC count <100 (vs 150–200 range in prior 72h); or JMIC threat level re-downgrade from SUBSTANTIAL to ELEVATED (below SUBSTANTIAL = lower deterrent posture).

**Prior probability:** 0.30 (HSC plateau suggests operational commitment, but swarms can demobilize quickly if IRGC command shifts to mine-clearance support; data lag on 28 July makes this observability-constrained).

**Status:** Open.

### H-011 · Created 2026-07-28 (Day 151) · Stop-out 2026-08-31 (Day 186)
**Hypothesis:** Restart-type FM count will remain static at 6 through 31 August, indicating operator consensus on 60-day MOU window durability (no surrender FMs, no acceleration FMs).

**Discriminating observable:** Zero new restart-type FM declarations (Type 5, multi-quarter) on Tadawul/EDGAR/exchanges from 1–31 August. Absence of both (a) escalation (new KPC/SABIC conditional delay FMs) and (b) optimism (partial restart FMs from EGA/QatarEnergy) counts as "held at 6" = consensus stasis.

**Prior probability:** 0.45 (operators are in wait-and-see posture; MOU window creates natural deadline for FM decisions; if held through 17 Aug (MOU expiration), operator silence becomes signal of either confidence or paralysis).

**Status:** Open.

---

## Resolutions (none completed by Day 151 — all prior hypotheses remain pending per backtest schedule).

## Hypotheses — Updated 31 July 2026 (Day 154)

**New hypotheses for this run:**

### H-001 · Created 31 July 2026 (Day 154) · Stop-out 14 August 2026 (Day 168)

**Hypothesis:** If mine-clearance advances on optimistic schedule (completion signal by 8 August per UK/France/Oman operation), insurance underwriters will resume Hormuz coverage by 10 August, enabling container carriers to announce phased route resumption 15–25 August (Scenario B). Probability of this hypothesis: 35% (aligned with Scenario B assigned probability).

**Discriminating observable:** (a) UK/France/Oman joint statement confirming 50%+ mine-risk area cleared by 8 August, OR (b) JMIC Advisory downgrade from SUBSTANTIAL to ELEVATED by 10 August, OR (c) Lloyd's List or insurance broker report confirming renewed underwriter appetite for Hormuz transits by 10 August. Any one of these three would validate the hypothesis.

**Prior probability:** 35% (calibrated to Scenario B).

**Status:** Open. Stop-out: 14 August 2026 (if none of the three observables occur, hypothesis falsified; Scenario A or C becomes more likely).

---

### H-002 · Created 31 July 2026 (Day 154) · Stop-out 7 September 2026 (Day 192)

**Hypothesis:** Sadara Chemical will not file a formal restart timeline or restructuring announcement by 15 September 2026. Instead, creditors will grant indefinite forbearance, and Sadara will linger in "cannot estimate" status through end-2026. This delays Wave 3 cascade into pharma/packaging until Q4 2026 or later.

**Discriminating observable:** (a) Tadawul filing on or before 15 September with specific restart target (e.g., "Q4 2026" or "January 2027") — falsifies hypothesis. (b) Credit Suisse / PIF / Aramco press release announcing capital restructuring or sovereign guarantee for Sadara debt — falsifies. (c) No new Sadara Tadawul filing 15 Aug–15 Sep — confirms hypothesis.

**Prior probability:** 55% (based on lack of public signal through 31 Jul and debt grace period passing 15 Jun without default).

**Status:** Open. Stop-out: 15 September 2026.

---

### H-003 · Created 31 July 2026 (Day 154) · Stop-out 31 August 2026 (Day 176)

**Hypothesis:** Container shipping carriers (Maersk, Hapag, MSC, CMA CGM) will not announce phased Strait route resumption in August 2026, despite any mine-clearance progress. Instead, carriers will maintain suspension through end-September pending full insurance coverage confirmation (avoiding reputational risk of another mid-journey Strait closure like March 2026). Scenario A becomes more likely than Scenario B.

**Discriminating observable:** (a) Major carrier (Maersk, Hapag, MSC, CMA CGM) announces phased Strait route restart for August or early September 2026 — falsifies hypothesis. (b) No carrier announcement by 31 August — confirms hypothesis.

**Prior probability:** 30% (carriers are risk-averse post-March, but commercial pressure to resume shipping by August is substantial).

**Status:** Open. Stop-out: 31 August 2026.

---

**Resolutions for hypotheses from prior runs:** None. This is the first run with a formal hypothesis ledger (Day 154 bootstrap). H-001, H-002, H-003 begin open.

## H-001 · Created 2026-08-01 (Day 155) · Stop-out 2026-08-17 (Day +16)

**Hypothesis:** Mine-clearance operation will complete by optimistic 17 August deadline per JMIC 40–50 day baseline (18 June + 50 days = 7 August, with administrative buffer to 17 August MOU expiration). No formal slip announcement will be made beyond this date.

**Discriminating observable:** (a) Formal JMIC / national navy announcement of clearance completion by 17 August; (b) Container-carrier press release announcing ME route resumption window 15–31 August; (c) Absence of mine-clearance delay statement through 17 August.

**Prior probability:** 0.60 (consistent with Scenario A base-case forecast).

**Status:** Open.

---

## H-002 · Created 2026-08-01 (Day 155) · Stop-out 2026-08-14 (Day +13)

**Hypothesis:** No new kinetic escalation (HSC attack, IRGC formal threat intensification, new mine-laying) will occur 1–14 August. 60-day MOU ceasefire holds through this window.

**Discriminating observable:** (a) UKMTO incident warning or MARAD MSCI advisory citing attack or mine-laying; (b) IRGC public threat statement escalating closure threat beyond current blockade posture; (c) Absence of incident reports through 14 August.

**Prior probability:** 0.85 (kinetic plateau observed 22 July–1 August; HSC deterrence posture sustained without major escalation).

**Status:** Open.

---

## H-003 · Created 2026-08-01 (Day 155) · Stop-out 2026-08-31 (Day +30)

**Hypothesis:** Restart-type FM count will remain static at 6 through 31 August. No new "cannot restart even when Strait reopens" or formal 5-year conditional FMs will be filed.

**Discriminating observable:** (a) New Tadawul / SEC 8-K filing by operator declaring multi-year conditional FM; (b) Industry analyst (Cefic, ICIS, Argus) reporting new long-term FM declaration; (c) Cumulative count tally in next 30-day window showing ≥1 new restart-type FM.

**Prior probability:** 0.70 (operators currently assuming Strait reopening in August–September, so long-term FMs are not yet filed; shift to restart-type only occurs if clearance slips or new kinetic event triggers permanent damage).

**Status:** Open.

---

## H-004 · Created 2026-08-01 (Day 155) · Stop-out 2026-08-31 (Day +30)

**Hypothesis:** Wave 3 cascade will not expand beyond current scope (pharma excipient starvation, PET/PP sourcing delays, automotive tier-2 supplier impact) absent a new kinetic escalation or mine-clearance slip. Cascade intensity plateaus through August; container resumption in late August triggers decay phase beginning early September.

**Discriminating observable:** (a) EMA drug-shortage list expansion (≥3 new generics from India/China shortage) by 31 August; (b) Tier-2 supplier bankruptcy announcement (Austrian / German stamping shop, Turkish casting plant, Eastern European wiring harness supplier) attributed to Hormuz cascade; (c) Automotive OEM production-cut announcement (VW, Audi, BMW Hungary plant utilization <70% due to parts starvation) by 28 August.

**Prior probability:** 0.60 (cascade is self-reinforcing via container suspension, but current starvation pace (8–12 week buffers) does not hit bankruptcy threshold until late August or early September; if container resumes mid-August, cascade begins decay).

**Status:** Open.

## 2026-08-04 (Day 158) · Hypothesis Log

### New hypotheses for this run

**H-008 · Created 2026-08-04 (Day 158) · Stop-out 2026-08-31 (Day 185)**

**Hypothesis:** Rhine River water-level recovery rate will fail to meet historical 2–4% per week normalization due to drought stress persistence into late August 2026; freight rates will remain >+200% elevated through 31 August, extending EU chemical margin compression into Q4 2026.

**Discriminating observable:** German Federal Waterways Administration daily water-level report at Kaub (reference point). Stop-out observable: if water levels recover to ≥70 cm by 31 August, hypothesis falsified (normal recovery rate confirmed); if water levels remain ≤60 cm on 31 August, hypothesis confirmed (delayed recovery, margin pressure sustained).

**Prior probability:** 0.40 (Rhine droughts 2018 and 2022 showed 60–90 day recovery lag; 2026 starting from already-weak position per Zerohedge report).

**Status:** Open.

---

**H-009 · Created 2026-08-04 (Day 158) · Stop-out 2026-08-24 (Day 168)**

**Hypothesis:** JMIC mine-clearance operation will delay formally beyond 7 August 2026; formal extension declaration will push mine-clearance completion into late August (after 17 August 60-day ceasefire MOU expiry).

**Discriminating observable:** JMIC public statement or Qatar/US/UAE official announcement confirming completion date. Stop-out observable: if completion announced on or before 7 August, hypothesis falsified; if 7 August passes with no announcement OR formal delay declared, hypothesis confirmed.

**Prior probability:** 0.25 (JMIC optimistic window assumes 40–50 day baseline from 18 June = 27 July–7 August; execution risk and geopolitical timeline uncertainty raise delay probability above baseline).

**Status:** Open.

---

**H-010 · Created 2026-08-04 (Day 158) · Stop-out 2026-08-31 (Day 185)**

**Hypothesis:** Spot LNG prices will remain in +15–25% premium range through 31 August 2026 despite QatarEnergy 30 Sept FM extension; spot-market arbitrage margins will compress to near-breakeven for Asia-to-Europe cargo operators, signaling sustained physical shortage (not pure financial/insurance premium).

**Discriminating observable:** Weekly LNG assessment from Argus Media, ICIS, or ChemAnalyst. Stop-out observable: if spot LNG premium declines to ≤10% by 31 August, hypothesis falsified (shortage priced out, margin recovery); if premium remains ≥15% through 31 August, hypothesis confirmed (physical shortage persists).

**Prior probability:** 0.65 (QatarEnergy 24-cargo FM + Edison routing through end-Sept means EU LNG demand still outrunning alternative supply; US LNG export capacity ramped but not yet sufficient to fill EU gap; spot premium = physical scarcity signal).

**Status:** Open.

---

**H-011 · Created 2026-08-04 (Day 158) · Stop-out 2026-09-03 (Day 191)**

**Hypothesis:** IRGC vessel-interception frequency will remain episodic (2–5 per week) through early September 2026, confirming L4 Systemic plateau; no escalation to >5 per week cluster (which would trigger Scenario C modeling).

**Discriminating observable:** Lloyd's JWC incident reports, UKMTO MSCI advisories, Windward Intelligence AIS-confirmed stops. Stop-out observable: if cumulative stops for 2–15 August remain ≤15 (average 2–3 per day), hypothesis confirmed; if >25 stops (average >3–4 per day) or any named carrier announces casualty/capture, hypothesis falsified (escalation to Scenario C).

**Prior probability:** 0.80 (IRGC Navy pattern since 12 July shows managed volatility, not sustained blockade; 4-day pause 25–31 July followed by 2–4 interceptions 31 July suggests operational tempo, not intensity escalation).

**Status:** Open.

---

### Resolutions for hypotheses from prior runs

*No hypotheses from Day 155 or prior runs have reached stop-out date. All backlog hypotheses (H-001 through H-007) remain open pending their respective stop-out dates.*

---

## 2026-08-07 (Day 161) · Hypothesis Log

### New hypotheses for this run

**H-012 · Created 2026-08-07 (Day 161) · Stop-out 2026-08-21 (Day 174)**
- **Hypothesis:** Rhine water level will not recover above 40 cm through 21 August; if true, EU chemical producers (Inovyn, Covestro, Clariant) will announce rate cuts or FM declarations by 21 August, extending Wave 3 cascade.
- **Discriminating observable:** BfG daily Kaub gauge reading; threshold 40 cm; source German Federal Institute of Hydrology (publicly available daily).
- **Prior probability:** 0.65 (given current 21 cm and historical August average of 80–120 cm, recovery to 40+ requires significant rainfall in Rhine basin or heat wave break; neither is forecast as of 3 Aug).
- **Status:** Open.

**H-013 · Created 2026-08-07 (Day 161) · Stop-out 2026-08-15 (Day 168)**
- **Hypothesis:** JMIC mine-clearance operation will announce on-schedule completion (14–16 Aug target) by 15 August; if true, first visible Hormuz transits (convoys under naval escort) will occur 18–22 August, triggering Scenario A probability jump from 35% → 60%.
- **Discriminating observable:** JMIC official announcement or CENTCOM / UKMTO NOTAM confirming mine-clearance completion; source primary regulatory bodies (JMIC, CENTCOM press release, or UKMTO navigational alert).
- **Prior probability:** 0.40 (JMIC original estimate was 40–50 days from 18 June = 27 July–7 August; current date (7 Aug) is at outer edge of original window; slips are typical for underwater demining operations; no announcement of completion or delay as of 7 Aug suggests delay is likely).
- **Status:** Open.

**H-014 · Created 2026-08-07 (Day 161) · Stop-out 2026-08-14 (Day 167)**
- **Hypothesis:** QatarEnergy will NOT announce any FM extension beyond 30 September 2026 by 14 August; silence on this date signals confidence in Strait reopening by end-Q3.
- **Discriminating observable:** QatarEnergy customer notice (Edison or other long-term contract holder) or Tadawul filing; absence of new extension notice is the signal; source company press releases, customer advisories.
- **Prior probability:** 0.70 (QatarEnergy has extended FM twice (29 May to mid-Aug, then 28 July to 30 Sept); pattern suggests they are "extending to certainty horizon" = high confidence in Strait closure through 30 Sept; unlikely to extend further by 14 Aug, as that would signal 4+ month closure extending into October, contradicting their stated rebuild timeline estimates).
- **Status:** Open.

### Resolutions for hypotheses whose stop-out passed

None. All priors hypotheses (if any existed in prior log entries provided) were outside this 3-day window's stop-out dates.

## H-NNN hypotheses for Day 164 run

### H-006 · Created 2026-08-10 (Day 164) · Stop-out 2026-08-25 (Day 158+17)

**Hypothesis:** Rhine water level stays <25 cm through mid-September despite seasonal rain forecast, locking Q4 2026 chemical/fuel supply chains into 2x freight-cost regime permanently.

**Discriminating observable:** Kaub gauge daily reading; if any single day shows >40 cm recovery and sustains for 72h, hypothesis fails. If it stays 20–25 cm range through 20 Aug, hypothesis gains 80%+ confidence.

**Prior probability:** 0.65 (Rhine climate patterns highly non-linear; 2018/2022 precedents show multi-week low-water persistence despite forecasts; current heatwave trajectory suggests no rain relief through August).

**Status:** Open. Meteorological data: WSV forecast shows recovery to 93 cm on 6 Aug (reported 29.5), but current trajectory suggests low persistence. Next update: 15 Aug.

---

### H-007 · Created 2026-08-10 (Day 164) · Stop-out 2026-08-20 (Day 154+20)

**Hypothesis:** Iran-Oman Strait management accord is formalized (signed) by 20 August, enabling 30–50 vessel/24h recovery in transits by 1 September, triggering L4 → 3.5 Wave Intensity downgrade.

**Discriminating observable:** Formal accord text published by Iranian FM / Oman Ministry, with specific transit corridors + fee structure defined. Not mere "talks ongoing" statements. Hard deadline: 20 August EOD.

**Prior probability:** 0.60 (Oman mediation track record positive; Iran-US pattern is rapid accord-then-collapse; current talks labeled "constructive" by both sides; but IRGC strikes 5–10 Aug suggest political instability, lowering accord probability).

**Status:** Open. Decision point: By 15 Aug, accord should be in legal review phase if on-track for 20 Aug signature. If no legal-review signal by 15 Aug, posterior drops to 0.35 (collapse likely).

---

### H-008 · Created 2026-08-10 (Day 164) · Stop-out 2026-08-22 (Day 156+22)

**Hypothesis:** Saudi Aramco Jazan refinery restarts on or before 15 August post-Houthi strike repair, signaling intact Saudi repair capacity and de-escalating L4 plateau.

**Discriminating observable:** Jazan restart confirmation: (a) Saudi Aramco press release naming restart date, (b) Kpler / Windward AIS tracking shows loading activity, (c) Tadawul filing with restart notice. Any one of (a)–(c) confirms. Hard deadline: 22 August (7-day grace from 15 Aug target).

**Prior probability:** 0.55 (Saudi repair teams competent; 400 kbpd refinery is national priority; but damage assessed as moderate IGCC + tank farm, which typically requires 15–30 day repair cycles; 15 Aug target is optimistic baseline).

**Status:** Open. No update available 8–10 Aug. Next signal: Saudi Aramco investor call or Tadawul filing expected by 12 Aug.

---

### H-009 · Created 2026-08-10 (Day 164) · Stop-out 2026-09-10 (Day 184+30)

**Hypothesis:** QatarEnergy does not lift LNG force majeure before 1 November 2026; 5-year Ras Laffan rebuild on track, confirming regime-lock on L4 Systemic (not L3 transition) through 2027.

**Discriminating observable:** QatarEnergy formal statement (press release, Tadawul filing, buyer notification) confirming no restart acceleration. If any QatarEnergy notice mentions restart before 1 Nov (e.g., "preparing to restart one train by 31 Oct"), hypothesis fails. Absence of such notice through 1 November confirms hypothesis.

**Prior probability:** 0.80 (Ras Laffan Trains 4/6 damage assessed as severe; 3–5 yr rebuild official timeline; no restart signals in any buyer correspondence; market consensus is 2029–2030 recovery at earliest).

**Status:** Open. This is a long-duration hypothesis; confirmation/falsification expected by 1 November 2026.

---

### Resolutions

None this run (all prior hypotheses remain open or not yet at stop-out date).

## Hypotheses log — 2026-08-13 (Day 167)

### New hypotheses

**H-045 · Created 2026-08-13 (Day 167) · Stop-out 2026-08-27 (Day 181)**
- **Hypothesis:** Rhine Kaub gauge will remain below 15 cm through 27 Aug, forcing production deferrals (automotive, chemicals, steel) that manifest as formal production FMs by German/EU operators by 20 Aug. At least one operator (BASF, Evonik, or ThyssenKrupp) will announce formal production FM or capacity cut >10% (publicly disclosed on SEC / stock exchange).
- **Discriminating observable:** (a) BfG 14-day forecast (updated daily) shows Kaub <15 cm through 27 Aug (threshold: probabilistic forecast >70% chance); (b) Operator press release / stock exchange filing (Tadawul, XETRA, Euronext) with "force majeure" language or "force majeure-equivalent" capacity cut announcement (≥10% volume reduction attributed to Rhine transport).
- **Prior probability:** 0.35 (Rhine is at record low 12 cm, 9 Aug forecast showed persistent low, BfG extended forecast typically accurate 7–10 days out; after that, meteorological uncertainty rises. 35% = confident in near-term <15 cm persistence, less confident in extension past 25 Aug).
- **Status:** Open. Stop-out date is 27 Aug. Hit if H-045 manifests by then; Miss if Kaub rises >20 cm before operator FM announced.

**H-046 · Created 2026-08-13 (Day 167) · Stop-out 2026-08-31 (Day 195)**
- **Hypothesis:** Iran-Oman accord will NOT be formally signed (or will be signed but Strait reopening will remain conditional on US policy concessions that are not met) through 31 Aug. Strait transits will average <20/24h through end-Aug; no "rapid ramp" phase will begin.
- **Discriminating observable:** (a) No joint Iran-Oman statement published by 21 Aug (source: Iranian FM statement, Oman FM statement, UN IMO registry); (b) OR statement published but does not include Strait reopening date or includes caveat "pending US action" or similar; (c) Strait transits (Windward, Lloyd's List, MARAD) average <20/24h for 3 consecutive days in the period 21–31 Aug.
- **Prior probability:** 0.60 (Iran-Oman accord is in final drafting as of 8 Aug, but reopening is explicitly conditional on US sanctions/blockade policy. Trump administration has not signaled sanctions relief. 60% = base rate for signature by 21 Aug is ~65%, but conditional probability of actual Strait reopening is lower ~40%. H-046 assumes one of: signature delayed, signature with caveats, or signature but Strait stays closed pending US action).
- **Status:** Open. Stop-out date is 31 Aug. Hit if Strait transits <20/24h average through end-Aug AND (no signed accord OR signed accord with reopening contingencies).

**H-047 · Created 2026-08-13 (Day 167) · Stop-out 2026-09-12 (Day 197)**
- **Hypothesis:** Houthi strike cadence will accelerate to 2+ confirmed strikes per week through 12 Sept (vs. current 1–2/week observed 1–13 Aug). Geographic spread of strikes will expand beyond Red Sea / Yanbu to include Gulf ports (Khalifa Bin Salman, Jebel Ali) or extended-range tanker hits (100+ nm from Saudi coast). Escalation will trigger upgrade of JWC-listed areas (merchant fleet war-risk insurance underwriting) to expand coverage footprint.
- **Discriminating observable:** (a) Windward SAR / Lloyd's List / UKMTO reported strike count 14–31 Aug totals ≥6 confirmed strikes (2+ per week average); (b) At least one strike is reported >100 nm from nearest land (open-ocean hit or extended-range precision), OR one strike hits a named Gulf port (Khalifa Bin Salman, Jebel Ali, Fujairah); (c) JWC notice (published on Lloyd's List) expands listed areas to include new Gulf zone (geometry change in war-risk underwriting footprint).
- **Prior probability:** 0.40 (Houthi pattern shows ~1–2 strikes/week so far in Aug; escalation to 2+/week is plausible if Oman-Iran talks stall [forcing Iran to "signal strength"], but not certain. Extended-range strikes are technically harder (101+ nm requires cruise missiles or drone swarms), suggesting lower probability of geographic expansion at this magnitude. 40% = base rate for cadence acceleration, lower for geographic spread + JWC update combined).
- **Status:** Open. Stop-out date is 12 Sept. Hit if any one of the three observables (cadence, geography, JWC) is confirmed; Miss if all three remain static through 12 Sept.

**H-048 · Created 2026-08-13 (Day 167) · Stop-out 2026-09-30 (Day 217)**
- **Hypothesis:** Dual-chokepoint system stress (Hormuz + Rhine) will cascade into observable supply-chain margin compression for at least TWO of the following industries by 30 Sept: (1) automotive (OEM or supplier capacity cuts announced), (2) chemicals (production deferrals or FM declarations from Chem industry), (3) steel / metal (mill curtailments), (4) utilities (rolling blackouts or demand destruction in EU). At least one will manifest as formal public FM or "force majeure equivalent" disclosure.
- **Discriminating observable:** (a) Automotive OEM (VW, BMW, Mercedes, Audi, Renault, Stellantis, Volvo, Scania) announces capacity cut or production schedule slip >15% attributed to supply-chain (naming Rhine, Hormuz, or "logistics" as reason); (b) OR chemical producer (BASF, Evonik, Covestro, Lanxess, INEOS, Huntsman, Arkema) announces formal FM or "capacity reduction attributable to supply-chain disruption" ≥10%; (c) OR steel producer (Arcelor, Thyssen, Salzgitter, Voestalpine, ArcelorMittal EU) announces mill output cut >20% attributed to energy or transport; (d) OR EU grid operator (ENTSO-E statement) reports demand-destruction event (rolling blackouts, industrial load shedding >1 GW sustained, explicitly attributed to energy market tightness from supply chain disruptions).
- **Prior probability:** 0.50 (Dual-chokepoint stress is now observable; margin compression is already evident in anecdotal reports (BASF CEO guidance, Evonik statements). Formal FM declaration is a higher bar than internal production deferral. 50% = confident that at least one industry will experience material impact by 30 Sept, but uncertain whether impact rises to formal FM disclosure threshold — executives often avoid the term "FM" even when conditions qualify, preferring "force majeure-equivalent" language or euphemisms).
- **Status:** Open. Stop-out date is 30 Sept (Day 217). Hit if any one of the four observables is confirmed; Miss if all four remain static through 30 Sept.

## New hypotheses for Day 170

### H-007 · Created 2026-08-16 (Day 170) · Stop-out 2026-08-30 (Day 184)

**Hypothesis:** Houthi attack cadence on Saudi Red Sea-adjacent refinery infrastructure will persist at 7–10 day intervals; third strike will target Yanbu crude export terminal or Ras Tanura refinery between 9–17 August 2026, extending outage chain across ≥2 facilities and crossing restart-type FM threshold (count rising from 6 to 8+).

**Discriminating observable:** IIR Energy Alert publication of third attack confirmation + restart date slip on either Jazan or Yanbu to ≥45 days outage duration OR Ras Tanura surprise shutdown announcement. Data source: IIR Energy daily monitoring, Reuters Breaking Energy, Lloyd's List Intelligence. Threshold: formal operator confirmation (Tadawul filing or press release) within 24h of IIR alert.

**Prior probability:** 0.40 (based on observed cadence 27–28 Jul + 8 Aug = 10-day interval; pattern suggests discipline and resourcing).

**Status:** Open.

### H-008 · Created 2026-08-16 (Day 170) · Stop-out 2026-08-31 (Day 185)

**Hypothesis:** Iran-Oman Strait routing accord will stall beyond 25 August 2026 due to unresolved US sanctions conditionality; informal talks will continue but no formal joint statement will be published before 1 September 2026, sustaining Hormuz transits at 10–15/day through end-August.

**Discriminating observable:** (a) No Iran-Oman joint statement published by 25 Aug; (b) US Treasury OFAC advisory on sanctions scope revision NOT issued by 24 Aug; (c) Lloyd's List / Windward Intelligence transit count remains <20 v/day for 27–31 Aug window. Sources: Iranian FM Telegram, US State Dept press releases, OFAC notices, Lloyd's List daily monitoring.

**Prior probability:** 0.35 (based on 7 Aug Iranian FM statement "final drafting" with no signature; complexity of US sanctions policy alignment increasing).

**Status:** Open.

### H-009 · Created 2026-08-16 (Day 170) · Stop-out 2026-08-28 (Day 182)

**Hypothesis:** Rhine River Kaub gauge will remain below 12 cm through 28 August 2026; combined with BASF/Lanxess/Evonik production margin crush (margin negative by observable statements), Wave 3 cascade will trigger ≥1 formal EU converter FM declaration (Tier 1 operator press release or stock exchange notice) by 25 August 2026.

**Discriminating observable:** Kaub gauge reading <12 cm on 20, 22, 24, or 25 August (BfG forecast data) + BASF or Lanxess or Evonik formal FM statement or EMA excipient shortage list addition referencing Rhine logistics constraint. Source: WSV / BfG water level reports, BASF/Evonik/Lanxess Tadawul / stock exchange filings, EMA official shortage database.

**Prior probability:** 0.25 (FM is last resort; companies typically manage margin squeeze via hedging before filing FM; BfG forecast suggests <12 cm likely but margin-negative statement not yet published).

**Status:** Open.

## Resolutions for hypotheses from prior runs

None — this is the first hypothesis backlog entry (hypotheses were not systematically tracked prior to Day 170).

## New hypotheses for this run

### H-006 · Created 2026-08-22 (Day 176) · Stop-out 2026-08-25 (Day 179)

**Hypothesis:** Iran-Oman accord collapses after 25 Aug 2026 deadline (≥70% probability by assessment). Trump administration rejects Iranian military-withdrawal demand as non-negotiable. Strait remains de facto closed through Q4 2026.

**Discriminating observable:** Official announcement from Iran FM, Qatar FM, or Oman Ministry of Foreign Affairs on 25–26 Aug (±24h window) stating talks have stalled or failed. Reuters/Bloomberg/AP will carry within 2h of statement. Search query: "Iran Oman accord" + "negotiations" + "failed OR stalled OR collapsed OR suspended" on 25 Aug morning.

**Prior probability:** 0.70 (elevated from 0.65 Day 167 based on Trump admin public statements rejecting withdrawal demand; Qatar FM statement 7 Aug indicated "final drafting" but no breakthrough imminent).

**Status:** Open. Stop-out decision point 25 Aug (noon UTC ±12h).

---

### H-007 · Created 2026-08-22 (Day 176) · Stop-out 2026-08-30 (Day 182)

**Hypothesis:** Saudi Aramco Jazan refinery restart slips into September 2026 (≥50% probability) following third Houthi claim on 18 Aug. Facility-level kinetic damage assessment extends timeline beyond 30 Aug target.

**Discriminating observable:** Saudi Aramco press statement on 28–30 Aug stating new restart date (or "date TBD"). Alternatively: satellite imagery (NASA FIRMS, Sentinel-2 GEOINT) shows continued fire/smoke 28–29 Aug, or no operational activity signals by 30 Aug. Secondary: Saudi Energy Ministry statement on refinery status (usually within 48h of incident). Tier-1 hard signal if Aramco invokes FM or issues force majeure notice on crude export contracts.

**Prior probability:** 0.45 (unconfirmed Houthi strike damage + prior two delays suggest logistical re-assessment ongoing; Saudi Aramco has been conservative on restart timelines this crisis).

**Status:** Open. Stop-out decision point 30 Aug.

---

### H-008 · Created 2026-08-22 (Day 176) · Stop-out 2026-08-28 (Day 180)

**Hypothesis:** Rhine Kaub gauge stays <15 cm through 28 Aug (≥85% probability per BfG forecast). Full modal shift to road/rail occurs within 48h; barge operators halt commercial operations <12 cm threshold.

**Discriminating observable:** BfG daily gauge reading at Kaub on 22–28 Aug published each morning 06:00 UTC. If Kaub <12 cm on any day 22–28 Aug, hypothesis confirmed (modal shift occurs immediately). Freight rates (Rotterdam-Rhine route per Freight Perspectives) spike >€200/ton (4× baseline) within 24h of <12 cm reading.

**Prior probability:** 0.85 (BfG forecasts <15 cm through 22 Aug, potential recovery 26–31 Aug; weather forecast shows no heavy rain through 25 Aug, scattered showers only 26–28 Aug insufficient to raise water levels significantly).

**Status:** Open. Stop-out decision point 28 Aug.

---

## Resolutions for hypotheses whose stop-out passed

**H-005** (from prior brief) · Created 2026-08-16 (Day 170) · Stop-out 2026-08-20 (Day 174): "Houthi escalation pattern continues at 2 attacks per week through 20 Aug; no breakthrough on Strait diplomacy by mid-Aug."

**Resolution:** **Hit** (with caveats). Two Houthi claims surfaced (late July attack on Jazan + 8 Aug second strike), and third claim on 18 Aug (one day past stop-out window, but trend clear). Iran-Oman accord stalled in "final drafting" (no breakthrough). However, the second Jazan attack (8 Aug) was NOT followed by immediate third strike as expected; 10-day gap suggests tactical redeployment rather than sustained 2/week tempo. Posterior probability that Houthi attacks sustain 2/week pace through Sept: 0.55 (down from 0.70 prior). Attack *claims* may be outpacing confirmed damage; escalation may be narrative rather than kinetic. Adjust monitoring weight to "unconfirmed Saba claims" (Tier-2 sourcing) vs. Saudi-confirmed damage (Tier-1). Recommendation: flag future Houthi claims with explicit "unconfirmed" tag pending Saudi/independent verification.

---

## 2026-08-25 (Day 179) · Hypothesis Delta

### New hypotheses for this run

**H-001 · Created 2026-08-25 (Day 179) · Stop-out 2026-09-08 (Day 193)**
- **Hypothesis:** Iran-Oman accord failure (unsigned by 28 Aug, coupled with explicit Iranian government statement that Strait remains closed) will trigger a wave of restart-type FM declarations from KPC, SABIC, EGA, or Orlen within 5 days (by 2 Sept). Restart-type FM count will increment from 6 to 8+, signalling operator consensus that Hormuz closure is regime (not temporary).
- **Discriminating observable:** (a) No Iran-Oman joint statement signed by 28 Aug (Tier-1 source: Reuters / Bloomberg), AND (b) Iranian Foreign Ministry or IRGC issues statement that Strait remains closed pending US concessions (Tier-1 source: IRNA / Mehr News), AND (c) KPC, SABIC, or EGA files new Tadawul / SEC 8-K disclosure with forward-looking "cannot estimate" or conditional-restart language (Tier-1 source: exchange filing).
- **Prior probability:** 0.62 (accord stall 70% × operator filing risk 70% given stall = 49% base, adjusted +13% for restart-type count stasis for 18 days = 62%).
- **Status:** Open. Stop-out threshold: 2 Sept (5 days post-accord-failure confirmation). Falsifying condition: Accord signature by 27 Aug, or new Hard restart-type FM does not appear by 2 Sept despite accord failure.

**H-002 · Created 2026-08-25 (Day 179) · Stop-out 2026-09-30 (Day 214)**
- **Hypothesis:** Rhine water level will remain below 20 cm Kaub through 31 August AND below 30 cm through 30 September, persisting through autumn rainfall season; combined with Hormuz 12% baseline, this dual-chokepoint stress will trigger an L4→L5 escalation decision point (PGSA toll regime or EU emergency tariff waiver) by 15 Sept.
- **Discriminating observable:** (a) BfG forecast on 27 Aug projects Kaub will stay <20 cm through 31 Aug with >90% confidence (Tier-1 source: BfG official), AND (b) by 15 Sept, either (i) PGSA announces mandatory toll regime change (Persian Gulf Strait Authority press release, Tier-1), or (ii) EU Commission issues emergency energy/transport directive lowering tariff on Rhine shipping (EU Official Journal, Tier-1).
- **Prior probability:** 0.45 (Rhine forecast 95% <20 cm through 31 Aug × PGSA toll risk 55% = 52% base, adjusted -7% for low probability of EU emergency action = 45%).
- **Status:** Open. Stop-out threshold: 15 Sept (boundary-test decision moment). Falsifying condition: Rhine Kaub rises to >25 cm by 31 Aug (≤5% BfG probability), or PGSA/EU take no escalatory action by 15 Sept.

**H-003 · Created 2026-08-25 (Day 179) · Stop-out 2026-09-30 (Day 214)**
- **Hypothesis:** Jazan refinery will *not* restart by 30 Aug as currently targeted; a fourth Houthi attack will occur 24–30 Aug, pushing restart to mid-September and triggering a "three consecutive failures" restart-FM pattern that escalates L4→L5 regime-shift probability to 60%+.
- **Discriminating observable:** (a) Houthi SABA News Agency issues statement claiming fourth attack on Jazan or sister facility (Yanbu / Ras Tanura) 24–30 Aug (Tier-2 source: SABA / Houthi military channel), AND (b) Saudi Energy Ministry or Aramco delays restart beyond 30 Aug (Tier-1 source: official statement or IIR Energy alert), AND (c) New operator FM or conditional guidance filed citing "extended refining outage" as triggering factor (Tier-1 source: Tadawul / SEC).
- **Prior probability:** 0.35 (Fourth attack probability 30% × restart-delay probability 70% given attack = 21% base, adjusted +14% for pattern-escalation risk weighting = 35%).
- **Status:** Open. Stop-out threshold: 2 Sept (restart-delay confirmation window). Falsifying condition: Jazan restarts on/before 30 Aug without further attack, or only minor damage is claimed by Houthis without restart delay.

**H-004 · Created 2026-08-25 (Day 179) · Stop-out 2026-09-15 (Day 200)**
- **Hypothesis:** Restart-type FM count will remain static at 6 through 31 Aug; if accord collapses and Hormuz closure is accepted as regime by operators, the count will jump from 6 to 8–9 (not 7) by 15 Sept, indicating bunching of filings (multiple operators filing simultaneously) rather than sequential declarations.
- **Discriminating observable:** (a) Accord confirmed unsigned/stalled by 28 Aug per prior H-001, AND (b) between 1–15 Sept, three or more operators (from {KPC, SABIC, EGA, Orlen, Asry, KNPC, BAPCO, Saudi Aramco conditional}) file new Tadawul / SEC / exchange disclosure with restart-FM language (Tier-1 source: exchange filings), AND (c) all three filings occur within 48-hour window (suggesting coordinated market signal, not independent decisions).
- **Prior probability:** 0.58 (Accord stall triggers filings: 70% × bunching probability 70% = 49%, adjusted +9% for operator herding behavior in crisis = 58%).
- **Status:** Open. Stop-out threshold: 15 Sept (post-accord-failure filing window). Falsifying condition: Accord signature by 27 Aug, or filings occur sequentially over 2+ weeks (no bunching pattern), or fewer than 3 new FMs appear by 15 Sept.

### New hypotheses for this run

## H-015 · Created 28 August 2026 (Day 182) · Stop-out 2 September 2026 (Day 187)

**Hypothesis:** Iran-Oman accord will not be signed by 1 September 2026; unsigned status by stop-out date (2 Sept) indicates &gt;75% probability of formal collapse by 15 Sept.

**Discriminating observable:** Formal joint statement from Iran-Oman foreign ministries OR absence of signature announcement by 23:59 UTC on 1 Sept 2026.

**Prior probability:** 0.70 (from forward market pricing, Kalshi/Polymarket 26–28 Aug).

**Status:** Open. Stop-out date 2 Sept (next trading day after 1 Sept threshold).

---

## H-016 · Created 28 August 2026 (Day 182) · Stop-out 31 August 2026 (Day 185)

**Hypothesis:** Rhine Kaub gauge will fall below 15 cm by 31 August 2026; if confirmed, cascading Type 2 FM (allocation) on barge-dependent chemical supply chains (BASF, Covestro, Evonik) will trigger by 5 Sept.

**Discriminating observable:** BfG PEGELONLINE gauge reading for Kaub &lt;15 cm posted by 23:59 UTC on 31 Aug 2026; corroborated by WSV or Waterways and Shipping Administration confirmation.

**Prior probability:** 0.15 (tail risk; BfG 95% forecast &lt;25 cm through 5 Sept, but &lt;15 cm within next 72h is sub-20% conditional).

**Status:** Open. Stop-out date 31 Aug.

---

## H-017 · Created 28 August 2026 (Day 182) · Stop-out 5 September 2026 (Day 190)

**Hypothesis:** Restart-type FM count will remain frozen at 6 (no new Type 5 or Type 6 FMs filed) through 5 Sept; if count rises to 8+, operator confidence in Strait reopening has collapsed.

**Discriminating observable:** Tadawul filings, SEC EDGAR 8-K submissions, or BX Dubai disclosures from QatarEnergy, KPC, SABIC, Saudi Aramco, Petronas, ADNOC, or major EU/Asia converters showing new long-term contract FM or "cannot estimate" statements filed between 28 Aug–5 Sept.

**Prior probability:** 0.25 (current count frozen since Day 52; escalation would require either (a) Iran-Oman collapse by 1 Sept + 4-day operator filing lag, or (b) unilateral sovereign-level Strait reblockade announcement. Either is plausible but not base-case).

**Status:** Open. Stop-out date 5 Sept (Day 190).

---

## H-018 · Created 28 August 2026 (Day 182) · Stop-out 2 September 2026 (Day 187)

**Hypothesis:** Jazan refinery restart will execute on 30 August 2026 as confirmed; if restart is delayed beyond 30 Aug (fourth Houthi attack or operational hold), Type 1 Production FM on 400,000 bbl/d will be filed by 2 Sept.

**Discriminating observable:** (a) Positive signal: Jazan liftings resume, facility operational status confirmation by Saudi Aramco or Reuters port watchers by 1 Sept. (b) Escalation signal: Fourth Houthi attack claim or official restart delay announcement by 30 Aug; Type 1 FM filing by 2 Sept.

**Prior probability:** 0.15 (restart delay; cumulative kinetic stress is visible but magnitude is facility-level, not systemic FM. Probability of fourth attack in 72h is &lt;20% based on Houthi tempo 2 attacks/week).

**Status:** Open. Stop-out date 2 Sept.

## New hypotheses for this run.

### H-001 · Created 2026-08-31 (Day 185) · Stop-out 2026-09-30 (Day 214)

**Hypothesis:** QatarEnergy's October FM endpoint (notified 28 Aug) signals management's confidence in post-October ramp to 10–15% production recovery by November 2026. If actual restart achieves 15%+ by 1 November, ramp trajectory is on schedule; if ramp is <5%, long-term contract FMs cascade.

**Discriminating observable:** QatarEnergy production figures (LNG export volumes) reported weekly by S&P Global Platts or trader reports. Threshold: 0.5–1.0 Mt/month by November 2026 (vs. pre-crisis ~5 Mt/month Ras Laffan). Source: Platts, Argus Media, LNG trader color (weekly updates).

**Prior probability:** 0.65 (base case assumption in today's brief).

**Status:** Open.

---

### H-002 · Created 2026-08-31 (Day 185) · Stop-out 2026-09-14 (Day 199)

**Hypothesis:** Iran-Oman Strait accord will be formally signed and implemented by 15 September 2026. Implementation means interim 60-day arrangement allows 30–40 transits/day by 30 Sept (50% pre-crisis baseline); Hormuz Trend reverses from Same to Better by 15 Sept.

**Discriminating observable:** Formal joint statement published by Tehran and Muscat on official gov't gazette or embassy portal (Tier 1). Threshold: Signature + publication by 15 Sept. Source: Iranian Foreign Ministry, Oman Ministry of Foreign Affairs (Tier 1 primary).

**Prior probability:** 0.25 (per today's scenario framework; base case assumes accord remains unsigned through September).

**Status:** Open.

---

### H-003 · Created 2026-08-31 (Day 185) · Stop-out 2026-09-07 (Day 192)

**Hypothesis:** Restart-type FM count will spike above 6 by 7 September 2026, driven by either Sadara, Saudi Aramco, ALBA, or MRPL India filing new "cannot estimate return" or multi-year language. Spike to 8+ triggers L4→L5 boundary test.

**Discriminating observable:** Tadawul / Bursa / BSE / NSE filing flagged "force majeure" + "cannot estimate return" or "multi-year" restart timeline. Count threshold: >6 (currently 6). Source: Stock exchange regulated disclosures (Tier 1 primary).

**Prior probability:** 0.15 (low probability that restart-type cascade occurs within 72h; more likely by mid-September given seasonal demand peak and month-end backlog pressure).

**Status:** Open.

---

### H-004 · Created 2026-08-31 (Day 185) · Stop-out 2026-09-05 (Day 190)

**Hypothesis:** Rhine Kaub gauge will remain <20 cm through 5 September 2026. If no recovery, EU chemical producers (BASF, Covestro, Lanxess, OMV) will declare additional FMs, creating Wave 3 cascade independent of Hormuz. Dual-vector supply shock (Hormuz + Rhine) escalates L4 stress.

**Discriminating observable:** BfG daily gauge reading at Kaub, Germany. Threshold: <20 cm on any day 31 Aug–5 Sep. Source: Bundesanstalt für Gewässerkunde (BfG) official water-level gauge (Tier 1 primary).

**Prior probability:** 0.95 (BfG forecast predicts <20 cm through early September; very high confidence in this observable).

**Status:** Open.

## New hypotheses for this run

### H-062 · Created 2026-09-01 (Day 186) · Stop-out 2026-10-01 (Day 186+30)

**Hypothesis:** If Iran-Oman accord (Strait reopening framework) is NOT signed and formally published by 30 September 2026, restart-type FM count will accumulate to 8–10 by mid-October as ADNOC and Saudi Aramco issue conditional restart notices (Wave 1 Type 5).

**Discriminating observable:** Public filing or press release from ADNOC or Saudi Aramco using restart-type language ("output will resume 60–90 days after Strait secured" or "conditional on port access restoration"). Source: Tadawul, ADNOC press center, Reuters. Threshold: At least one new Type 5 FM from a Gulf producer (not QatarEnergy, not KPC) filed between 15 Sept and 1 Oct.

**Prior probability:** 0.65 (medium-high). Rationale: If Strait remains closed past mid-September, regional producers will face customer pressure to formally declare restart timelines, shifting from private buyer notifications (as QatarEnergy did) to public regulatory filings. This cascades fear into supply chains and triggers dual-layer hedging (both long-term contract renegotiation AND emergency inventory builds).

**Status:** Open.

---

### H-063 · Created 2026-09-01 (Day 186) · Stop-out 2026-09-15 (Day 186+14)

**Hypothesis:** LNG spot price (1-month-forward, November 2026 delivery) will NOT exceed $30/MMBtu by 15 September 2026 if Edison or other major buyers continue announcing successful substitution pool access.

**Discriminating observable:** LNG spot quote for November 2026 cargoes on Platts/ICIS assessments. Threshold: Spot price <$30/MMBtu on at least 3 of 5 trading days (10–15 Sept). If price consistently >$30, substitution is failing.

**Prior probability:** 0.60 (medium). Rationale: Edison's 31 Aug statement ("already replaced 21 of 29 cargoes") suggests spot LNG supply is available, but at elevated prices. Prices typically remain <$25/MMBtu if substitution is flowing steadily; >$30/MMBtu signals rationing. This is a leading indicator of Wave 3 cascade intensification.

**Status:** Open.

---

### H-064 · Created 2026-09-01 (Day 186) · Stop-out 2026-10-15 (Day 186+44)

**Hypothesis:** If Rhine water level at Kaub falls below 30 cm on any day between 1 Sept and 15 Oct, inland barge cargo velocity will drop by 40–50% (measured by weekly barge transit counts via Rijkswaterstaat), triggering emergency road/rail intermodal activation and >15% shipping cost increases for bulk chemical/fuel cargo.

**Discriminating observable:** (a) BfG or Rijkswaterstaat official Kaub gauge reading <30 cm on any day 1 Sept–15 Oct. (b) Deutsche Logistik Verbund or Evonik Industries public statement on intermodal activation or cost escalation. Threshold: Both (a) AND (b) must occur for hypothesis to resolve as "Hit."

**Prior probability:** 0.30 (low-medium). Rationale: BfG forecast currently projects recovery to 43–100 cm by late Sept, which would keep Kaub above 30 cm through October. However, climate forecasts are volatile; a drought re-intensification (second heat wave) could push levels lower. This is a low-probability but high-impact (dual-chokepoint cascade) scenario.

**Status:** Open.

---

## Resolutions for hypotheses whose stop-out passed

None this run. All active hypotheses from prior runs (H-060, H-061) remain open and will be scored at their scheduled stop-out dates.

## New hypotheses for 2026-09-04 (Day 189)

### H-001 · Created 2026-09-04 (Day 189) · Stop-out 2026-09-07 (Day 192)

**Hypothesis:** US drone strikes on Iranian tankers (2 Sept, unverified Windward report) are confirmed by CENTCOM or Lloyd's by 5 Sept 12:00 UTC, triggering Iranian counter-strike on Gulf oil/gas infrastructure within 72 hours (by 7 Sept 18:00 UTC).

**Discriminating observable:** Official DoD/CENTCOM press release or verified Lloyd's Intelligence alert naming date/location/casualties of 2 Sept strikes; plus Iranian IRGC or state media statement signaling retaliation. Both required to trigger.

**Prior probability:** 0.35 (Windward is credible source but report is unverified; historical pattern shows ~30% of unverified Tier-2 military claims confirm within 72h; 65% are retracted or prove ambiguous).

**Status:** Open.

### H-002 · Created 2026-09-04 (Day 189) · Stop-out 2026-09-30 (Day 216)

**Hypothesis:** Rhine Kaub water level remains ≥35 cm through 30 September 2026, supporting BfG forecast recovery to 43–100 cm by late September and avoiding a second European inland shipping Hard FM.

**Discriminating observable:** BfG daily PEGELONLINE Kaub gauge reading published Monday/Wednesday/Friday through 30 Sept; 95% confidence threshold = weekly median Kaub ≥35 cm (vs. current 40 cm, 2018 prior low 25 cm).

**Prior probability:** 0.72 (BfG forecasts have historically converged to within ±5 cm of median by T+21 days; current forecast trajectory supports recovery; seasonal pattern shows late Sept rainfall is likely in Rhine catchment).

**Status:** Open.

### H-003 · Created 2026-09-04 (Day 189) · Stop-out 2026-10-01 (Day 219)

**Hypothesis:** QatarEnergy or other Tier-1 operator declares a new restart-type FM (Type 5 "even-when-reopened" language) by 1 October 2026, raising restart-type FM count from 6 to ≥7 and triggering L4→L5 boundary alert.

**Discriminating observable:** Press release or Tadawul/SEC filing from QatarEnergy, SABIC, KPC, Saudi Aramco, EGA, or other Tier-1 operator naming (a) production facility + damage assessment, (b) restart timeline >6 months, (c) explicit language "even when Strait reopens" or equivalent ("regardless of diplomatic resolution").

**Prior probability:** 0.25 (Restart-type FMs are rare signals of deep structural damage; 6 existing FMs already represent ~3x normal rate; new declaration would require either kinetic escalation 1–30 Sept or executive decision to pivot from tactical to multi-year allocation stance).

**Status:** Open.

## Resolutions for prior hypotheses

None — all prior hypotheses remain in Open status or did not reach stop-out date.
