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
