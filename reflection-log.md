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
