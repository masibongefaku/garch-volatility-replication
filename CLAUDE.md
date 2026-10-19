# CLAUDE.md — Rules for this repo

GARCH(1,1) volatility replication on Bitcoin, from my BComHons research (UJ, 2025).
Any AI assistant (Claude, Copilot, ChatGPT) working in this repo follows these rules.
Humans too. If another tool expects `AGENTS.md`, copy this file to that name.

---

## 1. Start of every session (non-negotiable)

1. Read `memory/STATUS.md` — current focus, next actions, blockers.
2. Read the latest 2 entries in `memory/SESSION_LOG.md`.
3. If touching logic, read the relevant section of `docs/SPEC.md`.
4. State in one line what this session will do. Pick it from **Next actions** unless told otherwise.

Fast version: `python scripts/track.py status`

## 2. End of every session (non-negotiable)

1. `python scripts/track.py log "what got done, with numbers"`
2. `python scripts/track.py done <n>` for finished actions, `next "..."` for new ones.
3. Any choice between approaches → `python scripts/track.py decide "..." --why "..."`
4. Commit the `memory/` changes with the code: `chore(memory): update status`.

A session that changed code but not `memory/` is not finished.

---

## 3. House rules

**R1 — No code I can't explain.** Every non-trivial function gets a plain-English
explanation before it is committed. If the assistant writes it, the assistant explains
it line by line on request, and I write the docstring in my own words.

**R2 — Spec first.** No new feature without a section in `docs/SPEC.md` stating
inputs, outputs, method, and how it will be tested.

**R3 — Numbers first.** Results are reported as numbers with units and dates
(e.g. "persistence 0.965, daily BTC-USD Feb 2015 - Jan 2025, n = 3,652").
No "looks good", "performs well".

**R4 — Every calculation has a test.** Each function in `src/` that computes a number
has at least one test in `tests/` against a known value (hand-calculated, textbook,
EViews output, or reference library output).

**R5 — No look-ahead.** Any forecast or backtest uses only data available at time t.
Splits are by date, never shuffled. Note the split dates in the log.

**R6 — Reproducible.** Fixed random seeds. Data source, series, and download date
recorded in `data/README.md`. Dependency versions pinned.

**R7 — Logic lives in `src/`.** Notebooks are for exploration and charts only.
Anything reused twice moves to `src/`.

**R8 — Never commit:** raw data dumps, `.env`, API keys, passwords, personal files,
anything from work (Life Healthcare data never touches this repo).

**R9 — Small commits.** One logical change per commit. Format:
`type(scope): summary` — types: `feat`, `fix`, `test`, `docs`, `refactor`, `chore`, `data`.

**R10 — `main` always runs.** Work on `feat/<name>` branches, merge only when
tests pass and CI is green.

---

## 4. Definition of done

- [ ] Code runs from a clean clone
- [ ] Tests pass (`pytest`) and lint is clean (`ruff check .`)
- [ ] I can explain every line (R1)
- [ ] Result recorded with numbers in `SESSION_LOG.md` (R3)
- [ ] `STATUS.md` updated
- [ ] README updated if the result or how-to-run changed

---

## 5. How the assistant should behave here

- Be direct. Numbers first. No motivational filler.
- If a request breaks a house rule, say which rule and propose the compliant version.
- Prefer the smallest change that works. Don't refactor unasked.
- When unsure about a finance/stats assumption, state it explicitly and log it as a
  decision rather than guessing silently.
- Don't invent data, results, or citations. If a number isn't computed, say so.
- Don't commit or push without my OK.

## 6. Map of this repo

| Path | What it is |
|---|---|
| `memory/STATUS.md` | Where things stand right now. Read first. |
| `memory/SESSION_LOG.md` | Dated log of what was done, newest first |
| `memory/DECISIONS.md` | Why things are the way they are |
| `memory/LEARNINGS.md` | Concepts learned, in my own words |
| `ROADMAP.md` | Milestones M0-M4 with checkboxes |
| `docs/SPEC.md` | What the code must do |
| `scripts/track.py` | CLI that updates the memory files |
| `src/` | Reusable code (fitting, metrics) |
| `tests/` | Tests for `src/` and `scripts/` |
| `notebooks/` | Exploration and charts only |
| `figures/` | Charts used in README |
| `data/README.md` | Data provenance |
| `requirements.txt` | Runtime deps; `requirements-dev.txt` = pytest, ruff (CI) |
