# DECISIONS

Why the repo is the way it is. Add with
`python scripts/track.py decide "title" --why "reason" --alt "rejected option" --revisit "condition"`.

Never delete a decision. If it changes, add a new one that supersedes it.

## D-001 - 2026-10-19 - Use in-repo markdown files as project memory
- **Why:** Lives next to the code, versioned with git, readable by any AI tool and by recruiters.
- **Alternatives rejected:** Notion-only tracking (drifts from the code); GitHub Projects only (not visible to AI assistants).
- **Revisit if:** Repo gets collaborators who need a shared board.

## D-002 - 2026-10-19 - Treat Student-t as the preferred error distribution
- **Why:** AIC 18,148.6 vs 19,101.6 for Normal (delta -953); nu = 3.17 shows fat tails. Normal-model 19-day half-life is not robust.
- **Alternatives rejected:** Normal errors (original EViews spec) kept only as the replication baseline.
- **Revisit if:** Skewed-t or GED fits materially better.

## D-003 - 2026-10-19 - CI installs only pytest and ruff (requirements-dev.txt)
- **Why:** requirements.txt is a UTF-16 full pip freeze with Windows-only pywinpty; it would fail on Linux CI.
- **Alternatives rejected:** Installing requirements.txt in CI.
- **Revisit if:** requirements.txt is slimmed to cross-platform direct deps; then CI can install it and test src/.

## D-004 - 2026-10-21 - Snapshot data before writing known-value tests
- **Why:** yfinance re-downloads each run and Yahoo revises history; tests need fixed input or they fail even when code is correct
- **Alternatives rejected:** Write src/ tests first against live downloads
- **Revisit if:** never - fixed test data is standard practice
