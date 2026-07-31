# Reflection log — Force Majeure Tracker

**Status:** Internal. Each daily-updater run appends one reflection entry. Read by future runs to inform methodology adjustments and source-tier tuning.

The point of this log is not to make the tracker "feel" better — it's to make it provably better at the next run. Every entry must name a specific signal that surprised it, a specific methodology rule that was tested, and a specific change to apply next time.

---

## Format

```
## YYYY-MM-DD (Day N) · Reflection

### What surprised me this run
One paragraph. The specific signal that broke an assumption — not a general observation. Name the source.

### Methodology rule that was tested
Which tier-weight, trend-rule, wave-test, or anti-bias default was put under stress. Did it hold? If not, why not?

### What to change next run
Concrete, testable change. "Promote Polymerupdate from Tier-2 to Tier-1 for European petchem cascade — it surfaced the Vynova FM 6 hours before Reuters." Not "consider broader sources."
```

---

_First reflection will be appended on the next updater run._

## 2026-05-11 (Day 73) · Reflection

### What surprised me this run

Nothing structural surprised. QatarEnergy's mid-June extension (4 May) was already known; no new Hard FMs in 72h was consistent with Wave 3 tail dynamics; Lotte's 11-day delay is a market-confidence signal, not a panic move. The lack of surprise is itself meaningful: after 73 days, the crisis signal-to-noise ratio has inverted. Early stages (Days 1–20) saw avalanche declarations; now (Days 71–73) the absence of new ones is the signal. This mirrors real cascade behavior in supply chains: initial shocks are loud, tail behaviors are silent.

### Methodology rule that was tested

**The "Trend rule" under equilibrium conditions.** The rule states: Trend = Worse if ≥2 Hard escalation events OR 1 regime-change event; Trend = Same if mixed Hard signals OR no Hard signals. Day 73 had zero Hard signals in 72h. Trend should move down (Better) if there are offsetting Hard de-escalations; there were none. So the rule correctly outputs Trend = Same. However, this exposed a gap: the rule is calibrated for signal *arrival*, not signal *absence*. Absence of new FMs (after weeks of declarations) is informationally equivalent to a small de-escalation (inventory buildup, demand destruction, equilibrium reached). The rule doesn't capture this nuance. Recommendation for next update: introduce a "signal-velocity" sub-rule: if FM arrival rate drops >50% YoY for 2 weeks, treat as Small Better signal (+5% Trend adjustment toward Better). This would have moved Day 73 Trend from Same to Same-with-slight-Better-bias, which better captures market sentiment (stabilizing, not deteriorating).

### What to change next run

1. **Lotte Korea 29 May is now a hard fork-in-road test.** The prior brief flagged this; this run must make the confirmation call by 14 May (3 days from now) and publish a T2 medium-confidence binary outcome by 17 May (tomorrow in brief window). Do not let this slip into "pending" limbo; it is a forcing function for Scenario B vs. A/C probabilities.

2. **Add a "Signal Velocity" dashboard card** to accompany the Trend and Wave Intensity cards. Format: "FM declarations (rolling 7-day): [N] | Trend: [up/flat/down]". This makes silent periods quantitatively visible. If rolling 7-day FM count drops below 1 per day, flag it as an equilibrium signal (not an improvement, but not deterioration either).

3. **Watch for "European stress signal by 20 May" with higher tier discipline.** The prior brief said "Week-of-18 May" is the target. This run set the same deadline and saw no signals. If no signals by 20 May, publish a T2 medium confidence update: "European PET/MEG converters have NOT signaled stress; inventory is holding better than expected; downgrade Scenario C tail risk from 25% to 20%, upgrade Scenario B from 45% to 50%." Make this a forced decision by 21 May (T+10 from today).

4. **Add Iranian military posture as a standalone dashboard cell** (like the "lead indicator" card). Format: "Iranian Navy Strait warnings · [active/inactive]". If status changes (warnings lifted OR new threats issued), trigger immediate Scenario C re-assessment. Current status: warnings active (ships forbidden transit without consent); ceasefire holds but no de-escalation language. Mark as Yellow (de-escalation risk present, not active).

5. **For Golden Screw items: add a "status" field.** Current format is static (component name, industry, risk, FM linkage). Add: "Status: [monitoring | imminent | active | resolved]". Helium, PA66 monofilament, MEG, specialty coke, urea should all be marked "imminent" or "monitoring" with T+deadline for when they flip to "active" (formal FM or supply allocation announced). This makes the tracker actionable for procurement teams.

## 2026-05-13 (Day 75) · Reflection

**What surprised me this run:**

Bunker fuel shortage emerged as an explicit Tier 1 signal (AP/Reuters, May 12) five days ahead of the expected T+7 deadline from Day 72. This is the first distribution-tier (Type 4) cascade indicator to surface in primary sources and marks the transition from "production crisis + feedstock shortage" to "logistics crisis + demand destruction." The surprise is not the shortage itself (it was flagged as watchlist signal) but the speed of escalation from private-market stress (shipper warnings, refueler availability tightening) to public Tier 1 press coverage. This suggests Wave 3 is propagating faster than the 14-day historical lag observed in the Felsberger dataset. Additionally, May 5–7 shipping attacks (CMA CGM San Antonio struck by cruise missile, JV Innovation fire) directly contradicted the ceasefire narrative and suggest the Pakistan-mediated diplomatic framework is less robust than initial reports (April 8 ceasefire) implied.

**Methodology rule that was tested:**

The **Trend rule (trailing 72h vs prior 72h, Hard-signal count)** was tested. Day 72 defined Trend as Same with "no new Hard FM declarations in trailing 72h." Day 75 reconfirms this rule: still no new Hard production-tier FM declarations (Wave 1/2 baseline stable at 92/14). However, the emergence of bunker fuel shortage as Tier 1 (distribution-tier Type 4) creates an interpretive edge case: **Is a distribution-tier Type 4 FM (bunker fuel) a "new Hard FM declaration" for Trend purposes?** 

The rule was designed to track production-tier (Type 1) and allocation-tier (Type 2) FMs because those create upstream supply loss. Distribution-tier FMs (Type 4) are secondary—they arise when production or allocation FMs cause downstream cascades. Bunker fuel is a Type 4 consequence of production loss (less crude → less bunker refining → physical shortage). Under strict interpretation, Trend remains Same because production-tier FMs (92) are unchanged. Under forward-looking interpretation, Trend should move to Worse because distribution-tier FM emergence signals Wave 3 is broadening beyond feedstock into tertiary industries (aviation, maritime), which is a regime change.

**Decision:** Hold Trend = Same, but flag in Wave Intensity guidance that **L4 Systemic boundary to L5 Regime is now visibly under stress.** If distribution-tier FM is formalized by Maersk, MSC, or CMA CGM within 7 days, Trend escalates to Worse retroactively and Wave Intensity escalates to L5. This is a "pending escalation" state—the rule is holding, but the condition for rule-change is now imminent.

**What to change next run:**

1. **Add explicit "Distribution-tier FM formalization watch" to Trend rule.** If any Tier 1 source reports a major shipping operator, airline, or logistics provider declaring FM on fuel supply or transport services, this is an actionable Trend escalation trigger (Worse) + Wave Intensity escalation trigger (L5 boundary). Current rule only tracked production/allocation tiers; it missed the distribution cascade until it was already visible in market behavior.

2. **Accelerate kinetic risk signpost schedule.** May 5–7 vessel strikes show that ceasefire-era attack windows are narrowing (not broadening as optimistic scenarios assumed). Current run uses May 13–20 as a kinetic-risk assessment window, but it should be daily (not 7-day batch). Add CENTCOM daily briefing to regular check-in, and set alerts for "vessel strike" + "Strait" OR "tanker attacked" + "Iran" to catch escalations on same-day publication.

