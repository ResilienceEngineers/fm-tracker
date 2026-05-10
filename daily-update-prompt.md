# Daily update procedure

**Read this before drafting today's brief.** The Python updater script encodes the same procedure inline in its system prompt — this file is the human-readable canonical version.

---

## Step 0 — Score yesterday's predictions FIRST

Before any new web search. Open `backtest-log.md`, find yesterday's entry, mark each Action / Watchlist / Scenario as Hit / Miss / False alarm / Surprise / pending. If a deadline passed without the outcome, it's a Miss — don't soften it. Append the calibration note to today's entry header.

If yesterday's brief was wrong on Wave Intensity direction, log the methodology delta with the reason. Don't carry the bias forward.

## Step 1 — Read the context files

In order:
1. `methodology.md` — the current rules.
2. `sources.md` — the search target list.
3. `knowledge-base.md` — analytical anchors.
4. `backtest-log.md` — last 7 entries.
5. The most recent `daily-briefs/YYYY-MM-DD.md`.
6. Current `index.html` and `brief.html` for last-published state.

## Step 2 — Web search the Tier 1–3 set

In this order, single-pass:
1. Tier 1 first-party operator releases for active FMs in `knowledge-base.md` section 4.
2. Argus / ICIS / Platts / OPIS / Chemical Week — last 24h on naphtha / LNG / urea / aluminium / methanol / helium / jet fuel.
3. Lloyd's List + Baird Maritime + Ship & Bunker — last 24h on Hormuz / Gulf shipping / port FMs.
4. Tadawul + Bursa Saudi + BSE FM-related disclosures.
5. Reuters wire + Bloomberg primary — sovereign and regulator statements.
6. Polymerupdate weekly + Plasteurope — European petchem cascade.

Do not pull from Tier 6 (anonymous OSINT, op-eds, AI summaries) unless the same claim is independently corroborated by Tier 1–3.

## Step 3 — Classify every signal

For each input found in Step 2:
- Tier (Hard / Medium / Soft / Noise)
- FM type (Production / Shipping / Downstream / Distribution / Restart / Cascade)
- Wave (1 / 2 / 3 — see methodology section 4)
- Commodity chain
- Operator + site
- Source name (specific outlet)

Put the noise pile aside. Score the rest by the methodology section 1 weights.

## Step 4 — Set Trend and Wave Intensity

Apply methodology sections 2 and 3. The trend rule is binary on Hard signals only. Wave Intensity moves only on the operative test passing — write down which test passed and on which signals.

## Step 5 — Draft the six categories

Each category: title + badge (Worse / Same / Better) + arrow + confidence + 3 signal bullets + "Why this matters" para + "Implication" para + sources line.

Categories:
1. New FM declarations (last 72h pulse)
2. Kinetic / facility damage
3. Cascade through downstream chains (Wave 2 propagation)
4. Restart / forward-coverage signals (Wave 3 markers)
5. Substitution / alternative sourcing
6. Outlook scenarios (T+30, 3 scenarios summing to 100%)

## Step 6 — Status board (one-pager)

Six tiles, each one-line status + 2-bullet body. These are the at-a-glance summary; the full reasoning lives in the deep brief.

## Step 7 — Map pins

Edit the JS array between `// BRIEF:MAP_PINS_START` and `// BRIEF:MAP_PINS_END`. Each pin: `{ name, lat, lon, status, note }`. Status is `red | amber | green` mapped to active / partial / restarted.

## Step 8 — Operational outputs

- 3 actions (operational verbs only — "lock in", "diversify", "request", "audit", "stage")
- 5 watchlist items (each with deadline + directional implication)
- 3 scenarios (probabilities sum to 100%, each with observable)
- Recent FM declarations table (last 14d)
- Cascade timeline T+0 / T+7 / T+30 / T+90

## Step 9 — Write the blocks

Output format is delimiter blocks, never JSON. The Python script parses them. Required keys are listed in the system prompt.

## Step 10 — Stop conditions

- Tier 1–3 input insufficient → set INTERIM=true, write thin brief, flag on masthead. Don't pad.
- Source-tier conflict (Tier 1 contradicts Tier 2) → publish the Tier-1 reading and name both sources.
- Wave Intensity move without Hard signal → don't publish the move; explain the Soft signals in the watchlist instead.

## Step 11 — Tone rules (output)

- Practitioner not narrator. The reader is a supply chain executive at 8 AM, not a journalism prize jury.
- Lead with fact, then why, then so-what.
- No AI tells. No "delve". No "elegant". No "comprehensive landscape". No copula avoidance ("serves as", "represents") — say "is".
- Numbers when available, ranges when not, "unknown" when unknown.
- Don't generalise from one source to "many experts". Name the source.
- No hindsight reframing. The brief is a forecast, not a justification.

## Step 12 — Output checklist

Same as methodology section 9. Tick each one before emitting the delimiter blocks.
