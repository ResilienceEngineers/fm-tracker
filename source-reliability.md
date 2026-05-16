# Source reliability — Force Majeure Tracker

**Status:** Internal. Maintained automatically by the daily updater. Sources that consistently surface primary documents before peers earn promotion; sources whose citations don't downstream-confirm get downgraded.

This file is the empirical companion to `sources.md`. `sources.md` is the curated tier list of *which sources we target*; this file is the running scorecard of *which targeted sources actually deliver*.

---

## Scoring rules

For each source cited in a brief:

- **Citation:** Source appears in a published brief block (CATEGORY_*, FM_TABLE, RECENT_EVENTS_DATA).
- **Confirmation:** Within 14 days, an independent Tier-1 source publishes the same fact.
- **Lead:** Source's publication timestamp precedes the next-earliest independent confirmation by ≥ 6 hours.
- **Falsification:** Within 14 days, a Tier-1 source contradicts the cited fact.
- **Hit rate** = (Citations that earned Confirmation) / (Citations old enough to evaluate).
- **Lead rate** = (Citations with Lead) / (Citations with Confirmation).

## Promotion / demotion rules

- **Demote one tier** if: 4-week rolling Hit rate < 0.6 AND ≥ 5 citations evaluated.
- **Promote one tier** if: 4-week rolling Hit rate > 0.85 AND Lead rate > 0.3 AND ≥ 8 citations evaluated.
- **Mark "watch"** if: 4-week rolling Falsification rate > 0.05.

Decisions are proposed by the updater, listed below under "Pending tier changes", and applied after one calendar week's review.

---

## Current scoreboard

_(updated by the daily updater after each run)_

| Source | Current tier | 4w citations | 4w hit rate | 4w lead rate | 4w false rate | Status |
|---|---|---|---|---|---|---|
| _seed table — populated as runs accumulate_ | | | | | | |

---

## Pending tier changes

_(proposed by the updater; reviewed weekly)_

_None yet._

---

## Applied tier changes

_(historical log of promotions / demotions; each entry has a date and a reason)_

_None yet._

---

## Audit notes

- 2026-05-16 — Source reliability framework introduced (Day 78 audit). Initial scoreboard empty; the next 4 weekly runs populate the table. First promotion / demotion candidates expected on or after Day 106 (~13 June 2026).
