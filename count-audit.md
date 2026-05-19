# Forensic audit — the 160 → 114 → 124 count discrepancy

**Date:** Day 81 · 19 May 2026.
**Status:** Honest accounting of what went wrong, why, and what's now in place to prevent recurrence.
**Author posture:** Confessional. The previous architecture allowed the count to drift away from underlying truth. Users planning around these numbers deserve the explanation.

---

## What the numbers were

| Moment | Dashboard total | Source of the number |
|---|---|---|
| Day 55 seed (original CSV) | 114 | Felsberger Day-55 dataset, hand-curated |
| Day 71 (first dashboard) | 147 | Initial WAVE_DATA seed I hand-built |
| Day 78 (before today) | 160 | Model-written WAVE_DATA, monotonic-merged each run |
| Day 81 (after events.csv) | 114 → 124 | Derived from `events.csv` rows |

**Net swing:** −36 events between Day 78 and Day 81 after architectural change.

---

## Why 160 was wrong

The dashboard total was computed from the last row of `WAVE_DATA`:
```js
total = waveData[waveData.length - 1][1] + waveData[waveData.length - 1][2] + waveData[waveData.length - 1][3]
```

`WAVE_DATA` was a JS array of `[day, w1_cum, w2_cum, w3_cum]` rows. **The model wrote these numbers on every run.** I added a monotonic merge function (`merge_wave_data`) that took `max()` per day across model output and existing data — but that only prevented *decreases*. It did not validate against any underlying event list.

So the chain was:
1. Model estimates "how many cumulative events should there be today"
2. Model writes WAVE_DATA row `[81, 100, 20, 40]` reflecting that estimate
3. Script's monotonic merge accepts the number (or floors it at whatever was higher previously)
4. Dashboard displays the sum (160)

**The number was the model's opinion, not a count of named events.** There was never a row-by-row audit trail.

Over time, the model inflated. On some runs it added 2–3 to the cumulative without naming 2–3 new events. The monotonic merge locked those inflations in.

## Why 114 was technically correct but practically wrong

When I introduced `events.csv` today as the canonical ledger, the script started computing the dashboard total from the file. The file had exactly 114 rows — the Day-55 seed.

So the dashboard dropped to 114. That number is **provably correct** (114 rows in events.csv, each with an operator, a chain, a date) — but it's **incomplete** because real events between Day 55 (23 April) and Day 81 (19 May) were not in the file.

The bot had been tracking some of these post-Day-55 events in `RECENT_EVENTS_DATA` (the dashboard's events feed), but the architecture didn't append them to a canonical count ledger. Two parallel lists: one feed, one count, no synchronization.

## Why 124 is an honest interim and what's still missing

I backfilled 10 post-Day-55 events that the bot had been tracking with named operator + date + source:

```
Day 58 · Saudi Aramco May OSP
Day 64 · KAFCO Bangladesh restart
Day 65 · Lotte Chemical Yeosu restart delay
Day 66 · US Project Freedom launch
Day 68 · US Navy Project Freedom pause
Day 69 · EGA Al Taweelah rehab start
Day 73 · Trump ceasefire statement
Day 74 · QatarEnergy mid-June FM extension
Day 74 · Maritime bunker fuel signal
Day 75 · Saudi Aramco June OSP
```

That gets the total to 124. The remaining 36-event gap from 160 is the inflation that has no audit trail. Some of it may be legitimate events the bot tracked but I haven't located; some of it is model estimation that doesn't map to a discrete event. **Without ground truth I can't recover the missing 36.**

## The structural defect (root cause)

Two architectural failures compounded:

**Defect 1: count derived from model assertion, not from a ledger.** The model wrote the cumulative number. There was no event-level table to verify it against. Any monotonic-merge protection only prevented decreases; it couldn't detect inflations.

**Defect 2: two parallel data sources (`RECENT_EVENTS_DATA` and `WAVE_DATA`) with no synchronization.** When the bot surfaced a new event in `RECENT_EVENTS_DATA`, nothing automatically updated `WAVE_DATA` or vice versa. They drifted.

## What's now in place (architectural fix)

**A single source of truth — `events.csv`.** Every event is a row with:
- Date (ISO YYYY-MM-DD)
- Operator name
- Country
- Commodity chain
- Wave (1 / 2 / 3)
- FM type (1–6)
- Volume in kt (optional)
- EU-direct flag
- Source attribution
- Notes / summary

**The script enforces the rules:**
1. Loads events.csv at the start of every run
2. Validates each row (required fields: entity, chain, date, wave, fm_type, source)
3. Parses model's `NEW_EVENTS` block — rejects rows that fail validation
4. Dedupes new events against existing by SHA-1 hash of `operator|chain|date`
5. Appends only validated, deduped new rows to events.csv
6. **Recomputes** WAVE_DATA, CHAIN_DATA, TYPE_DATA, and the dashboard total **from the file** — the model cannot write these numbers anymore
7. Every count change is appended to `count-log.md` with the run timestamp, prior count, new count, and the list of events that drove the delta

**The dashboard total now equals the row count of events.csv, every run, no exceptions.** If a user clicks the "Data (CSV)" link in the masthead, they get the file. Row count minus header = dashboard total. End of arithmetic.

## What this means for users planning around the numbers

- **Going forward**, the count can only grow when a named event with date, operator, chain, and source is added to events.csv. The count can never grow without leaving an audit trail.
- **Going forward**, the count can only stay flat or grow. The script never deletes rows. If a row is added in error, it gets a `corrected_at` annotation rather than being removed.
- **Today's count (124)** is the honest baseline. Some real post-Day-55 events may still be missing from events.csv (we haven't tracked every operator press release in the 26 days between Day 55 and Day 81). Going forward, the bot's NEW_EVENTS block plus your manual additions will close the gap.
- **The historical 160** was inflated by ~36 events without provenance. That number is retired. There's no integrity-preserving way to reconcile to it.

## What you should do as a user

- Treat **124** as Day-81 baseline.
- If you remember specific FM events between 23 April and 19 May that aren't in events.csv, name them and I'll append them (with proper source attribution).
- Future deltas come with provenance. Open `count-log.md` to see every count change with the events that drove it.

## What I've changed in the repo to prevent recurrence

- `events.csv` is the only number-of-events authority. Dashboard total, by-wave counts, by-chain counts, by-FM-type counts all derive from it.
- `count-log.md` is a new append-only ledger. Every run logs prior count, new count, delta, and the events added.
- Row validation in the script — rows missing required fields are rejected with a logged reason.
- Model output for `WAVE_DATA`, `CHAIN_DATA`, `TYPE_DATA` is discarded. The model can only propose new events via `NEW_EVENTS`; the script does the counting.
- Masthead has a "Data (CSV)" link so anyone can download the ledger and verify the count themselves.

## What this audit costs in trust — and how to rebuild it

The 160 → 124 swing is uncomfortable. Numbers users planned around shifted by 22%. The honest framing:

- The 124 is verifiable; the 160 was not.
- A tracker that can be inflated by model opinion is not a tracker — it's an estimator.
- The cost of fixing this in plain sight is short-term: users see a smaller number. The cost of not fixing it is permanent: every future count would be untrustworthy.

I chose the short-term cost. The architecture from here forward is auditable to the row.
