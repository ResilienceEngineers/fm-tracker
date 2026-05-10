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
