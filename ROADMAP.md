# ROADMAP

Tick boxes as milestones complete. `python scripts/track.py status` reports progress.

## M0 - Foundation
- [x] Repo control kit merged to main
- [x] CI green on main
- [ ] requirements.txt slimmed to cross-platform direct deps
- [ ] data/README.md lists source, date range, download date

## M1 - Baseline replication
- [x] GARCH(1,1) Normal fitted on BTC-USD, results in README
- [x] Student-t extension with AIC comparison
- [x] Volatility figures in README
- [ ] Fitting code moved from notebook to src/ with known-value tests

## M2 - Asymmetric models
- [ ] SPEC section for EGARCH / GJR-GARCH
- [ ] EGARCH and GJR-GARCH fitted, leverage term reported with p-value
- [ ] Model comparison table (AIC/BIC, persistence) in README

## M3 - Forecast and risk
- [ ] Rolling out-of-sample 1-day volatility forecasts (date split, no look-ahead)
- [ ] VaR from forecasts, backtested with Kupiec (and Christoffersen) tests
- [ ] Results and limitations in README

## M4 - Portfolio-ready
- [ ] Reproduce-from-clean-clone check passed
- [ ] One-line headline result at top of README
- [ ] Repo stays pinned on GitHub profile
