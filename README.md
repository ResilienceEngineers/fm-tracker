# Force Majeure Tracker

Daily-updated supply-chain force-majeure dashboard, modelled on the Resilience Engineers Hormuz Daily Brief blueprint. Built and operated by Marco Felsberger, Resilience Engineers.

**Live site:** https://resilienceengineers.github.io/fm-tracker/
**Deep brief:** https://resilienceengineers.github.io/fm-tracker/brief.html
**Contact:** marco.felsberger@resilience-engineers.com

---

## What this is

A live tracker for force-majeure declarations across global supply chains, with the analytical frame fixed to the Three Waves model (Wave 1 production / Wave 2 allocation / Wave 3 physical absence).

The site updates daily at 06:00 UTC (08:00 CEST) via GitHub Actions. The updater calls the Anthropic API, runs the procedure in `daily-update-prompt.md` against the current methodology and knowledge base, and rewrites the BRIEF:* blocks in `index.html` and `brief.html`.

The methodology is private. The public site shows a one-paragraph meta-description. The full operating ruleset, source-tier list, and calibration log stay in this repo for the team and the daily updater.

## File map

| File | Purpose |
|---|---|
| `index.html` | One-pager dashboard (the URL shared with stakeholders) |
| `brief.html` | Deep brief with full categories, watchlist, scenarios |
| `methodology.md` | Internal rules — signal tiers, trend rule, Wave Intensity scale, anti-bias defaults |
| `sources.md` | Six-tier source list with daily-updater search targets |
| `knowledge-base.md` | Analytical anchors — crisis context, Wave model signature, asset status |
| `backtest-log.md` | Calibration loop — predictions scored T+1/T+3/T+7, Brier weekly |
| `daily-update-prompt.md` | Canonical procedure for the daily run |
| `daily-briefs/_template.md` | Archive template; the updater writes one per day |
| `.github/workflows/daily-brief.yml` | Triple-cron + skip-guard automation |
| `.github/scripts/update_brief.py` | Python script calling the Claude API |
| `.github/scripts/requirements.txt` | Python deps |

## Operating model

**Daily run.** GitHub Actions fires at 06:00 / 07:30 / 10:00 UTC. The skip-guard checks the last commit message — if today's date is already there, the later runs no-op. The script reads context, runs Claude API with `claude-sonnet-4-6` model and web-search tool, parses delimited output blocks, replaces BRIEF:* markers in both HTML files, archives yesterday's brief, appends today's predictions to the backtest log, and pushes.

**Schedule** — three cron slots because GitHub Actions schedules are best-effort and the first slot drops more often than the docs admit.

**Calibration loop.** Yesterday's predictions are scored at the start of each run before today's brief is drafted. Methodology deltas are logged in both `methodology.md` and `backtest-log.md`. The public site never shows calibration data — that's for the team only.

**Cost target.** Sonnet 4.6 with caching, ~24k output tokens, 12 web searches max. Roughly $0.10–0.20 per daily run.

## Model used

`claude-sonnet-4-6` for the daily run. Opus is overkill for this task and 5× more expensive; same quality on this specific procedure.

## Author / branch hygiene

The bot owns:
- `index.html` and `brief.html` (BRIEF:* block content)
- `daily-briefs/*.md`
- `backtest-log.md` daily entries

Humans own:
- `methodology.md`, `sources.md`, `knowledge-base.md`, `daily-update-prompt.md`, `README.md`
- `.github/workflows/*`, `.github/scripts/*`
- HTML structure outside BRIEF:* markers

Always `git pull --rebase` before pushing local changes.

## Setup

The repo ships ready to run. To start:

1. Add `ANTHROPIC_API_KEY` to repo secrets at  Settings → Secrets and variables → Actions.
2. Trigger the first run: `gh workflow run daily-brief.yml`.
3. Watch: `gh run watch <id> --exit-status`.

Generated at console.anthropic.com/settings/keys.

## Methodology in one paragraph (public)

The brief uses a tiered signal-weighting framework. Only verified physical events from primary sources can move the Wave Intensity assessment. Trend movement requires confirmed change versus the prior 72 hours. The system continuously calibrates against outcomes — when predictions miss, the underlying heuristics are sharpened. The full operating ruleset is kept private to preserve analytical edge.

---

## Pitfalls (lessons saved)

1. JSON output fails on large HTML — use delimiters.
2. `re.error: invalid group reference` when replacing strings starting with digits — use lambda for `re.sub`.
3. `max_tokens` triggers SDK 10-min timeout in non-streaming mode — use `client.messages.stream()`.
4. First scheduled cron drops silently — triple cron with skip-guard.
5. `html2canvas` / `jsPDF` choke on Leaflet tiles (CORS) — print CSS only for PDF.
6. Race conditions between local edits and bot commits — `git pull --rebase` before every push.
