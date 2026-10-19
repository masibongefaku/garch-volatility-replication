# STATUS

_Last updated: 2026-10-19_

## Current focus
Install repo control kit, then make the repo reproducible on any machine.

## Next actions
- [ ] Merge chore/repo-kit into main and confirm CI is green
- [ ] Slim requirements.txt to direct deps only (it is a UTF-16 full pip freeze incl. Windows-only pywinpty)
- [ ] Fill data/README.md: confirm BTC-USD source and download date
- [ ] Move GARCH fitting code from notebook into src/ with a known-value test (R4, R7)
- [ ] Write docs/SPEC.md section for EGARCH / GJR-GARCH extension

## Blockers
- none

## Parked
- Rolling out-of-sample volatility forecasts and VaR backtest (after asymmetric models)
