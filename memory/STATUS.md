# STATUS

_Last updated: 2026-10-21_

## Current focus
M1: lock the data (CSV snapshot), then move fitting code into src/ with tests.

## Next actions
- [ ] Save BTC-USD CSV snapshot to data/sample/ and load from it by default (Yahoo revises history) - branch feat/data-snapshot; check alpha = 0.125, beta = 0.840 still reproduce
- [ ] Move GARCH fitting code from notebook into src/ with a known-value test (R4, R7)
- [ ] Write docs/SPEC.md section for EGARCH / GJR-GARCH extension

## Blockers
- none

## Parked
- Rolling out-of-sample volatility forecasts and VaR backtest (after asymmetric models)
