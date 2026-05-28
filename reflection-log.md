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