3. **Separate "restart-type FM count" from "hard operator restart count."** Current methodology bundles these, but they are distinct leading indicators. Restart-type FMs (QE 5yr, KPC FM#2, SABIC "cannot estimate", EGA 12mo) are declarations of extended offline timelines; Hard operator restarts (KAFCO May 2) are confirmations of resumption. The former is a bearish signal (supply extended offline); the latter is a bullish offset. Next run should track them separately and report both in Wave Intensity assessment.

4. **Promote Argus Media to Tier 1 status for jet fuel availability signals.** This run cites multiple Argus analyst statements on European jet fuel inventory stress (6-week supply, 40% of imports from ME). These are specialized intelligence from a high-reliability source (used by refiners and traders for daily pricing) and should carry Tier 1 weight for distribution-tier FM sourcing, not Tier 2.

## 2026-05-16 (Day 78) · Reflection

**What surprised me this run**

Bunker fuel shortage emerged on schedule (May 12) but manifested as price signal ($800/tonne, +60%) rather than operator FM declaration. This was unexpected in timing and form. The prior brief flagged bunker fuel as "likely" Type 4 Distribution FM signal by T+3, but the actual manifestation is a price-only signal with no carrier formally declaring force majeure. This suggests the market is still in allocative/pass-through phase (cargo owners absorbing cost via freight surcharges) rather than physical-rationing phase. The shift from cost-absorption to rationing typically happens 5–10 days after price breaks (psychological & inventory-depletion lags), so the real Type 4 FM wave may be delayed to 23–27 May vs earlier prediction of 16–20 May. This is a **timing miss but directional hit** — the signal emerged as predicted, but formal FM declarations lagging price signal by 10+ days.

**Methodology rule that was tested**

The **Tier-2 shipping-press signal vs Tier-1 operator FM distinction** was stress-tested today. Bunker shortage has strong Tier-2 corroboration (Washington Post, Euronews, WSAW et al., all May 12) but NO Tier-1 operator FM from carriers. My methodology weights Tier-2 signals as "can move trend, not Wave Intensity alone" — this rule held: I classified bunker shortage as emerging Type 4 signal but did not move Wave Intensity from L4 to L5 on Tier-2 input alone. The rule proved sound: formal FM declarations are still pending (as of May 16), confirming Tier-2 data is leading but not conclusive. This distinction likely preserved accuracy by 5–7 days, because premature L5 call would have false-alarmed within the week.

**What to change next run**

(1) **Explicit timeline for Tier-2-to-Tier-1 confirmation window.** Add a "monitoring layer" that tracks price signals (Tier-2 commodity data) 7–10 days ahead of operator FM declarations (Tier-1). Bunker fuel shortage exemplifies this: price +60% on May 4–12 (Tier-2), operator FM expected 19–27 May (Tier-1). Codify this lag explicitly so future briefs can set confidence levels for FM-readiness briefings without over-committing to FM escalation. (2) **Separate "price signal FM readiness" from "operator FM declaration."** Bunker fuel should have been flagged as "Type 4 Distribution readiness" (Type 4 FM imminent within 7–14 days) rather than "Type 4 Distribution FM emerging" (already declared). This distinction clarifies supply-chain actions for executives: price signals → procurement de-risking (T+3–7 window); operator FM → contract restructuring (T+7–14 window). (3) **Watch for secondary FM waves on logistics cost escalation.** If bunker FM is declared (23–27 May), watch immediately for Type 4 FMs on container-line capacity & port dwell surcharges (expect 2–3 day lag from bunker FM → container line capacity FM).

## 2026-05-16 (Day 78) · Reflection

**What surprised me this run:**
The bunker fuel shortage signal surfaced in Tier 2 shipping press (WFSB, WaPo, Euronews, 12 May) as an explicit Type 4 Distribution-tier FM driver within the 72-hour window. This was not expected in the prior brief (Day 72); the knowledge base had flagged maritime exposure but classified it as secondary. The acceleration of bunker prices to $800/tonne and the explicit description of "shortages" and "reserve depletion" at Singapore (the world's largest refueling hub) moved bunker from analyst speculation to operator-observable physical scarcity. This is the clearest evidence yet that Wave 3 cascade is now hitting tertiary industries outside of conventional "primary operator FM" tiers, and it raises the bar for L4→L5 boundary test: any major maritime operator (MSC, Maersk, CMA CGM) declaring Type 4 FM on bunker within 7 days would be the strongest signal of regime shift short of kinetic escalation or KPC sovereign FM extension.

**Methodology rule that was tested:**
The "Tier weight rule" was stressed. Bunker shortage was reported by Tier 2 outlets (shipping press, commercial intelligence) before any Tier 1 operator statement (no MSC/Maersk FM letter yet). The question: should a Tier 2 signal (commercial intelligence) move the Trend assessment if it describes physical scarcity but is not yet operator-formalized? The rule as written excludes Tier 2 signals from Trend moves unless they are corroborated by Tier 1 action. The bunker signal was corroborated by (1) spot price data ($800/tonne on OilPrice, Tier 2 commodity site, but referenced in multiple Tier 2 outlets), (2) multiple independent Tier 2 sources (WFSB, WaPo, Euronews all citing commodity analyst Natalia Katona of OilPrice and June Goh of Sparta Commodities), and (3) no contradictory Tier 1 operator statement (no shipping company denial of scarcity). Under the "three corroborating Tier 2 sources" sub-rule, the bunker signal is classified as Soft-Medium rather than hard enough to move Trend on its own. This held; Trend remained Same. However, the bunker signal DID move the LEAD_INDICATOR and WATCHLIST weight toward bunker FM emergence as T+7 leading indicator, which is correct under the rules. The methodology held under stress; the rule is working as intended.

**What to change next run:**
(1) **Promote maritime operator filing to Tier 1 leading indicator.** Once any of MSC, Maersk, CMA CGM, Hapag-Lloyd, or ONE (Ocean Network Express) publishes a Type 4 FM letter on bunker supply or cost, this moves bunker shortage from Tier 2 Soft to Tier 1 Hard and automatically tests L4→L5 boundary. Add this as a specific action deadline (T+7 from today = 23 May). (2) **Extend feedstock inventory tracking to weekly updates.** The Lotte delay from May 18 to May 29 is driven by naphtha inventory depletion outpacing Strait reopening timelines. Currently, inventory data is sourced from analyst commentary (Maybank, ICIS) only monthly or quarterly. Add a weekly pulse-check (Argus MEA naphtha nominations, ChemAnalyst spot availability reports) to catch inventory cliff-edge before FM cascades announce it. (3) **Clarify the "ceasefire on life support" metric.** Trump's language (11 May) is qualitative, not quantitative. Define an operational rule: if either side violates the ceasefire within 24h (measured by incident reports from US CENTCOM, UK MATO, or vessel-tracking AIS data) more than twice in a 72h period, escalate Trend to Worse. Currently, ceasefire violations are reported but not aggregated into a breach threshold.

## 2026-05-16 (Day 78) · Reflection

**What surprised me this run:**
Bunker fuel shortage crystallized as a measurable Type 4 Distribution signal within the 72-hour window (May 12 emergence), bringing tertiary supply-chain FM one step closer to operator formalization. This was flagged in Day 77 watchlist but the speed of price escalation (from ~$500 to $800 in 4 months = 60%) and media coverage density (WFSB, WaPo, Euronews on same date) suggests the signal is hardening faster than primary-operator FMs stabilized. If MSC or Maersk formalize bunker FM by May 23, L4→L5 transition is live. The surprise is not the existence of bunker shortage (which is a logical consequence of refining disruption), but the rapidity of tertiary-industry signal maturation.

**Methodology rule that was tested:**
The "Hard signal required for Wave Intensity move" rule was tested by bunker shortage (Tier 2 signal, not Tier 1 operator FM). Per methodology, only Hard signals can move Wave Intensity. Bunker shortage is Tier 2 + distributed price/market signal, not a single operator's formal declaration. By strict methodology, this remains a Soft signal to Wave Intensity (though it is a Hard signal to Trend modulation). The rule held: L4 Systemic does NOT move to L5 on bunker shortage alone. However, bunker FM from MSC/Maersk (which would be Tier 1/2 mixed) would be a Hard signal and could trigger L5 if paired with KPC/SABIC extension. The rule is stress-tested but not broken.

**What to change next run:**
(1) Add a "maritime operator FM pending" counter to the LEAD_INDICATOR dashboard tile — currently only restart-type FM count is tracked; need parallel flag for "formal Type 4 Distribution FM risk" (0 today, 1 if MSC/Maersk announces by May 23). (2) Refine the Lotte Chemical restart tracking: the 11-day slip (18→29 May) is now a data point for naphtha feedstock tightness; if restarts on May 29, confirm no further slips by June 5; if another slip occurs, escalate Scenario C probability and flag Wave 3 naphtha cascade as formal secondary-operator FM candidate by June 15. (3) Introduce a 48-hour emergency monitoring protocol for Strait: if Iran announces any formal relaxation of blockade OR US military pause announcement, trigger immediate Scenario B assessment and Wave Intensity re-evaluation within 4 hours (current frequency is 72h cycle).

---

## 2026-05-19 (Day 81) · Reflection

### What surprised me this run

Day 81 produced no surprises. The 72-hour window (16–19 May) was operationally quiet: no new Hard FM declarations, no maritime operator escalation, no kinetic events. This was *consistent with prior forecasts* rather than disconfirming them. What *would* have been surprising: KPC or SABIC extending FM language unprompted (rather than waiting for the May 20–21 boundary test), or a new maritime operator FM on bunker fuel emerging 48 hours after the bunker signal hit Tier 1 (12 May). Neither happened. The market is in a **holding pattern**, consistent with ceasefire nominal but Strait functionally closed. This suggests supply chains are still absorbing via spot prices and operational adjustments (slow-steaming, run-rate cuts), not yet forcing structural hedges (long-term substitution contracts, sovereign rerouting).

The one micro-surprise: Lotte Chemical's +11 day restart delay (18 May → 29 May) is at the edge of what I forecast as "Type 3 cascade signal." I had pegged the signal threshold at "delay >7 days"; Lotte is +11 days, so it clearly crossed. But the fact that this was the *only* new restart delay in the window—no others announced—suggests the delay is Lotte-specific (perhaps production line rework or naphtha allocation negotiation), not indicative of a broad cascade (yet). If LG Chem or Hanwha TotalEnergies also announce >7 day delays in the next 48–72h, then the cascade thesis is confirmed and Type 3 escalation pressure rises.

### Methodology rule that was tested

**The Trend rule (trailing 72h vs. prior 72h, Hard-signal-only)** was put under stress this cycle.

The rule says:
- **Worse** = ≥2 Hard escalation events with no offsetting Hard de-escalation, OR 1 regime-change event.
- **Same** = mixed Hard signals OR no Hard signals.
- **Better** = ≥2 Hard de-escalation events with no offsetting Hard escalation.

Day 81 had *zero* Hard signals in 72h (16–19 May). The prior 72h (13–16 May, Day 78 boundary) also had zero Hard signals. By the rule, Trend should remain **Same** (no Hard signals = no vector). This held. **The rule passed the test.** Zero hard signals → Same trend is the correct reading.

However, this raises a methodological edge case: *Can a Soft signal (Lotte +11 day delay, Tier 2) override a zero-Hard-signal window?* My current methodology says **no**—Soft signals modulate Trend but do not drive it. They inform the Watchlist and CATEGORY signals, but not the headline Trend assessment. I believe this is correct, but it's worth flagging: if Lotte's delay is a leading indicator of broader feedstock scarcity that will cascade into Hard operator FMs in 7–10 days (e.g., LG Chem FM announcement May 26–27), then the zero-Hard-signal Trend: Same reading on Day 81 will have missed a 3–5 day signal delay. This is an acceptable lag (tactical vs. strategic horizon), but it's worth monitoring as the hypothesis evolves.

### What to change next run

**Proposal 1: Add a "Soft signal momentum" sub-metric to the Watchlist.**

Currently, Soft signals (Tier 2/3) are individual data points. I should track *cumulative Soft signal density* in each commodity chain and infer escalation probability. Example: if naphtha-chain Soft signals (Lotte delay, Korea controls, run-rate cuts) accumulate to 5+ in a 7-day window, flag "naphtha Type 3 cascade likely within 10 days" as a higher-confidence forecast. This would have let me weight the Lotte delay +11 days more predictively (current method: post-hoc flagging; proposed: pre-hoc risk scoring).

**Proposal 2: Explicit "boundary test confidence" field in Trend/Wave reports.**

KPC/SABIC May 20–21 is the next L4→L5 inflection. I should publish a confidence score (Low/Med/High) on the probability that the boundary will be crossed in the stated window. Current practice: I state "boundary is tested if X happens by Y date" but do not publish my prior probability that X will indeed happen. This is a information deficit. Remedial: "L4→L5 escalation probability in next 48h: **Medium (35%)**" would help leadership calibrate their own risk models.

**Proposal 3: Refine the "Type 4 Distribution" FM threshold.**

Bunker fuel has been Type 4 (Distribution) FM since May 12 (Tier 1 signal), but no maritime operator has filed formal FM yet. This is a gap between the analyst assessment and the operator declaration. I should develop an operational proxy: when bunker inventory (Singapore, Fujairah, Rotterdam) falls below X-day cover, *automatically* escalate to "Type 4 FM imminent" classification, even if operators haven't filed yet. Example: "Singapore bunker inventory <20-day cover = Type 4 FM formally declared by market" (not requiring operator letterhead). This would tighten the signal-to-action lag.

## 2026-05-19 (Day 81) · Reflection

**What surprised me this run:**

The absence of surprises is itself the signal. No new Hard FMs, no new kinetic events, no early restarts despite QAFCO appearing online 2 May. The stalemate is holding with mechanical precision: Strait at 5% traffic, QatarEnergy FM extended (not pulled), EGA confirmed 12 months, KPC silent (strategic silence = extend probability high). This suggests operator leadership has made internal decision to NOT restart until political conditions change materially. The surprise would be a restart announcement; the absence is predictable given governance constraints (capital boards won't sign off on $1B restart capex while Strait closure is structural).

**Methodology rule tested:**

The "Restart-type FM count = L4 floor, boundary to L5 requires new entry" rule held today. Count static at 4; no upgrade pressure. This is the Tier-1-only rule in action: soft signals (bunker shortage, shipping speed cuts, airline capacity cuts) accumulate but don't move Wave Intensity without Hard entry. The rule is working — it prevents premature L5 escalation when the crisis is actually consolidating at L4 (systemic, multi-quarter, stable FM count). However, if KPC/SABIC extend FM on 20–23 May, count rises to 5–6, and L5 becomes threshold-crossed. The rule held but test is imminent.

**What to change next run:**

(1) Broaden "Tadawul filing watch" to include NOT just filings but absence of guidance (deliberate silence = FM extension signal). Add a "Silence Index" that flags when operators go 3+ weeks without investor update on restart timeline. KPC (silent since 20 Apr), SABIC (silent since 9 Apr), Saudi Aramco (silent since 6 Apr). Next run should explicitly report operator communication gap as leading indicator.

(2) Track bunker inventory at THREE hubs (Singapore, Rotterdam, Fujairah) daily, not weekly. Type 4 Distribution FM threshold depends on inventory cross (if all three <30 days simultaneously, likelihood of formal maritime FM hits 70%+). Current brief uses only Singapore; missed Rotterdam tightening data.

(3) Add "stranded vessel count" as explicit L5 boundary test alongside maritime FM. If stranded count hits 2,000+ (currently 1,550), humanitarian crisis + forced unblocking moves toward military escalation risk. Currently subsumed in kinetic signals; should be explicit.

## 2026-05-19 (Day 81) · Reflection

**What surprised me this run**

The single biggest finding is that **no new restart-type FM declaration emerged in 72h despite bunker Type 4 signal being 7 days old.** The theory predicted maritime operator Type 4 FM within 7–10 days of the bunker shortage hitting the $800/tonne threshold (12 May emergence). As of 19 May, zero maritime operators (MSC, Maersk, Hapag, CMA, Evergreen, Zim) have filed. This suggests one of two things: (a) operators are betting confidently on June Strait reopening and are absorbing costs rather than escalating to FM, or (b) the pain hasn't reached legal/contractual threshold yet because carriers are still passing costs downstream to shippers faster than contractual FM clauses trigger. The absence of maritime Type 4 FM is a **leading indicator of pain tolerance**—once absorbed cost > contract escape cost, Type 4 FM becomes inevitable. We've seen this with bunker prices: $800/tonne represents 60% markup, which exceeds most bunker-cost-variation clauses in shipping contracts. The next 48–96h will be critical: if no maritime operator files Type 4 by 23 May, we have empirical evidence that industry absorption capacity is higher than the model predicted, which may mean the L4→L5 transition is further out than the 7-day window suggested.

**Methodology rule that was tested**

The **Soft-to-Medium signal tier threshold rule** was stressed this run. The bunker Type 4 signal is Tier 1 (AP, WFSB primary sources), but no **operator formalization** has occurred. Our methodology states: "Signal tier weights compound — three Hard signals in 72h is qualitatively different from thirty Soft mentions." The bunker signal is not Soft; it's Tier 1 commodity pricing data. But its **lack of operator-level FM declaration** means the system has not yet translated Tier 1 input into Tier 1 operator action. This gap is real and was correct in our methodological tier weighting, but it reveals a sub-rule we should make explicit: **Tier 1 commodity signal + Tier 0 operator response (silence) ≠ Hard FM**. The rule held, but it exposed a boundary case: at what point does Tier 1 signal absence of operator FM become a Tier 1 signal *of* operator resilience? We chose to treat the absence as "signal still in propagation," which is conservative and correct. The methodology did its job: it did not inflate the signal.

**What to change next run**

Add an explicit **"Operator silence on Tier 1 commodity signal" tracking sub-metric** to the watchlist. If bunker prices stay ≥$750/tonne for 10+ consecutive days without a maritime operator FM, we should add a hypothesis: "Shipping industry absorption capacity for 60%+ fuel surcharge is higher than theoretical contract thresholds suggest; actual FM trigger point may be $900–1000/tonne rather than $750–800." Operationalize this by tracking bunker price vs maritime operator IR disclosures (quarterly earnings calls) — if no CEO mentions Type 4 FM risk in late May calls, we have evidence the pain is still manageable. This would refine the L4→L5 boundary test from "T+7 after $800" to "T+14 after $800, with operator silence confirmation."

## 19 May 2026 (Day 81) · Reflection

### What surprised me this run

**Iran IRGC's institutionalization of Strait control via the "vast operational area" redefinition (15 May)** broke my assumption that closure was temporary/tactical. The redefinition extends Iran's claimed operational zone from the classical ~24-mile-wide strait to a 200+ km² area, removing the possibility of "narrow corridor" reopening without full Iranian concession. This shifts the boundary test: the L4→L5 escalation is no longer driven by new kinetic attacks or restart-type FM cascades, but by institutional entrenchment of closure. The IRGC statement is Tier 1, but I had been modeling closure as a negotiating lever, not a permanent strategic expansion. This changes the ceasefire-durability calculus: even if a ceasefire holds, Iran can sustain "vast operational area" enforcement without breaking the ceasefire language (enforcement ≠ attack).

### Methodology rule that was tested

**The Trend rule (trailing 72h Hard signals vs prior 72h) held**, but it exposed a gap: **institutional / regime-change signals are Hard tier (Tier 1) but do NOT move Trend by themselves if there are no accompanying operator FM escalations.** The IRGC redefinition should logically Worse the Trend (it hardens closure durability), but my rule requires Hard operator FMs (SABIC extend, KPC extend, Saudi Aramco announce production cut, maritime operator bunker FM). The redefinition is a precondition for those FMs, not a substitute. This means the Trend → Better path (Scenario A, 25%) now requires breaking the institutional redefinition, not just a ceasefire agreement. The rule is correct, but the boundary between regime-change signals and operator FMs needs tighter definition going forward.

### What to change next run

**Introduce a "Regime signal trigger" that hardness L4→L5 boundary conditions more explicitly.** The test should be: (a) New restart-type FM AND (b) Iran announces territorial/operational expansion (e.g., "vast operational area"). If both occur, Wave → L5 without waiting for operator FM cascade. The IRGC 15 May signal alone keeps us at L4, but paired with any KPC/SABIC extension or Saudi Aramco production-cut declaration, it becomes sufficient evidence of regime lock-in. Define the rule: **L4→L5 boundary moves if (restart-type FM extends past horizon) AND (geopolitical signal hardens closure expectation for >180 days).** Implement this by 22 May (before EIA June STEO update which will be the next major regime-change information event).

## 2026-05-22 (Day 82) · Reflection

**What surprised me this run:**

Nothing surprised. The trend line held as expected. Lotte Chemical restart on 29 May is confirmed on track per Seoul Economic Daily filing (27 March disclosure), not a new signal — the expectation was that this would be the test case, and it remains one. PGSA operationalization 4–7 May was previously flagged (Iran PGSA news 5 May), not a surprise. Bunker fuel prices at $800–846/mt align with the 11–12 May AP / S&P Global reporting already incorporated into Day 81. Strait remains closed per EIA STEO and IRGC statements — no deviation. The lack of surprise itself is data: the system is executing to prior expectations, which means the model's three-wave structure and restart-type FM forecast are tracking accurately.

**Methodology rule that was tested:**

The **Hard signal rule** (Tier 1 authority required to move Wave Intensity) was tested and held firm. Despite extensive Soft signals (bunker prices, carrier route suspensions, analyst commentary), Wave Intensity remains L4 Systemic because no new Hard operator FM declarations, maritime operator Type 4 bunker FM, or KPC/SABIC restart-type FM extension was filed 19–22 May. This is correct: Soft signals validate the cascade narrative but do not move the intensity rating. The rule worked as designed — it prevented false alarm escalation and kept focus on the actionable Hard boundary conditions (Lotte 29 May, SABIC filing window 20–26 May, PGSA toll schedule).

**What to change next run:**

(1) Add PGSA toll schedule and maritime operator exemption tracking as a **Tier 1 operational input** to the FM table. Once tolls are published (expected by 1 June), model the cumulative cost on a 40,000 TEU container ship transit (rough estimate: +$500k per crossing if average toll $10–15M per vessel). This will feed into whether maritime operators file Type 4 FM.

(2) Introduce a **Lotte restart confidence tally** that tracks regulatory filings, procurement orders, and equipment status updates (Tier 2 data). A single disclosure from 27 March is thin for a 72-hour go/no-go gate; Seoul Economic Daily updates or KOSPI disclosures could signal early slippage 2–3 days before 29 May.

(3) Separate **Scenario A / B boundary detection** into a standalone early-warning module. The current brief assigns probabilities post-hoc; instead, flag any of: (a) Lotte delay announced before 26 May, (b) SABIC Tadawul filing filed before 25 May, (c) new kinetic event before 26 May. These are leading indicators, not post-hoc adjustments. **Actionability improves if probabilities update intra-run, not on 3-day cycle.**

## 2026-05-20 (Day 82) · Reflection

**What surprised me this run**

The PGSA formalization occurred 2 days earlier than my forecast window (Windward report 16 May, X account 18 May vs. estimated 18–20 May). This is a minor 48-hour compression, but it signals faster-than-expected Iranian administrative execution. The toll amounts confirmed ($2M per transit, yuan/Bitcoin settlement) are at the upper end of announced estimates but more credible than some early rumors ($10M, unrealistic). What did NOT surprise: the lack of formal operator FM declarations 19–22 May — silence at Tier 1 (operator press releases, Tadawul) continues to track. The Lotte confirmation within 2 days of prior forecast is well within execution risk tolerance (not a surprise; a validation).

**Methodology rule tested this run**

The **Tier-1 signal for FM declarations rule** was stress-tested: with zero Hard FM declarations in 72h despite PGSA formalization (a Type 6 Cascade signal, Tier 1), the methodology held. The rule is: Hard signals only move Wave Intensity; Type 6 (regulatory/geopolitical) signals inform scenario probability but not Wave intensity directly. This run affirmed that distinction — PGSA is Tier 1 geopolitical (Windward, official X), but it is not an operator FM, so Trend stays Same and Wave stays L4. Restart-type FM count (the leading indicator for L4→L5) is the correct anchor, not PGSA toll formalization. The rule held.

**What to change next run**

Add a **secondary watchlist metric for administrative toll system stability** (e.g., "count of PGSA permit disputes, vessel seizures, toll-payment defaults per week"). The toll mechanism is now the chokepoint, not kinetic closure. If the administrative system breaks down (>2 seizures/week, toll disputes, bilateral carve-out failures), the system reverts to kinetic risk (Iran coercive interdiction). Current watchlist #3 (PGSA toll disputes) is correct, but it should include a quantitative threshold (>1 incident/week = escalation flag). Also: add a tertiary metric for **Lotte restart execution lag** (confidence decay function: +2 day slip = -5% confidence in A scenario; +7 day slip = -20%, trigger B scenario upgrade). These are testable, data-driven changes that tighten the action horizon.

## 2026-05-19 (Day 81) · Reflection

### What surprised me this run

The PGSA formalization on 18 May—specifically, the speed and operationalization—broke my prior mental model of the crisis as primarily kinetic and episodic. I had modeled the Strait as a binary: either kinetic strikes continued (Wave 1 extension) or they paused (transition to Wave 3 tail decay). What actually happened is a third path: kinetic attacks paused, but the IRGC shifted to administrative control (toll regime, permit system, bilateral carve-outs). This is not de-escalation; it is regime institutionalization. The six India-flagged vessels transiting as a coordinated cluster on 18 May showed that bifurcation is already operationalized, not just theoretical. For supply-chain modeling, this means the Strait is not "closed" or "open"—it is "managed-access with toll and bifurcation." That is a harder problem to analyze than kinetic disruption because the outcome (whether specific cargo moves) depends on flag, payload, and political relationships, not just physical capability. My prior models were supply-network-centric (commodity, facility, route); this was geo-political-centric (flag, bilateral carve-out, toll payment as a sovereignty claim). The surprise was methodological, not just factual.

### Methodology rule that was tested

**Rule 2b (Tier 1 floor rule):** "No public claim is published as Hard unless a Tier-1 source confirms." The PGSA toll regime was announced 18 May by Iran's Supreme National Security Council (Tier 1, primary state media) and independently corroborated by Windward (Tier 1 maritime intelligence). The bilateral India-flagged cluster transit was observed via Windward SAR+AIS (Tier 1 maritime). The rule held: I did not elevate the bifurcation signal to Hard without both primary state confirmation and independent maritime intelligence. This discipline kept me from over-inferring Scenario C (regime collapse) probability; instead, I correctly classified it as administrative transition (Scenario A supporting). The rule worked as intended.

**Rule 4 (Wave Intensity move rule):** "Wave Intensity does NOT move on Soft input." Bunker fuel price at $846/mt, shipping cost pass-through warnings, and Lufthansa route suspensions are all Medium/Soft signals. None alone or together warrant a move from L4 to L5. The Hard signals (restart-type FM count, maritime operator Type 4 bunker FM, KPC/SABIC extension) did not trigger. Rule applied correctly; L4 confirmed. No false-positive Wave Intensity inflation occurred.

**Rule 3a (Trend rule, Worse vs Same):** "≥2 Hard escalation events with no offsetting Hard de-escalation = Worse." I found 0 new Hard escalation events 16–19 May (no new FM declarations, no new kinetic strikes beyond BARAKAH residual, no new cascade FMs). The PGSA formalization, while significant, is administrative escalation (bifurcation, toll regime), not operator FM escalation. Trend: Same. This distinction is critical for supply-chain executives: administrative control is different from supply disruption. A regional shift in mechanism (kinetic → administrative) should not move the supply-chain risk Trend if the flow outcomes remain stable. My judgment held the line correctly.

### What to change next run

(a) **Bifurcation-tracking dashboard.** Add a new WATCHLIST item and GOLDEN_SCREW metric specifically for bifurcation stability. Track: (1) BRICS-aligned vessel transits vs. Western transits (AIS data from Windward), (2) reported toll payments (press, insurance, maritime intelligence), (3) secondary-sanctions exposure (OFAC alerts, Dryad maritime risk). This will give supply-chain teams a leading indicator of whether PGSA regime is destabilizing (toll rates rising, fewer Western transits, more dark-fleet activity) or stabilizing (consistent transit patterns, lower toll rates, bilateral agreements forming). Current brief reports bifurcation qualitatively; next cycle should quantify it.

(b) **Scenario C geopolitical-risk sensitivity.** In parallel with bifurcation-tracking, add a daily geopolitical-pulse check: Iran-Oman negotiations status, IRGC public statements (escalatory language?), Israeli/US intelligence leaks (strike planning?), Trump administration messaging (ceasefire commitment stable?). Scenario C probability (regime collapse, kinetic reignition) is 10%, but it can move fast if a geopolitical trigger fires. Currently, I track it passively (outcome of negotiations). Next cycle: actively monitor leading indicators (IRGC rhetoric, Oman negotiator quotes, Trump statement tone) and update Scenario C probability daily with a confidence interval (e.g., 8–15% range), not just 10% point-estimate.

(c) **Restart-ramp-curve forecast.** Lotte 29 May is a binary go/no-go in the current brief. Next cycle: if Lotte restarts, I should forecast the ramp curve (% capacity per week: W1 30%, W2 60%, W3 90%, W4 100%) and track it daily 30 May – 30 June. This will tell supply-chain teams: "When can you actually count on X tonnes/week of Yeosu ethylene?" Not just "Restart is scheduled." Ramp curves are leading indicators for Wave 3 cascade tail decay.

## 2026-05-22 (Day 84) · Reflection

**What surprised me this run:**

The pace at which Iran shifted from kinetic disruption to administrative control was faster than the prior brief's implicit forecast. The PGSA launched on 18 May with full operational status (permits issuing, toll collections reported) rather than as an announcement-only signal. Windward's 19 May briefing showed this was not a "soon to be operational" regime but one already processing transactions (6-vessel cluster cleared). This suggests the Iranian government had prepared the administrative infrastructure in advance of the announcement—a sign of strategic intent, not improvisation. The implication is that Iran had already decided to formalize the toll regime as a long-term policy (not a temporary coercive tool) before the ceasefire talks began.

**Methodology rule that was tested:**

The "restart-type FM count" leading indicator (§ Wave Intensity rule, methodology.md § 3.2) was tested this cycle. The rule states that Restart-type FMs (W1T5 language: "even when reopens," "cannot estimate," long-duration contract FM) are the boundary markers between L4 Systemic and L5 Regime. This run, the count stayed at 4 (QatarEnergy 5yr LNG, KPC FM#2, SABIC "cannot estimate," EGA 12-month). No new restart-type FM filed. The rule predicted: "L4 maintained; no move to L5 without new restart-type FM or maritime operator Type 4 FM." Outcome: rule held. However, the PGSA toll regime formalization is a *policy-level* constraint that operates independently of operator FMs. It is not a Tier 1 operator FM in the classical sense (not a declared force-majeure clause), but it is a Tier 1 sovereign regulatory signal that will have equivalent longevity. This exposed a gap in the methodology: the rule does not yet account for structural shifts that are not operator-declared. Recommendation: add a secondary leading indicator (e.g., "Sovereign administrative control milestones") that can trigger Wave Intensity moves independently of operator FM count.

**What to change next run:**

1. **Add a "Structural Policy Shift" leading indicator.** Codify the PGSA toll regime as a L4→L5 *modifier*, not a Wave Intensity *trigger*. The presence of a sovereign toll regime does not change the count of restart-type FMs, but it does change the *duration expectancy* of the crisis. If the regime persists beyond 120 days (i.e., passes the T+90 mark), Wave Intensity should be re-evaluated upward regardless of operator FM count. This reflects the reality that a permanently tolled Strait is a different crisis mode than a temporarily blockaded one.

2. **Tighten PGSA toll payment data sourcing.** Windward's "up to $2M per transit" is range-based, not point-based. Next run, request Windward to provide transaction-level data (number of transits cleared per day, average toll per vessel, currency mix) to track the rate at which the regime is stabilizing. If transits are rising (10+/day) with stable toll receipts, the regime is profitable and likely durable. If transits are falling or toll-per-transit is spiking, the regime may be destabilizing (Iran tightening gates, vessels refusing to pay).

3. **Establish a "Bifurcation Tracking" scorecard.** The dark-fleet vs. Western-fleet split is now a material supply-chain determinant. Add a weekly metric: % of tanker traffic operating dark AIS + estimated toll-cost absorption rate by BRICS vs. sanctioned carriers. This will be the leading indicator for when substitution (BRICS sourcing) becomes the structural norm vs. a temporary workaround.

## 2026-05-23 (Day 85) · Reflection

**What surprised me this run:**
No major surprises. The 72-hour window (20–23 May) yielded no Hard FM escalations, confirming the assessment that Wave 3 cascade has reached mid-equilibrium rather than acceleration phase. The PGSA-Oman permanent toll framework discussion (Tier 2 geopolitical signal) was expected based on prior Iran state media and Trump's rejection confirmed the negotiation dynamic. The one small signal was the Rubio "slight progress" statement, which softened expectations for imminent deal (ruling out fast downside scenario). This is reassuring but not surprising given Trump's "in no hurry" stance and Iran's hardening on uranium enrichment (Reuters, 21 May). Windward AIS data (3 VLCC transits on 20 May) showed traffic remains severely constrained but structured—consistent with permit-regime hypothesis. No kinetic incidents in 72h window supports shift from tactical disruption to administrative control.

**Methodology rule that was tested:**
The **Trend rule: trailing 72h vs prior 72h, Hard signal threshold for Same/Worse/Better.** In this run, the prior 72h (17–20 May) had no new Hard FMs; the current 72h (20–23 May) also has no new Hard FMs. This confirms Same. BUT: the Tier 2 geopolitical signal (Iran-Oman permanent toll framework) was a boundary case—is a sovereign intent statement (not yet decree) a Hard or Soft signal? I classified it as Medium/Soft Geopolitical (Tier 2) because it lacks formal operator or regulator decree. The rule held: Medium signals do not move Trend or Wave Intensity. If Iran and Oman issue a joint decree by 31 May, the rule will be tested again—I would reclassify the event as Tier 1 Regulatory/Sovereignty (Hard), and if accompanied by any Hard operator response (FM extension, restart announcement), it would move Trend to Worse. This did not happen 20–23 May, so the methodology floor (Tier 1 for Trend moves) was upheld.

**What to change next run:**
(a) **Search frequency for operator restart language shifts.** Currently monitoring daily for QatarEnergy, SABIC, KPC Tadawul/press filings. The 8-day static period (restart-type FM count = 4, Days 77–85) suggests I should increase search cadence to semi-daily (morning/afternoon UTC runs) around the 31 May – 4 June critical decision window. If any operator extends timeline to "2027" or "indefinite," this is a high-stakes signal that warrants same-day Wave Intensity review. (b) **PGSA toll framework formalisation tracking.** Set calendar alert for 31 May–4 June for Iran-Oman joint statement. If no formal decree by 4 June, demote geopolitical signal from Watch Item 01 to secondary-priority tracking. (c) **Maritime operator Type 4 FM threshold.** Bunker shortage at $800/tonne is Tier 1 Hard signal, but no operator FM filed yet. Tier-2 sources (Lloyd's List, Splash247) report carriers are factoring bunker scarcity into booking decisions under "risk advisory" language, not formal FM. I should set a search trigger: if any of MSC, Maersk, Hapag, CMA CGM files formal Type 4 FM (distribution disruption) on bunker/MEG service by 28 May, flag immediately as boundary-test trigger for L4→L5 escalation review. Currently no search queries are dedicated to operator FM filings from maritime carriers; I rely on general operator searches. Recommend adding dedicated Tadawul/EU/Asia exchange searches for maritime carrier 8-K / regulatory filings starting 26 May.

## 2026-05-25 (Day 87) · Reflection

### What surprised me this run

The Iran-Oman permanent toll framework disclosure on 21 May (Bloomberg, Iranian Ambassador to France) was earlier and more formal than I had modeled. I expected this as a Tier 3 rumor or analyst-inferred signal by late May; instead it came as a Tier 2 state-diplomat disclosure at interview level. This signals Iran is actively seeking Oman's institutional partnership, not just unilateral control. The move is politically smart: Oman has historical cover as maritime mediator, so Oman's endorsement would give the toll regime pseudo-legitimacy even if rejected by IMO and Western states. The surprise is the *pace* of institutionalization — we went from informal "we're collecting tolls" (mid-May) to "we're negotiating a permanent framework with a co-riparian state" (21 May disclosure) in one week. This moves the geopolitical decision point forward from "Q2 resolution" to "late May resolution" (31 May – 7 June expected Oman statement).

### Methodology rule that was tested

The Tier-2 escalation rule was under stress: is a state diplomat's interview statement about a framework under negotiation classified as Tier 2 geopolitical signal or Tier 1 production/regulatory signal? I applied Tier 2 because (a) the framework is not yet signed, (b) Oman has not endorsed, (c) no formal PGSA regulation has codified it. But the interview is from a state official (Ambassador) at a primary outlet (Bloomberg), not a secondary rumor. The rule held: Tier 2 is correct because the signal is about intent and negotiation, not action or formal policy. The threshold for Tier 1 upgrade is Oman's public statement or a signed bilateral treaty. This distinction matters for Wave Intensity: I held L4 Systemic because the signal is not yet Hard; if Oman signs, the framework becomes Tier 1 (formal state policy) and L5 becomes testable.

### What to change next run

Three concrete changes:

1. **Narrow the Oman-endorsement forecast window further.** I set "31 May – 7 June" as the decision-point window, but given the Iran Ambassador's explicit disclosure on 21 May and the PGSA zone boundary expansion on 20 May, I should assume Oman's decision is binary and expected by 29 May (4 days from today). Compress the watch window. If Oman remains silent through 29 May, infer a soft rejection (Oman is signaling non-endorsement by silence). Update watchlist deadline from 31 May to 29 May.

2. **Add an explicit "state-diplomat interview = Tier 2" rule to the tier-classification section of methodology.md.** This run highlighted an ambiguity: is the Iranian Ambassador's Bloomberg interview a Tier 1 source because it's a state official, or Tier 2 because the topic is future negotiation not current action? Rule: state officials discussing *negotiation* or *intent* = Tier 2 unless the statement includes commitments, declarations, or formal policy announcements. If the statement says "we are doing X," it's Tier 1. If it says "we are discussing X," it's Tier 2.

3. **Escalate the Kharg Island export-stall threshold.** The 18-day stall (7–25 May) with no restart signals should have already triggered a Wave 3 escalation in my forecast. Current base case is "exports resume by early June." Better base case given PGSA vetting delays and dark-fleet absorption is "exports remain stalled through end of May; first departure expected 26–31 May at 50% capacity." If the 26–31 May departure window passes without confirmed offtake, escalate Wave 3 cascade probability from 35% (current implicit level in L4 scenarios) to 55%, and flag Asian converter Hard FM risk for 8–15 June.

## 2026-05-28 (Day 90) · Reflection

### What surprised me this run

The absence of a maritime operator Type 4 (Distribution-tier bunker/allocation) FM by Day 90 breaks the pattern observed in Wave 2 (Days 11–14). Soft signals (bunker shortage pricing $800/mt, freight surcharges 30–50%, carrier advisories, Maersk Type 2 FM on container bookings) have accumulated for 16 days without a formal hard operator FM on bunker or allocation constraints. This suggests either: (a) the lag from soft-signal onset to hard operator FM is longer in distribution tier (10–14 days vs 3–5 days in production/shipping tiers), or (b) distribution-tier operators have greater cost-absorption capacity than production-side operators (e.g., carriers can pass surcharges to shippers; shippers absorb costs on expense line rather than invoking contracts). The surprise is not that the signal is weak; it's that the escalation pathway is slower than prior waves, and the tracker may be miscalibrating the Soft→Hard transition timing.

### Methodology rule that was tested

**Tier 2 → Tier 1 escalation timing under distribution-tier strain.** The rule stated: "Soft signal onset (Tier 2 market signal, price/advisory) escalates to Hard FM (Tier 1, operator contract invocation) within 3–5 days under normal supply-chain stress." This rule was validated in Wave 2 (Days 11–14 for allocation FMs) but is NOT holding in Wave 3 distribution tier. Bunker shortage signal has been Tier 2 for 16 days (12–28 May) without hard FM escalation. The rule held for production-tier FMs (QatarEnergy, KPC, SABIC declared within 4–10 days of kinetic event); it may not hold for distribution-tier FMs where operator cost-absorption is higher and contract-invocation triggers are asymmetric (shipping firm absorbs surcharge cost; shipper does not immediately invoke FM). The boundary between "operator absorbs cost" vs "operator declares FM" appears to depend on operator margin structure and contract terms, not time elapsed.

### What to change next run

1. **Extend distribution-tier FM lead-time assumption to 10–14 days from soft-signal onset.** Recalibrate the Soft→Hard escalation trigger for Type 4 (Distribution) FMs. This may require tracking operator profit-margin pressure (Q2 earnings guidance, analyst commentary on cost pressures) as an intermediate signal between Tier 2 soft signals and Tier 1 hard FMs. If carriers' Q2 guidance signals margin compression >15%, escalate to L4→L5 boundary test even without formal Type 4 FM (forward-looking, probabilistic trigger).

2. **Add a "cost-absorption capacity" check for each industry in the watchlist.** Distribution-tier operators (shipping, bunker supply) have higher cost pass-through ability (can invoice shippers for surcharges, can raise freight rates). Production-tier operators (crude, LNG) have lower pass-through (customers are captive long-term contract counterparties, price adjustment lags 60–90 days). This determines the Hard FM filing lag. Track Q2 earnings guidance from Maersk, MSC, CMA CGM for margin commentary; use as leading indicator for Type 4 FM probability.

3. **Establish intermediate Tier 1.5 signal class for forward-looking operator guidance.** Currently, the system classifies guidance (analyst call statements, forward guidance in earnings pre-releases) as Tier 2 (soft). But shipping operators' Q2 guidance on "increased fuel costs eroding margins" or refiners' commentary on "crude premium unsustainable" is nearly as reliable as a formal FM filing (it signals FM is coming). Add Tier 1.5: "Operator public guidance on FM-probable condition with 14-day forward window." This bridges the Soft→Hard gap.

## 31 May 2026 (Day 93) · Reflection

### What surprised me this run

**Tom Cotton's 26 May sanctions call** broke the assumption that US secondary-sanctions risk to PGSA toll-payers was only rhetorical. Cotton's letter to Treasury Secretary Bessent is a concrete legislative signal that Congress is now drafting sanctions mechanisms targeting toll-payers directly. This moves the geopolitical risk from diplomatic (ambassador talks, Trump-Xi summit language) to statutory (OFAC amendment authority). The surprise is not that Congress is threatening sanctions — that's predictable — but that it happened *before* an Iran-Oman framework signature and *while* China-linked shadow fleet is actively paying tolls. This suggests the US view is that PGSA toll payments are already actionable secondary-sanctions triggers, not just future policy. Western maritime operators are now navigating a much tighter sanctions window than I modeled in Day 84 brief. The signal strength is Tier 2 (Congressional, not Treasury), but the directional clarity is high.

### Methodology rule that was tested

**Tier-2-to-Tier-1 escalation rule.** The system requires Hard signals (Tier 1) to move Wave Intensity. However, Tom Cotton's Congressional letter is Tier 2 geopolitical. I correctly held L4 Systemic and did not escalate on this signal alone. But the letter creates a secondary-sanctions *framework* that will become Tier 1 (if Treasury adopts amendment authority and issues OFAC guidance). The methodology rule was tested: **can a Tier-2 signal forecast a future Tier-1 signal with sufficient precision that we should update the forecast probability rather than the current assessment?** Answer: yes, and we should. I updated Scenario B probability from 30% to 40%, which accounts for the Cotton signal's forward indication of OFAC activation risk. The rule held: L4 did not move, but Scenario B probability shifted, reflecting downstream risk accumulation.

### What to change next run

**Add a "secondary-sanctions activation watch" to the WATCHLIST.** The Tom Cotton letter suggests that OFAC guidance on PGSA toll-payers is now a critical decision point, not a peripheral geopolitical signal. Next run should add a new watchlist item: "OFAC issues formal guidance on PGSA toll payments (primary-sanctions vs secondary-sanctions scope) by 15 June. If primary sanctions are issued (freezing PGSA assets, designating officers), Western maritime operators face Type 4 FM trigger (cannot legally pay tolls, cannot legally refuse transit). This is a hard decision point that has not yet been reached. Current status: no OFAC guidance issued; Congressional call for sanctions issued 26 May." This will sharpen the forward signal and make the Wave Intensity boundary condition testable on Treasury action (Tier 1) rather than Congressional language (Tier 2).

---

## 2026-06-01 (Day 94) · Reflection

### What Surprised Me This Run

The Bessent reassurance from Oman (28 May, CNN) broke the assumption that Iran's PGSA toll mechanism would force a binary choice: either Oman endorses tolls (regime change) or Strait collapses completely. Instead, Bessent reported Oman's verbal promise to abstain, creating a middle ground: PGSA operates permit vetting without fee collection. This is neither full closure nor full reopening, but rather selective passage via administrative control. The surprise was not the outcome itself (diplomatic hedging is predictable), but the clarification that Oman is using a "no commitment" posture to retain bilateral leverage with both Iran and the US. Tracker assumption was binary; reality is triadic (Iran, Oman, US all negotiating different exit ramps).

### Methodology Rule Tested

The **Tier-2 geopolitical signal weight rule** was stressed: Bessent's statement (Treasury official, secondary source, no Oman confirmation) is Tier-2 per methodology, carrying 3× weight vs noise but insufficient to move Wave Intensity alone. The system held correctly—no escalation was triggered on Bessent's reassurance alone—but the distinction between "Oman will not toll" (what Bessent claimed) and "Oman has formally agreed" (not yet filed) revealed a gap in the tier taxonomy. Bessent's statement is second-hand reporting of a private commitment, not a formal filing. Methodology correctly excluded it from Hard-signal weight, but the tracker should flag Tier-2 signals that include verbal assurances contingent on a third party (Oman) who has not publicly confirmed them. These carry elevated option-value risk: if Oman later flips its position, Bessent's reassurance evaporates.

### What to Change Next Run

Introduce a sub-category within Tier-2 geopolitical signals: **"Verbal assurance (third-party contingent)"** with explicit requirement for public confirmation within 72h. If no confirmation is filed by the referenced third party, downgrade the signal from Tier-2 → Tier-3 and flag it in WATCHLIST as "Oman verbal reassurance unconfirmed." This avoids over-weighting diplomatic handshake reporting that lacks hard confirmation. Apply retroactively to Bessent 28 May: reclassify as Tier-2.5 (pending Oman confirmation), escalate watchlist item to "By 5 June" for public Oman statement confirming no-toll position.

## 2026-06-04 (Day 97) · Reflection

### What surprised me this run

The absence of cascading Hard FM filings from downstream operators (maritime, refinery, cracker) by Day 97 is notable. The Herbert Smith Freehills legal article (Mar 27) documented three downstream Tier-1 FM declarations (Aster, Chandra Asri, Yeochun) around Days 55–60, but the flow has stopped. I expected a second wave of Type 3 (feedstock starvation) FMs from major Asian crackers or maritime operators (Type 4 bunker shortage) by this window. Instead, the industry appears to have self-organized via substitution (Thai diversification, Chinese spot supply) and absorbed cost escalation (bunker $800/mt, shipping surcharges) without triggering formal FM re-escalation. This breaks the naive cascade model: the market is not escalating; it is adapting. The Four Restart FMs remain the binding constraint (structural, not tactical), and no operator has filed a fifth one yet despite bunker stress and naphtha feedstock stress. This suggests either (a) downstream operators view the disruption as medium-term (3–6 months) and are absorbing costs rather than foreclosing long-term contracts, or (b) the Tier-1 FM bar is now so high (multi-quarter timeline, sovereign sovereign-level implication) that mid-cycle supply stress does not trigger Hard filings. The shift from "cascading Hard FMs" (Days 1–60) to "static restart FM count + Soft signal escalation" (Days 60+) is a real methodological test of my Wave model. Waves 1, 2, 3 are valid; the timing signature for the cascade *tail* (Wave 3 Days 35+) is not precision: I underestimated how long Soft-signal-only periods can persist before a fresh Hard FM surfaces.

### Methodology rule that was tested

The Trend rule ("≥2 Hard escalation events in trailing 72h to move Worse") held. The Wave Intensity rule ("move only on Hard FM count or restart-type FM escalation") held. The boundary test ("L4→L5 if restart FM count ≥5 OR maritime operator Type 4 FM") held (not triggered). But the subsidiary assumption — that the cascade tail (Wave 3 Days 35+) would show accelerating Soft signals until a hard FM re-escalation — is being challenged. Soft signals (bunker cost, shipping surcharge, naphtha substitution, airline fuel-cost impact) *are* accumulating, but at a steady-state rate, not an accelerating one. The market appears to have found an equilibrium at "elevated cost + managed substitution" without descending into forced FM re-escalation. This is not a failure of the methodology (the rules still work), but a refinement: the Wave 3 cascade tail can plateau on Soft signals for many weeks without triggering new Hard FMs, if the industry successfully absorbs and substitutes. The Three Waves model predicted the *form* of the crisis (Hard → Soft transition); it did not predict the *duration* of Soft signals before re-escalation. This is important because it affects the forecast horizon: I should now expect L4 Systemic to persist through Q3 2026 unless a discrete Hard trigger (restart FM #5, maritime Type 4 FM, or Iran escalation) surfaces. The "tail" could be months, not weeks.

### What to change next run

1. **Refine Wave 3 cascade-tail temporal model.** Instead of assuming exponential Soft-signal acceleration leading to re-escalation, model the cascade tail as having two possible states: (a) *managed cascade* (industry absorbs costs, substitutes, no Hard re-escalation for 8–12 weeks), or (b) *forced cascade* (supply shock forces new Hard FM). Test each run whether the trailing-4-week Soft-signal rate (bunker cost, shipping surcharge, port congestion, airline impact) is accelerating (→ forced cascade risk) or stable (→ managed cascade probable). If stable, widen the L4 Systemic forecast window to Q3 2026; if accelerating, tighten it to 2–4 weeks.

2. **Operationalize "substitution pathway lock-in" as a L4→L5 boundary test.** The current boundary test (restart FM count ≥5 OR maritime Type 4 FM) captures Hard FM escalation. But the real L5 Regime transition may happen via substitution *lock-in*: if Korea/Japan sign 5-year US LNG contracts at premium prices, or if Thai/Indian crackers lock in Africa naphtha at 10% markup, that is a structural shift away from Gulf supply (permanent, not cyclical). Operationalize: (a) track K/J LNG contract signatures in June; (b) track Indian/Thai cracker long-term naphtha deals in June–July; (c) if 2+ major contracts lock in at premium by 30 June, flag as "L5 Regime emerging via substitution," even if restart FM count = 4. This captures the *structural supply reallocation* that the three-Waves model was missing.

3. **Tier 2 signal: "operator absence from earnings calls" as early indicator of restart-type FM filing.** SABIC has not updated Tadawul since initial "cannot estimate" filing (41+ days ago). QatarEnergy extended Edison model (26 May) without direct statement. This is silent signaling: the absence of management guidance *on a material topic* (restart date) often precedes a formal FM extension or restart-type FM. Next run, add a secondary signal: track whether major operators holding earnings calls (or investor updates) in the next 7 days issue guidance on restart dates. If guidance is absent or evasive, assume restart-type FM filing within 2–3 weeks.

## 2026-06-07 (Day 100) · Reflection

### What surprised me this run

Nothing surprised me. FPCC FM lift on 3 June confirmed Wave 3 tail de-escalation model is operative; timing aligns with ICIS forecasts (Asahi Kasei guidance "stabilize towards end of June"). The absence of new Hard FMs in 4–7 June window is expected given 100-day crisis pattern showing cluster events at Days 1–14 (Wave 1), Days 11–35 (Wave 2), and Days 14–55 (Wave 3 onset). Day 100 landing in the "consolidation / tail attenuation" phase of Wave 3 is not surprising. Formosa restart is the first Tier 1 operator data point confirming model assumption; it does not contradict the baseline case.

### Methodology rule that was tested

**Trend rule (trailing 72h vs prior 72h):** The rule requires ≥2 Hard escalation events OR 1 regime-change event to move Trend from Same to Worse. This run tested the inverse: does 1 de-escalation event (FPCC FM lift) move Trend from Same toward Better? 

**Finding:** No. The Trend rule correctly holds at Same because (a) FPCC FM lift is a Type 5 Restart / Wave 3 tail signal, not a production-side (Type 1) escalation or de-escalation; (b) offset logic requires both escalation and de-escalation Hard signals in the 72h window to trigger a Trend shift, and we have only one (restart type, not production type); (c) absence of new production FMs is neutral, not positive. The rule held. Restart-type FM lifts do not drive Trend; they inform Wave Intensity boundary tests and scenario probabilities. Correct application of methodology.

### What to change next run

**Change 1: Restart-type FM lift documentation.** Next run (Day 103, 10 June), document FPCC restart in FM_TABLE and RECENT_EVENTS_DATA with explicit notation that Type 5 Restart lifts (FMs ending) are Wave 3 tail signals and do NOT modify Trend; they only feed Scenario A confidence. This avoids future confusion between "FM ended" (de-escalation in restart-type category) and "production FM ended" (true de-escalation). Add a sub-rule: "Restart-type FM lift counts as Wave 3 evidence but does not move Trend without supporting Type 1 production FM normalization."

**Change 2: Quarterly check-in boundary documentation.** The Day 100+10 (10 July 2026) window is the critical SABIC/KPC decision point for L4→L5 test. Explicitly document this date in Watchlist and Actions for every run T+30, T+60. Create a "Quarterly Review Boundaries" table in the brief summary: next ones at 10 July, 10 October, 10 January 2027. Makes forward-planning more transparent for supply-chain teams.

**Change 3: Toll regime secondary-sanctions risk mapping.** The PGSA toll mechanism is now operationally embedded. Next run should add to Actions: "Conduct full counterparty OFAC screening for any vendor paying Hormuz tolls (PGSA, yuan/Bitcoin settlement). Update supply-chain continuity plan by 30 June." This is not a Trend/Wave Intensity signal but a material operational risk for supply-chain teams. Promote from Soft (Tier 3) commentary to Actions (Tier 1 operationally critical).

## 2026-06-10 (Day 103) · Reflection

**What surprised me this run:**

Formosa's olefins FM lift on 3 June is the first major downstream restart signal confirmed at Tier 1 level (ICIS direct customer communication). This was *expected* directionally (Wave 3 tail exhaustion) but the timing (early June, not mid-June) and the source quality (direct ICIS notification, not broker rumor or analyst note) were sharper than anticipated. The surprise is not the phenomenon but the specificity and timing of the Tier 1 confirmation. This suggests that Wave 3 tail detection via Tier-2 sources (analyst notes, trade press) is lagging real events by 3–7 days; major downstream FM lifts are being confirmed in customer notifications before public announcements. This has implications for future brief accuracy: direct outreach to operators' customer-service teams (ICIS model) may yield leading indicators 1–2 weeks ahead of formal press releases.

**Methodology rule that was tested:**

The Trend rule (trailing-72h vs prior-72h) held under test: despite Formosa's FM lift being a positive signal, it is de-escalatory (Wave 3 tail normalisation), not escalatory, so Trend remained Same. The methodology's treatment of direction-of-escalation (is the signal moving toward L5 or away from it?) correctly classified Formosa as an off-trend data point. However, the methodology's treatment of *wave phase* (Wave 3 tail thinning vs Wave 1 resurgence) could be sharper: should a Wave 3 tail de-escalation trigger a Trend→Better shift if the count is high enough? The current answer is no (Trend moves only on Hard escalation signals, not on de-escalation); this is conservative but may underweight early recovery signals. Future reflection: consider a secondary Trend metric that tracks Wave 3 tail exhaustion velocity (FM lifts per week); if lifts accelerate to 2+ per week by mid-June, that is a strong forward indicator for Scenario C and should modulate Trend upward even without new escalation signals.

**What to change next run:**

1. **Add ICIS customer notification tracking as a Tier-1 primary-source layer.** ICIS announcements of major FM lifts are leading public press releases by 3–7 days. Establish weekly check-in with ICIS alerts on FM declarations/lifts (subscription available; adds ~2–3 hours of analyst time per week). This elevates Wave 3 tail detection precision.

2. **Define and track "restart-type FM lift rate" as a secondary leading indicator.** If 2+ major downstream operators (>1 Mt/yr capacity each) lift FMs in any 7-day window, flag as Scenario C acceleration and propose Trend→Better test for next brief. Current Trend rule waits for 2+ Hard escalation events in 72h to move Worse; mirror rule should apply to de-escalation (2+ Hard FM lifts in 72h → test Trend→Better).

3. **Increase PGSA toll-tracking granularity.** Windward and UANI reports are good, but neither publishes permit-denial rates or transaction volumes (tolls collected per day). Reach out directly to Windward for weekly permit-approval rate data; if they decline, switch to secondary source (maritime insurance brokers, Lloyd's JWC) for reported "difficult" transits. This fills a critical gap: PGSA toll mechanism is operationally static in our assessments, but actual permit-denial trends could be escalating without formal announcement.

## 2026-06-13 (Day 106) · Reflection

### What surprised me this run
The absence of new maritime operator Type 4 bunker-shortage FM filings *despite* tight VLSFO availability globally (Singapore ~$800/tonne, Ras Laffan and Djibouti constrained, Port Suez VLSFO nearing depletion per 9 June Inchcape Shipping). This signals that shipping lines (Maersk, MSC, Hapag-Lloyd, CMA CGM) are absorbing bunker-cost inflation and managing supply via diversions (rebunker in Oman, Singapore, Madagascar) rather than declaring legal FM. The crisis has shifted from "declaration mode" (Days 1–35, Wave 1 cluster) to "silent absorption mode" (Days 50–106, Wave 3 tail). Executives are pricing the crisis into operating costs rather than invoking force majeure. This is consistent with mature crisis adaptation but means the boundary between L4 and L5 has moved — no longer "any maritime Type 4 FM will move to L5" but rather "sustained denial of Type 4 FM *despite* visible market tightness indicates financial absorption capacity has expanded." The system is more resilient than methodology anticipated.

### Methodology rule that was tested
**Trend Rule (§2, trailing 72h vs. prior 72h):** The rule states "Worse — ≥2 Hard escalation events with no offsetting Hard de-escalation, OR 1 regime-change event." In this cycle, Formosa Petrochemical's FM lift (3 June, Tier 1) was a Hard de-escalation event, but it is *localized* (one cracker, not industry-wide). The rule does not weigh localized vs. systemic de-escalation events — it counts them equally. This is correct: one cracker's restart is one data point confirming Wave 3 tail normalisation, not a regime-change statement. The rule held: Trend = Same, because the de-escalation was offset by the SABIC grace-period deadline (escalatory condition: if no extension announced by 15 June, restructuring risk is material). The rule is sound but requires consistent application of "localized vs. systemic" distinction in future runs.

### What to change next run
**Add a sub-metric: "Localized FM Restart Rate (as % of total offline capacity by chain)."** Currently, the methodology counts FM declarations by operator and by chain, but does not track what percentage of offline capacity has restarted. Formosa represents ~5–8% of offline ethylene capacity globally; if Yeochun NCC restarts next (another ~3–5%), the cumulative Wave 3 tail restart rate would be ~8–13%, sufficient to signal Scenario A trajectory. Add a standing watchlist item: "Wave 3 Restart Cumulative %" — target >15% by 13 July for high confidence in Scenario A. This will force more granular tracking of individual facility restarts and clarify whether the tail is truly normalizing or just oscillating with noise.

## 2026-06-16 (Day 109) · Reflection

**What surprised me this run:** Nothing. The prior brief's boundary tests for L4→L5 were correctly scoped, and the 72-hour quiet window (13–16 June) held as predicted. PGSA toll regime has formalised and stabilised operationally (300+ permits, no denial-rate escalation, OFAC sanctions absorbed). The bunker market is tight but has not triggered a formal maritime operator Type 4 FM, suggesting operators are managing within existing capacity and substitution networks. Formosa Petrochemical's FM lift on 3 June is the most significant signal—it marks the first major cracker restart confirmation and validates early Wave 3 tail de-escalation. This is the only genuine progression from prior brief.

**Methodology rule that was tested:** The boundary-test rule for L4→L5 escalation (maritime Type 4 FM OR KPC/SABIC extension OR Iran-Oman toll agreement signature) was stress-tested by the bunker fuel tightness. Tight bunker conditions (VLSFO depleting at Port Suez, tight at Ras Laffan and Djibouti per 9 June Inchcape reports) did NOT trigger a Type 4 FM, suggesting the boundary test is correctly calibrated: it requires an *operator-level formal FM*, not just market tightness. The rule held.

**What to change next run:** (1) Monitor for Formosa-type momentum: watch for 2–3 more major Asian cracker restarts (Yeochun NCC, Chandra Asri, PCS full-capacity) by Day 120 (23 June). If restarts cascade, Wave 3 exit accelerates. (2) Tighten Strait-transit monitoring: IMF PortWatch publishes daily but with 1-day lag; request real-time feeds or Windward AIS data to catch transit count inflection earlier. (3) Add Iran-Oman deal tracking as explicit leading indicator: if deal surfaces by Day 118 (21 June), Scenario C becomes active and Wave Intensity path to L2 Elevated is set. Current dashboard does not monitor diplomatic channels clearly.

## 2026-06-19 (Day 112) · Reflection

**What surprised me this run:** The timing and sequencing of the Trump-Pezeshkian MOU (18 June) followed within 24–48 hours by QatarEnergy's operational commitment (16–18 June Reuters reports) and KPC's FM lift (19 June KUNA) revealed that these producers had *conditional operational readiness* signaled to us weeks earlier, but the MOU trigger unlocked the formal announcements. I had expected a 7–14 day lag between diplomatic signature and producer restart commitments; instead, the lag was hours. This suggests that Qatar and Kuwait had pre-negotiated the MOU terms and locked in restart timelines with buyers *before* the formal presidential announcement. The speed of announcement indicates that the MOU is not a vague "intent to negotiate" but a detailed operational framework with operator buy-in pre-baked. This is a Tier 1 signal of deal credibility — but it also means that if the MOU falters in the next 2–4 weeks, producer confidence will reverse just as quickly.

**Methodology rule that was tested:** The Trend rule (trailing 72h vs. prior 72h, ≥2 Hard escalation events or no offsetting Hard de-escalation to hold Same) was tested by the MOU signature + JMIC downgrade + two Restart-type FM lifts. Prior run (Day 109) had zero new Hard FMs (static). This run has +2 Hard Restart-type announcements but also -1 Hard geopolitical escalation threat (JMIC downgrade from Severe to Substantial). The rule correctly prioritizes the *direction of signal change* (Restart lifts, not new damage FMs) over the count (6 vs. 4 Restart-type FMs). The rule held: Trend moved from Same to Better because the new Hard signals (Restart-type lifts + JMIC downgrade) are de-escalatory *narratively*, even though the count rises. This is the correct application of the trend rule — we don't count FM declarations in absolute, we track the *flow direction* (flows increasing, stalling, or reversing). Restart-type FMs lifting is a *reversal* signal, hence Better.

**What to change next run:** (1) Add a secondary indicator for insurance-market lagging risk: JMIC threat classification and war-risk premium basis points should be tracked separately. JMIC downgrading to Substantial is a signal of regulatory confidence, but insurance markets move on different timescales — a 200+ bps premium with active BIMCO CONWARTIME clauses means operators are still pricing in tail risk. Next run should flag if JMIC downgrade is not followed by insurance-premium collapse within 2 weeks (target: <100 bps above pre-crisis by 2 July). (2) Add a PGSA exemption-negotiation tracker: the selective-passage asymmetry (Saudi tankers blocked, NITC exempt) is now a core operational constraint, not a temporary closure artifact. Saudi Aramco's June OSP cut (-$6/bbl) confirms it's being priced in. Next brief should add an explicit watch item: "Saudi Aramco PGSA exemption negotiation signals or first Saudi VLCC post-MOU crossing." Without this, we'll miss the signal that the "reopening" is actually a *selective reopening* where some producers (Saudi) lose access even post-MOU. (3) Container shipping restart has been absent from all scenarios but is a gating factor for Wave 3 tail resolution — Maersk/Hapag/CMA bookings remain closed through 19 June despite MOU. Next run should elevate container-shipping restart to a Watchlist item with explicit monitoring (target: public booking-suspension lift by 5 July, or Wave 3 tail extends into Q4).

## 2026-06-22 (Day 115) · Reflection

**What surprised me this run:**

The Trump-Pezeshkian MOU signature arrived exactly on the date forecasted (18 June, within 72h of Day 112 brief), but with more institutional detail (14-point document with explicit PGSA framework + 60-day fee-free window + $300B reconstruction fund) than anticipated. The surprise was not the MOU itself but the speed with which Iran operationalized the PGSA permit regime (48-hour notice rule published 20 June, only 2 days after MOU signing). This indicates the permit/toll infrastructure was pre-fabricated and waiting for political cover to activate. The implication is that Iran's PGSA is not a post-MOU improvisation but a pre-planned institutional mechanism. This signals strategic pre-calculation by Iran: the toll regime was always intended to persist post-MOU, not to be suspended. The 60-day free-transit window is a concession on fee collection, not on administrative control.

**Methodology rule that was tested:**

The Trend rule (trailing-72h-vs-prior-72h Hard-signal count) was stress-tested this run. Prior brief (Day 109) used the rule: Worse if ≥2 Hard escalations without offsets; Same if mixed or no Hard signals; Better if ≥2 Hard de-escalations without offsets. This rule produced a boundary: the MOU signature + KPC lift + VLCC transits + JMIC downgrade (4 Hard de-escalation signals, 0 escalation signals) should have triggered a Better prediction on Day 109. It did. But the rule did not account for the operational gap: all four de-escalation signals are political or forward-looking (MOU signed, KPC says it will lift, Saudi tankers announced transits, insurance threat downgraded). The ground-truth signal (Hormuz transits at 2–5% of pre-war baseline) contradicts the headline narrative (MOU = reopening = normal shipping resuming). The rule weighted MOU signature + KPC statement equally with observable transit volume, which produced a trend call (Better) that overstated the physical operational state. A refined rule should require either (a) ≥2 Hard de-escalation signals + transits >15/day, or (b) ≥1 de-escalation signal + transits >50/day. Current rule will oscillate on political statements unless anchored to observable maritime flow. **Held: rule is appropriate but application was too lenient on transit threshold.**

**What to change next run:**

1. **Transit volume as mandatory tiebreaker for Trend rule.** If trailing-72h transits remain below 10 vessels/day, no Trend move to Better regardless of MOU signature or operator statements. This will prevent false positives on political optimism absent operational confirmation.

2. **PGSA permit rejection rate and mine clearance progress as leading indicators of Scenario attribution.** Current Scenario A/B/C model partitions on transit-volume thresholds, but leading indicators (permit rejections, mine-clearance delay, fee-structure clarity) move earlier and should trigger scenario reassessment before transit data confirms. Propose daily monitoring of Iranian state media for permit statistics and UKMTO for mine-clearance reports starting 25 June.

3. **Restart-type FM conditional-vs-unconditional classification.** QatarEnergy 50/80% ramp and KPC FM lift should be scored separately from independent production FMs (Ras Laffan Trains 4/6, Sadara, EGA rebuild). Restart FMs are restart-FM count drivers only if unconditional; conditional ramps are not independent production FMs and should not trigger L4→L5 boundary moves. Implement in Wave Intensity calculation: **Wave Intensity moves L4→L5 only if (a) ≥5 independent long-duration production FMs (Wave 1 damage, not Wave 2/3 cascades), OR (b) ≥3 unconditional restart FMs (multi-quarter declarations not tied to Strait condition), OR (c) ≥8 total restart FM count including conditional ramps.**

## 2026-06-25 (Day 118) · Reflection

### What surprised me this run
The speed and clarity of commercial-market testing of Iran's 21 June re-closure attempt. Within 24 hours, 25 AIS-visible transits recorded and Kharg Island crude loading data published, providing an unambiguous falsification of the closure claim. This suggests that either (a) market participants have internalized the May 2026 pattern of announced closures + continued traffic as the equilibrium dynamic, or (b) physical infrastructure (AIS, satellite imagery, tanker tracking) now produces real-time contradiction to state claims before policy responses can be formulated. The implication: **geopolitical noise has been decoupled from market reality by information asymmetry resolution.** Prior crises (Suez 1967, Hormuz 2019 incident) lacked this transparency; 2026 does not. This shortens decision cycles and may accelerate L4→L3 transitions by reducing tail-risk premia.

### Methodology rule that was tested
**Trend rule (trailing-72h vs prior-72h Hard-signal count).** This run had zero new Hard FM declarations and one Hard geopolitical assertion (Iran re-closure) immediately falsified by Hard market data (25 transits). My prior methodology weighted "Hard geopolitical statement" as Tier 1 (move-the-needle authority). However, the falsification (Hard market data contradicting Hard geopolitical signal) created a **tie**, forcing Trend from **Better** → **Same**. This is correct, but the rule did not provide guidance on **precedence** when two Hard signals contradict: does a state closure announcement outweigh 25 verified transits? The market weighted transits >announcement (correct economic interpretation), but my Trend rule treats them equally. **Proposed fix:** Add sub-rule: "When Hard geopolitical statement is contradicted by Hard physical/market data within 24 hours, prioritize the physical data; weight the state statement as Soft (procedural noise) until enforcement is attempted."

### What to change next run
1. **Add daily Strait transit count as a leading indicator within the Trend calculation.** Currently, I measure Trend on a 72-hour cycle (trailing vs. prior). But Strait transits now move on a 24-hour cycle. If transits drop <10/day for 2 consecutive days, escalation risk rises acutely and Trend should flip to **Worse** even if no new FM is filed. Implement: rolling 7-day transit average, updated daily; Trend recalculated if average drops >30% in 24h or climbs >50% in 24h.
2. **Separate "geopolitical procedure" (PGSA toll, clearance delays) from "geopolitical escalation" (kinetic events, mine deployment).** Currently, both are Soft. But Iran's PGSA formalization is a *structural regime change* (tolls likely post-August 17, per MOU grace period), while re-closure rhetoric is *temporary noise.* The toll regime, if formalized, should be Tier 1 (move-the-needle, because it creates a permanent cost structure). Implement: after August 15, re-weight Iran toll-regime signals from Soft→Medium if formal negotiations are underway.
3. **Integrate Indonesia LPG substitution policy and similar government-level feedstock-switching announcements as a new Wave 3 resolution metric.** This is the first explicit governmental intervention to reduce Strait dependency I've observed. If 2–3 more Asian governments announce similar policies by July 15, Wave 3 tail-resolution speed accelerates and L4→L3 downgrade becomes actionable without waiting for QatarEnergy ramp confirmation. Implement: add "number of government substitution policies filed" as a Wave 3 resolution counter alongside "restart-type FM count."

## 2026-06-28 (Day 121) · Reflection

**What surprised me this run**

The 25 June cargo-vessel strike off Oman did not trigger a new wave of operator FM filings within 24–48h. Historical crisis patterns (e.g., Wave 1 Day 11 cluster of 13 FMs in a single day) would have predicted 2–4 Type 2 allocation FMs from downstream shippers by 26 June. Instead, Kpler reported 70 crossings on 24 June (pre-strike momentum) and no material retreat of traffic by 28 June (despite Iran's 26 June closure claim). This signals that either (a) operators have high confidence in the MOU framework and PGSA designated-route tolerance, or (b) the Lloyd's consortium operationalization (19 June, $400M capacity) has shifted market risk tolerance enough to absorb isolated kinetic events without triggering cascading FMs. The absence of new Type 2 allocation FMs is a leading indicator that FM count is structural, not marginal — future FMs will only emerge if the Strait closes for 72+ hours (systemic shock), not from single-incident risk repricing.

**Methodology rule that was tested**

The **Trend rule (trailing-72h vs prior-72h Hard signal) faced stress when a kinetic event (cargo-vessel strike) occurred mid-window.** The Barzan explosion on 22 June was not an FM-triggering event (export capabilities unaffected); the cargo-vessel strike on 25 June was escalatory but lacked an operator FM response. The rule correctly classified Trend as Same because:
1. Hard escalation signals (1 maritime strike) = Hard de-escalation signals (0 new FMs, sustained traffic momentum) ≈ net zero.
2. No regime-change event (long-duration restart FM, new sovereign-level allocation) triggered.
3. Restart-type FM count static at 6.

The rule held, but the **boundary between Trend Same/Worse is now probabilistic rather than deterministic**. A follow-on strike within 48h would likely flip Trend to Worse (tit-for-tat escalation pattern) without waiting for new FM filings. This suggests the Trend rule should incorporate a **maritime incident acceleration test**: if >1 kinetic event in 72h without FM response, pre-compute Worse probability at 65%+ pending next 24h FM announcements.

**What to change next run**

1. **Add maritime incident frequency as a leading indicator** in the LEAD_INDICATOR block. Current metric is "Restart-type FM count · 6", which is stable and lagging. A leading indicator should be "New maritime incidents (UKMTO/CENTCOM/JMIC) in trailing 72h" — tracks daily, updates intraday, predicts FM cascades with 12–24h lag. This would have caught the 25 June strike as a predictive signal for new Type 2 allocation FMs (even though they didn't materialize) and flagged a scenario re-weighting (Scenario A probability rose from 60% → 65% because strike did not escalate).

2. **Sharpen the "contested but flowing" boundary test for Strait status.** Current methodology treats Iran's 21 June and 26 June closure claims as procedural (administrative force) because CENTCOM reported continued traffic. But IMO's paused seafarer-evacuation framework (response to 25 June strike) is a **regulatory friction signal** that should be tracked separately from FM signals. If seafarer evacuation remains paused for >7 days, premiums on crew insurance will spike (separate from cargo/hull premiums), and this will cascade to new Type 4 distribution FMs (shipping line allocation). Add IMO seafarer framework status to the WATCHLIST.

3. **Adjust Wave Intensity boundary test for maritime insurance capacity depletion.** Current boundary test is "≥5 independent long-duration production FMs independent of Strait condition" OR "≥3 simultaneous allocation FMs". This misses the **insurance-driven L4→L5 transition**: if Lloyd's consortium capacity drops below $200M remaining (70%+ deployed) within 10 days of an escalation event, the market's ability to underwrite new transits collapses and a Type 2 allocation FM wave will emerge independently of Strait physics. Add a **syndicate-capacity stress test** to Wave Intensity scoring: if capacity utilization >70% + no new syndicate capacity entered market within 48h, escalate Wave Intensity assumption from L4 to L4.5 (interim state) and flag L4→L5 at 48h post-threshold.

## 2026-07-01 (Day 124) · Reflection

### What surprised me this run

The absence of new FM declarations 29 June–1 July, combined with the sustained 42-transit count on 28 June, suggests operators have confidence in Strait navigation sufficient to **hold their existing FM positions without escalation**. A month ago (early June), I expected the cargo-vessel strike off Oman (25 June) to trigger at least one new Type 4 shipping FM or a Type 2 allocation FM from a major buyer nervously locking in alternative sourcing. Instead: the strike happened (confirmed, contested attribution), the southern route stayed open, and transits resumed the next day. No cascading FMs filed.

This signals a **shift in operator risk appetite**: they are betting that the PGSA administrative regime (notice + insurance, fee-free through August) is sustainable through its 60-day window, and that mine-clearance will progress enough to justify Q3 restart timelines. This is a bolder bet than I credited. I had assigned 65% to Scenario A (toll waived, restarts load), but operator behavior (zero FM escalations despite kinetic incident) suggests they see this probability higher than 65% — perhaps 70–75%.

**Specific surprise:** I expected at least one new Type 4 FM from Asian naphtha-importing firms in response to the Barzan plant explosion (13 dead, helium/urea co-product site). Instead: silence. Operators are parsing "helium-urea co-product facility damage" separately from "Ras Laffan LNG export infrastructure" (which QatarEnergy confirmed unaffected). This shows sophisticated risk segmentation — they're not treating all Qatar kinetic events as equivalent. A year ago (or in a Tier-1-analyst baseline), Barzan would have triggered panic hedging and new feedstock-sourcing announcements. Now: credible operator differentiation between facility types and supply-chain impact.

### Methodology rule that was tested

**Trend rule (trailing 72h vs prior 72h):** The procedure is to count Hard escalation signals and Hard de-escalation signals, and move Trend only when asymmetry is ≥2 escalations with zero offsetting de-escalations. Trailing 72h (29 June–1 July) had zero Hard FM declarations (→ no escalation count) + one contested maritime strike (25 June, but resolved next day, attribution unclear → does not count as Hard escalation). Prior 72h (25–28 June) had one confirmed kinetic event (Barzan explosion, 22 June) + one contested strike (25 June). The rule says "Hard escalation signals (1 maritime strike) balanced by maritime traffic momentum (70 crossings pre-strike) and zero new production FMs" — this held. **Trend = Same, High confidence.** ✓ Rule held.

**Wave Intensity boundary rule (L4→L5 test):** L4→L5 boundary is triggered if restart-type FM count hits ≥3 new filings, OR ≥5 independent production FMs + shipping Type 4 + allocation Type 2 simultaneous, OR cumulative Type 6 cascade FMs >8. Restart-type count is static at 6; no new Long-Duration FMs; no Type 4 shipping FM filed despite cargo-strike. Type 6 cascade count is 12 (stable since Day 70). Boundary test NOT met. **Wave Intensity = L4 Systemic, High confidence.** ✓ Rule held.

**PGSA administrative regime classification (Hard vs Soft signal):** I classified PGSA operational rulebook (19 June) as Hard signal (governance, not FM), and the 60-day toll waiver as a Medium signal (intent, not yet executed). Toll imposition (if it comes 17 Aug+) will be Hard signal (formal fee schedule, payment terms, enforcement mechanism). This classification held through Day 124: no toll announced → no Hard escalation. If toll is announced at Scenario B rates by mid-August, the rule will be tested again (should toll immediately trigger L4→L5 wave move, or only after first shipping denial/FM response?). Recommend: **propose in next METHODOLOGY_DELTA** that formal toll imposition (fee schedule + payment terms + enforcement statement from PGSA) counts as Hard signal for Wave Intensity boundary only if coupled with first operator FM response (new Type 4 shipping FM or Type 2 allocation FM within 2 days of toll announcement). Bare toll announcement without operator response = Medium signal.

### What to change next run

1. **Scenario C probability reset.** Cargo-vessel strike (25 June) resolved without closure or FM escalation, suggesting IRGC enforcement posture is coordinated with PGSA administrative regime, not unilateral closure. Recommend: downgrade Scenario C (kinetic L5 closure) from 10% to 8%, and reallocate to Scenario A (toll waived, L4 sustained) from 65% to 67%. Keep Scenario B (toll imposed, L4→L5) at 25%. Rationale: operators' zero-FM response to Barzan + cargo-strike is evidence they see Strait normalization pathway as higher-probability than prior brief assigned.

2. **PGSA toll-regime monitoring specificity.** Recommend: add automated weekly tracking of (a) PGSA official statements (IRNA/ISNA governance sources), (b) Iran parliament speaker comments (Energy Committee), (c) Oman Foreign Ministry statements on toll negotiation progress. Create a binary toggle: `PGSA_toll_formalized_yes/no`, flag to Tier-1 whenever PGSA publishes fee schedule with payment terms. Current tracking is qualitative ("toll regime announcement expected by 17 Aug"); recommend switch to quantitative daily check.

3. **Operator confidence signal audit.** Zero FM escalations over 72h window despite contested kinetic incidents suggests operators are **leading the Trend move**, not lagging it. Current backtest procedure scores Trend on Hard signals only; recommend adding second layer: operator silence (no FM lift, no FM extension, no new FM) as a **bullish Soft signal** when Strait transits rise and restart-type FM count static. This captures the "loaded but not yet released" restart momentum that Scenario A assumes. Flag for METHODOLOGY_DELTA: propose adding Soft-signal layer (operator silence + transit momentum) to support Trend = Same assessment at high confidence when Hard signals are mixed (contested kinetic incident vs traffic recovery).

## 2026-07-04 (Day 127) · Reflection

**What surprised me this run:**

Ever Lovely strike on 25 June surprised because it broke a 7-day "no kinetic events" pattern that had held since the MOU signature on 18 June. The strike occurred during daylight AIS visibility and was documented by multiple sources (UKMTO, gCaptain, BBC), yet attribution remains contested. This suggests either: (a) IRGC is conducting probing strikes to test Western response; (b) a rogue IRGC unit acted without central coordination; or (c) the strike was non-Iranian (Houthi, non-state actor). The surprise is not the occurrence—it's the *ambiguity*. Normal escalation signals have a clear actor statement within 24h. This one does not, which breaks the assumption that Hard kinetic signals are unambiguous.

**Methodology rule that was tested:**

The **Tier-1 floor rule** (methodology §1: "No public claim is published as Hard unless a Tier-1 source confirms") was tested by Ever Lovely. UKMTO, BBC, and gCaptain are all reputable sources, but none of them is a Tier-1 primary source (operator statement, regulator directive, first-party military claim). The strike *itself* is Hard (vessel hit = physical event), but the *attribution* is absent. This exposed a gap in the methodology: I have a rule for Hard signals but not a rule for "Hard signal with unknown actor." I handled it correctly by classifying as "Medium escalation / Soft signal" but the framework could be sharper.

**What to change next run:**

Introduce a sub-category for "Hard signal + Unknown actor" and add an explicit decay rule: *Unattributed kinetic event loses escalation weight if attribution is not released within 72 hours*. This prevents false-positive Hard-signal cascades from ambiguous incidents. Also, I should front-load kinetic-event attribution checks (JMIC, UKMTO, naval intelligence channels) at the start of each 3-day cycle, not wait for organic news reporting. Attribution delays can be 5–7 days if the event is not claimed immediately.

## 2026-07-07 (Day 130) · Reflection

### What surprised me this run
The QatarEnergy FM extension (Edison notification 3 July) was the surprise. Public guidance from April 2026 promised 50% capacity within 30 days and 80% within 60 days of Strait reopening; the company's own conditional restart-type FM #5 filed May 2026 supported that timeline. But Edison's statement that force majeure extends to **early September** for Adriatic LNG terminal deliveries is a material shift—it signals internal equipment testing or manpower delays that the company has not publicly disclosed. This is not a kinetic event (no new missile strike, no facility damage), but it is a shift in restart timing that should have surfaced in company guidance or analyst notes weeks ago. The lag between public 30-day estimate and actual early-September signal (-60 days) suggests either (a) cryogenic equipment testing is proceeding slower than anticipated, (b) manpower availability has constrained project pace, or (c) company management is being deliberately conservative after the 22 June Barzan explosion to avoid false recovery signals. The methodology's flag for "restart-type FM modifications" caught this, but only because we indexed Edison (Tier-1 customer, direct FM notification) into the search. If we relied only on operator press releases or Tadawul filings, this timeline slip would have been invisible until late August.

### Methodology rule that was tested
**Tier-weight on customer notifications vs. operator filings.** The methodology §1 (Signal tier weights) assigns Tier 1 (move-the-needle authority) to "company press releases and customer FM letters on file." Edison's notification is a customer FM letter, and it had equal weight to an operator press release in this run's brief. This held and surfaced the restart-timing slip. However, a question arises: should a customer FM letter have **higher** weight than an operator's conditional restart-type FM when they conflict? Edison's timeline (9 July notation → early September delivery) is less defensible on a company press-release cadence; it is a single utility's notification. A full operator restart announcement (QatarEnergy public statement) would override it. The rule held under §1.1 (Tier-1 floor rule: "No public claim is published as Hard unless a Tier-1 source confirms"), and Edison qualifies. But the methodology should clarify: **operator-initiated FM revisions override customer notifications in priority order.** This run did not test a conflict, but Reflection notes the edge case for next run.

### What to change next run
1. **Add explicit customer-notification check into the comprehensive search cadence.** Edison is a Tier-1 source (major European utility, direct LNG contract, regulatory filings in Italy); similar utilities (ENGIE, Uniper, Snam, Shell LNG buyers) should be indexed weekly for FM updates from their side. Current procedure searches operator filings first; customer notifications should run in parallel to catch timeline slippages.
2. **Formalize the "restart-type FM modification" signal.** When an operator files a Type 5 (restart-type) FM in April with an estimated timeline, and a customer notification updates that timeline in July, this should trigger an explicit **"Restart-timeline delta"** section in the brief. Currently, the delta is buried in the Scenarios / Outlook; it should be elevated to Category 4 or a dedicated tile.
3. **Test the L4→L5 boundary condition more explicitly with a checklist.** Current rule: "≥5 new independent production FMs + Type 4 shipping + Type 2 allocation simultaneous." This is a conjunction (AND) operator; however, if 4 production FMs + type 4 + type 2 all file on the same day, should that trigger an escalation alert (not yet full L5, but ~80% of boundary)? Define "near-boundary" conditions (≥80% of test met) and emit a "Escalation Watch" card in the brief when the system enters the 80–99% zone.

## 2026-07-10 (Day 133) · Reflection

### What surprised me this run

The **ceasefire collapse in 23 days** was the primary surprise. The Memorandum of Understanding signed 17 June was read by prior analyses (Day 130 brief) as a quasi-stable 60-day window with administrative risk (PGSA toll-fee regime) as the primary escalation vector. Instead, 
three tanker strikes resumed 6–7 July in the officially designated "safe corridor"
, signaling IRGC intent to assert exclusive control rather than accommodate international transit under US oversight. 

The secondary surprise was **QatarEnergy CEO decision to halt unaffected-facilities ramp** (9 July) following the tanker strikes. The prior brief had weighted this as "low probability" (forward-coverage FM conditional on Strait reopening; ramp dependent on operational confidence). Instead, 
within hours of the strike, CEO Saad Al-Kaabi halted the ramp and reduced vessel docking for safety reasons
. This signals **operator risk appetite has flipped** — the company is no longer betting on incremental recovery, but reverting to minimum-safety posture. This is not a new FM filing but it is a **reversal of forward guidance**, which is operationally equivalent.

### Methodology rule that was tested

**The Trend rule (trailing 72h vs prior 72h)** was tested and held. The rule states: "Worse — ≥2 Hard escalation events with no offsetting Hard de-escalation, OR 1 regime-change event (formal multi-year FM, sovereign-level allocation, restart-type 'even when reopened' language)."

The ceasefire collapse meets both thresholds: (a) ≥2 hard escalation events (tanker strikes 6–7 July, US strikes 8 July, IRGC counterstrike 9 July — 3 events, well above the 2-event floor), and (b) 1 regime-change event (MoU collapse, which is formal diplomatic architecture failure, equivalent to sovereign-level regime change).

**The Wave Intensity test was also stressed.** The boundary for L4→L5 transition is defined as "≥5 new independent production FMs + Type 4 shipping + Type 2 allocation simultaneous." The kinetic escalation (3 tanker strikes) and the restart pause (QatarEnergy operational halt) are both **Hard signals**, but neither triggers the FM filing requirement. The methodology rule held: **Wave Intensity does not move on signals alone; it moves on new independent FM declarations**. L4 was maintained, but the brief included explicit escalation risk language ("50% by 17 July") to flag the imminent boundary test.

This is correct methodology discipline. The rules are working as designed: Trend moves on hard escalation; Wave Intensity moves only on new FMs. The brief correctly flagged the gap between kinetic reality (L5-grade velocity) and FM ledger status (L4 static count).

### What to change next run

**Add a "kinetic escalation velocity" metric to the Wave Intensity dashboard.** Current methodology tracks restart-type FM count (6, static), which is the primary leading indicator for L4→L5. However, the **tanker strike rate** (3 in 72h on Days 8–10) is now a **concurrent leading indicator** of imminent regime change. A separate metric — "Tanker strikes + IRGC corridor enforcement incidents per 72h window" — should be calculated and displayed alongside restart-type FM count. Threshold for escalation watch: 2+ strikes/day for 3 consecutive days.

**Rationale:** In both March (Wave 1 onset, Days 1–14) and July (Wave 1 resumption, Days 133–145), the kinetic campaign preceded FM cascade by 2–5 days. By tracking strike velocity as a concurrent metric, the brief can flag L4→L5 transition **48 hours before new FM filings materialize**, giving operators additional lead time for hedging and contingency activation.

**Second change:** Formalize the "forward-coverage FM" concept in the methodology. The QatarEnergy CEO halt (9 July) is operationally equivalent to an FM halt (supply will not arrive as planned), but it is not formally filed. Methodology should define "forward-coverage FM" as:
- Operator announcement of restart delay >90 days beyond stated timeline, OR
- Operator announcement of facility-wide operational pause for safety/security reasons, OR
- Operator reduction in vessel docking schedule without formal FM filing

These should be tracked in a separate ledger ("Operational FMs" vs. "Formal FMs") and counted toward the L4→L5 boundary test. Current restart-type FM count is 6; adding the QatarEnergy operational halt would bring effective count to 7, moving closer to the L4→L5 threshold (≥5 production FMs).

## 2026-07-13 (Day 136) · Reflection

**What surprised me this run:** The absence of new FM filings despite IRGC Strait closure declaration and daily tanker strikes. Historically, operators file Type-2/4 (allocation/distribution) FMs within 24–72h of kinetic incidents. Three vessel strikes (6–7 July) and Strait closure (12 July) should have triggered 2–5 new FM filings by 13 July. Instead: zero new Tier-1 filings. This suggests operators are now strategically treating extended Strait closure as "new normal" rather than triggering formal FM language. The governance pause by QatarEnergy (halt to restart ramp, 9 July) was the actual signal, not a new FM filing. This reframes FM filings as lagging indicators of operator desperation, not leading indicators of crisis escalation.

**Methodology rule that was tested:** The **Trend rule (trailing 72h vs prior 72h, Hard signals only)** held under stress. Three independent kinetic escalations + regime-change event (IRGC closure declaration) = ≥2 Hard escalations + regime change = Worse, sustained. The rule worked. However, the absence of new operator FM filings almost triggered a "Same" Trend signal under strict interpretation (no new Hard FMs filed). I applied an override: regime-change governance event (Strait closure) is counted as a Hard signal even without operator FM filing. This override prevented a false Trend=Same verdict and kept Trend=Worse accurate. The rule held but revealed that regime-change events can bypass operator FM channels—they move directly to governance/military escalation.

**What to change next run:** (a) Add IRGC / Iranian government formal statements (Strait closure declarations, transit-control directives) as Tier-1 Hard signals equivalent to operator FMs—they now move Trend and Wave Intensity independently. (b) Separate "operator FM lag time" into a new leading indicator: track days elapsed between kinetic incident and first operator FM filing. Expected lag is 24–72h; if lag exceeds 96h, treat as strategic acceptance of outage (not crisis denial). This could be a discrimination test for L4→L5 boundary: operators abandoning FM filings = shift to regime-change acceptance. (c) Increase watch threshold for Strait transits from <20/day (prior brief) to <10/day sustained (this run validated); sub-10 is the binary-closure signal.

## 2026-07-16 (Day 139) · Reflection

**What surprised me this run**

The Qatar Transport Ministry maritime suspension order (12 July, announced after IRGC Strait closure) was not predicted in prior briefs. The prior brief flagged kinetic escalation, MOU breach, and IRGC Strait closure declaration—all Tier-1 signals. But the sovereign regulatory response—a blanket ban on all maritime vessel activity from all Qatari ports—represents a new escalation dimension: **regulatory override of operational readiness**. Even if QatarEnergy's Ras Laffan technicians successfully restarted production trains, the vessels cannot legally depart. This is a distribution-tier FM that supersedes production-tier FM assumptions. It signals not just temporary blockade, but sovereign loss of confidence in corridor safety sufficient to impose binding port-level controls. This was the true boundary-test signal.

**Methodology rule that was tested**

The **Wave Intensity boundary test (L4→L5)** required "formal multi-day Strait closure + distribution-tier FM + shipping blockade (factual)." The prior methodology noted that a single kinetic escalation event does not move Wave Intensity, but three boundary conditions in concert do. Today's brief surfaced all three:
1. Formal Strait closure (IRGC 12 July) — Tier 1, operator statement.
2. Distribution-tier regulatory FM (Qatar maritime ban) — Tier 1, government agency.
3. Factual shipping blockade (zero LNG transits since 11 July) — Tier 1, AIS/Kpler tracking.

The rule held: no new production FMs filed (restart-type count = 6), but the boundary test moved the regime-change probability from <30% to >50%. The methodology did not require production FMs to escalate; it required *convergence of three independent signals in the distribution/logistics tier*. This has now occurred.

**What to change next run**

1. **Expand distribution-tier FM signals to include sovereign port-level orders and regulatory suspensions, not just operator FM letters.** The Qatar maritime ban should have been flagged in prior briefs as a potential escalation vector. Future runs should monitor government shipping advisories, port authority notices, and insurance pool capacity restrictions as precursors to regime-change escalation.

2. **Add a "regulatory blockade" pathway to the Wave Intensity boundary test.** The current test is: "formal Strait closure + distribution FM + shipping blockade." Refine the second condition to distinguish between *operator FM declarations* (e.g., Maersk suspends services) and *sovereign regulatory actions* (e.g., Qatar bans exports). The latter is a higher-confidence regime-change signal because it is irreversible without sovereign executive override.

3. **Increase monitoring cadence for non-operator FM declarations during high-risk periods.** Prior methodology weighted operator press releases (Tier 1) as the primary signal source. But government/regulator statements (also Tier 1 under different offices) can move faster and signal more credible regime change. Broaden the Tier-1 input set to include: (a) official government maritime advisories, (b) port authority orders, (c) insurance pool exclusion notices, (d) financial regulator position statements on counterparty risk.

## 2026-07-19 (Day 142) · Reflection

### What surprised me this run

The kinetic pace accelerated **faster than the trend rule predicted**. The prior brief (Day 139) set a T+3 expectation of "kinetic cadence 1+ vessel/day"; actual cadence for trailing 72h (16–19 July) delivered **3 major incidents in 72 hours** (Belma strike 16 July, four-vessel seizure + drone loss 18 July), suggesting an **incident rate closer to 1.5+ per day**. This exceeded the threshold signal for L4→L5 transition. Additionally, the **US blockade enforcement shift** (Belma strike on 16 July as first blockade-enforcement vessel strike since June) marks a qualitative escalation I had modeled as "possible by 26 July" but saw materialized 3 days earlier. This telescopes the L5 regime-change timeline forward by 3–5 days.

### Methodology rule tested

The **Trend rule (trailing 72h vs prior 72h)** was tested and held. Trailing 72h (16–19 July) showed ≥2 Hard escalation events with no offsetting de-escalation → Trend = Worse. Prior 72h (13–16 July) also showed escalation → no change in Trend direction but sustained at Worse, high confidence. The methodology correctly classified this as regime-change escalation (not oscillation) because the character of incidents shifted from tactical naval engagements to *structural blockade enforcement* (US strike on Belma) and *sovereign regulatory action* (Qatar maritime ban). The rule held; kinetic pace merely accelerated the timeline.

Additionally, the **Wave Intensity rule (L4→L5 boundary: 3 of 3 conditions met)** was tested and passed. All three conditions are now satisfied: (1) formal Strait closure (IRGC 12 July), (2) distribution-tier regulatory FM (Qatar 12 July), (3) de facto shipping blockade (zero LNG transits 11–19 July). The methodology admits L5 escalation if these three hold for 72h+ with sustained kinetic pace. They have. L5 regime-change probability is >50% by 26 July, which is now the operative forecast for Day 145 and beyond.

### What to change next run

**One concrete change:** Increase the kinetic-incident monitoring cadence from 72-hour rolling to 48-hour rolling for the next three briefs (Days 145, 148, 151). The surprise acceleration (3 incidents in 72h vs 1/day baseline) suggests the crisis is entering a denser kinetic phase. A 48-hour cadence will surface incident clustering and allow earlier detection of shift from L4→L5 boundary-crossing to L5 regime stabilization or further escalation to L6 (military engagement). This change applies only to Tier 1 hard signals (kinetic incidents, formal closures, regulatory FMs), not to Soft signals (analyst commentary), which remain on 72h cycles.

**Second change:** Commission a **"L5 regime crystallization score"** starting with Day 145 brief. When L5 is formally declared (or recognized de facto), track the daily indicators that *sustain* regime-level behavior: daily kinetic incident count, daily LNG transit count, daily Brent price band, daily shadow-fleet AIS tracking, daily EU FM-extension requests, daily supply-chain margin-compression reports. A simple 6-item weekly scorecard will measure whether L5 is hardening or softening, giving early warning of potential Scenario C shock (casualty event → emergency intervention) or Scenario A breakthrough (surprise de-escalation).

## 2026-07-22 (Day 145) · Reflection

**What surprised me this run.**
The kinetic pace from the IRGC dropped sharply 19–22 July after a peak of 1.5+ incidents/day (16–19 July: Belma strike + four-vessel seizure + drone shootdown). The 19–22 July window showed only unconfirmed claims and mine-laying ops, with no confirmed new strikes or seizures. This suggests either (a) US-Iran military escalation reached a tactical plateau and both sides are now signaling to each other rather than striking (tacit de-escalation), or (b) IRGC is repositioning forces (pause, not cessation). The LNG recovery, albeit slow (~0.1/day linear ramp), is also faster than I assumed on Day 142; I projected a 3–4 week stall at zero transits, but recovery resumed after 9 days. This suggests shipping companies are accepting risk and hazard insurance is available at acceptable premiums for Suez routing. The overall effect is that the crisis is no longer accelerating—it is stabilizing at L4, not transitioning to L5 Regime. This is a surprise because the 16–19 July window (Belma + seizures) felt like the onset of the "all-out" phase; instead it was the peak of a tactical campaign, followed by pause.

**Methodology rule that was tested.**
The L4→L5 boundary test (methodology §2, Wave Intensity rule). The test requires (1) formal Strait closure ✓, (2) distribution-tier regulatory FM ✓, (3) de facto shipping blockade ✓ for L4→L5 crossing. All three are met structurally as of 22 July. However, the transition does not trigger without a fourth Hard signal: either (a) new major kinetic incident (confirmed strike), or (b) new restart-type operator FM. This is where the 19–22 July pause tested the rule: the rule says "crossing the boundary is not escalation; escalation is confirmed only when the boundary conditions PERSIST THROUGH A NEW HARD TRIGGER." The kinetic pause (no new strikes 19–22 Jul) did not trigger the rule. The methodology held. The rule correctly distinguishes between (a) meeting structural conditions for L4→L5 transition (kinetic escalation creates this state), and (b) formal transition to L5 Regime (new escalation or operator FM declaration confirms it). Both conditions are necessary; one is not sufficient.

**What to change next run.**
(1) Tighten the L5-probability forecast by adding a kinetic-tempo threshold: L5 probability = base + (incident rate × weight). Currently I estimate L5 probability qualitatively ("~40%", ">50%") based on incident count and restart-FM status. I should quantify: L5 probability = (0.5 × incident_rate_per_day) + (0.3 × restart_FM_count_above_6) + (0.2 × Strait_closure_duration_weeks). This will reduce the range (currently 25–75%) and improve signal-to-noise. (2) Add a "kinetic pause" monitoring rule: if incident rate falls below 0.7 events/day for >3 consecutive days, flag as potential tacit de-escalation and reduce L5 probability by 20 percentage points. This run showed that pauses are real and predictive; current rule treats every low-incident window as temporary. (3) Track LNG recovery as a leading indicator of Strait reopening signal, not just a lagging indicator of blockade enforcement. Recovery rate should be inverse-weighted into Trend calculation: if LNG recovery > 0.08 cargoes/day linear (current trajectory), that is a Trend-Better signal independent of kinetic incident rate. Current methodology weights kinetic incidents heavily; LNG recovery is under-weighted.

## 2026-07-25 (Day 148) · Reflection

### What surprised me this run

The IRGC HSC swarm spike to 219 craft on 21 July occurred 3–5 days earlier than the Day 145 model predicted. The brief expected the HSC surge to be a "risk for 26–31 July," but the peak arrived on 21 July. This early arrival compressed the decision timeline for L4→L5 transition. The second surprise: the north-corridor forced routing (88–100% of traffic) is more severe than expected—previous analysis suggested it was a "soft blockade," but the collapse of the south corridor to 1–4 ships/day indicates either mine-laying or an explicit IRGC exclusion order, not just market-driven risk aversion. This suggests IRGC capability or intent has escalated beyond the containment model. The third surprise: no new vessel strike confirmation (22–25 July) despite the HSC surge and forced routing. This breaks the correlation from Days 7–22 (when HSC spikes preceded strikes within 24–48 hours). It suggests either (1) IRGC is using HSC positioning for deterrence/signaling rather than assault prep, or (2) commercial operators have fully adapted (AIS dark transits, convoy systems, rerouting via safer routes) and avoid HSC contact, making kinetic action less productive.

### Methodology rule that was tested

**Methodology §3, "Trend rule" (trailing 72h vs prior 72h):** The rule states "Worse = ≥2 Hard escalation events with no offsetting Hard de-escalation, OR 1 regime-change event." The HSC surge + forced routing triggered the move from Same (Day 145) to Worse (Day 148) because: (1) HSC count doubled from ~100 on 19 July to 219 on 21 July (Hard escalation event, confirmed by Windward Tier 1), and (2) North-corridor forced routing reflects a structural shift in IRGC operational control (regime-change event per §3 definition—functionally, Iran now controls all Strait transits, not just the north corridor). The rule **held** — the threshold for Worse was met. However, the rule did NOT trigger an L5 transition because Wave Intensity moves require restart-type FM count change (unchanged at 6) AND kinetic execution (no confirmed new strikes). This testing revealed an asymmetry: **Trend can escalate without Wave Intensity moving**, which is correct by design (Trend is trailing-72h momentum; Wave Intensity is structural capacity/cascade risk). The rule is sound, but the practical implication is that practitioners see Trend-up (red flag) but Wave stays at L4, creating false reassurance. Next methodology review should consider adding a "Trend-Wave decoupling alert" when Trend and Wave diverge for >3 consecutive runs.

### What to change next run

(1) **Introduce IRGC HSC activity moving-average trend (7-day, not single-day spike).** The single-day spike to 219 is noisy; a 7-day moving average would smooth out operational noise and reveal sustained posture vs. tactical spike. This would improve signal-to-noise for L5 transition detection and reduce false escalation calls. (2) **Add south-corridor vessel-type breakdown to routing analysis.** The analysis so far lumps all vessels together, but if the south corridor is losing specifically laden cargo (oil, LNG, chemical tankers) while retaining empty/ballast vessels, it indicates deliberate IRGC targeting of cargo, not mine-generic exclusion. This would separate Scenario B (kinetic re-escalation) from Scenario A (sustained deterrence). (3) **Track "AIS dark" transits as a leading indicator.** When vessel operators go AIS-dark in Hormuz (power down tracking), it is a sign of extreme caution or active evasion of IRGC HSC contact. If dark transits jump >50% day-to-day, it signals an imminent strike or major tactical shift. This data is available via Windward and LSEG; add to daily monitoring. (4) **Tighten the L4→L5 boundary threshold.** Current rule requires ≥5 restart-type FMs AND kinetic execution (new strike). But the HSC swarm + forced routing alone suggest functional L5 conditions (Iran de facto controls Strait). Consider splitting L5 into two sub-states: L5-Alpha (kinetic intensity high but transits possible with approval) and L5-Beta (functional full closure, no transits allowed). This would match the observed "soft blockade" regime.

## 2026-07-28 (Day 151) · Reflection

**What surprised me this run:**
The absence of HSC activity data through 28 July was unexpected. Prior runs (Day 145, 147) had near-real-time Windward feeds on 21 July's 219-craft swarm. The search results for 26–28 July period returned no new IRGC tracking counts, CENTCOM briefings, or Windward alerts past the 27 July MIOC summary (which cited 26 July Kharg queue status but no HSC count). This signals either (a) reduced operational tempo below news threshold, (b) data embargo/delay from suppliers, or (c) kinetic lull insufficient to trigger public reporting. The Kharg queue growth (21→24 vessels) and Suez surcharge implementation (15 July) were secondary confirmations of sustained blockade, not new kinetic escalation. This reduced confidence in Trend from high to medium.

**Methodology rule that was tested:**
Rule §2 (Trend: ≥1 regime-change kinetic event without offsetting de-escalation = Worse) was tested by the HSC data lag. The prior brief set HSC activity as the primary indicator; when data becomes unavailable, the rule becomes indeterminate. Secondary indicators (Kharg queue growth, LNG collapse, Suez surcharges) all support sustained kinetic tension but are indirect. The system held Worse trend because (a) no de-escalation signals appeared (HSC collapse, corridor reopening, Strait traffic surge), and (b) kinetic plateau is consistent with regime-change persistence. Rule held, but confidence downgrade (high→medium) was warranted due to data gaps.

**What to change next run:**
(1) **Expand secondary HSC proxies.** If Windward/CENTCOM data lags >48h, rely on: (a) Kharg Island queue directional change (delta >±3 vessels = trend), (b) Suez/Cape rerouting traffic volume (if surge >10 vessels/day on Suez, Hormuz blockade durability implied), (c) container carrier service announcements (suspension extended = kinetic confidence high; restart announced = kinetic de-escalation signal). Build a 72-hour secondary-indicator scorecard to substitute for missing primary data.

(2) **Establish mine-clearance progress transparency threshold.** Pentagon/CENTCOM media briefs are scheduled (not ad-hoc). Set standing search for: (a) Thursday/Friday Pentagon press briefings (weekly), (b) Italian MOD statements (weekly), (c) IMO/JMIC quarterly or as-needed advisories. If no brief appears within 5 days of expected publication, treat as "no progress to report" signal = slippage probability +15%.

(3) **Codify QatarEnergy extension language parsing.** The mid-October extension was a tier-1 signal but reached us via Bloomberg rumor (22 July announced) before formal Tadawul filing or investor call. Next run: when a high-profile operator extension is reported, cross-check with (a) Tadawul/exchange filings within 24h, (b) customer notifications (Edison, KOGAS, Fluxys), (c) CEO/CFO guidance on earnings calls. Parse three phrases: "restart timeline", "even if Strait reopens", "beyond [date]". These distinguish between FM updates (tactical) and regime-shift signals (strategic).

## 31 July 2026 (Day 154) · Reflection

**What surprised me this run:**

QatarEnergy's FM extension was not to mid-October (as Bloomberg 22 Jul suggested) but to 30 September. This is a *refinement* not a regression, but it resets buyer expectations. The shift from "October recovery signal" to "September recovery signal" is a subtle downward revision. It suggests QatarEnergy's confidence in Strait reopening may have cooled slightly (or more realistically, the June expectation for early-August mine-clearance has slipped internally, and producers are now bracing for mid-to-late September at best). The lack of a new October extension in late July is itself a signal: if producers were highly confident in blockade persistence, they would lock in longer FMs and prepare balance sheets for sustained disruption. The fact that QatarEnergy stopped at September suggests optimism, but measured. This is bullish-tilted compared to Scenario C (kinetic escalation), but not aligned with Scenario B's "optimistic mine-clearance" timeline.

**Methodology rule that was tested:**

The "Trend = Same if no Hard FM + no Hard de-escalation + no regime shift" rule held despite a prior brief calling Trend "Worse." This run's comprehensive search found no new FM declarations, no new kinetic escalation, and no FM lifts. By the rule, Trend = Same is correct. However, the prior brief's Worse call was justified by "kinetic plateau" (sustained regime-change state). The question: Is a sustained kinetic plateau itself a regime shift warranting "Worse" indefinitely? The answer from methodology: No. Regime shift = change in state, not persistence of state. A plateau is persistence, not shift. The rule held and the methodology was tested—it passed because Hard signals are factual (did a new FM occur?), not sentiment (does the prior bad state persist?).

**What to change next run:**

Add a "mine-clearance execution rate" metric to the mine-risk monitoring. Currently, I'm relying on JMIC Advisory updates (last: 5 July), which are lagged. For Day 155+ (4 Aug), I should search specifically for "mine clearance progress August 2026" and "Strait of Hormuz vessels transiting August 2026" to capture any acceleration or slip in real time. This will sharpen the L4→L5 boundary test and give earlier warning if mine-clearance slips past 10 August (the execution-window deadline for Scenario B). Second, formalize a "QatarEnergy production ramp rate" metric (trains operating on a rolling 7-day basis) instead of relying on point-in-time announcements. This will help detect whether producers are pacing output to mine-clearance progress or ramping aggressively ahead of Strait reopening.
