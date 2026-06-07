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
