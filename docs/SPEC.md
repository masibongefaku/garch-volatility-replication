# SPEC

Rule R2: nothing gets built that isn't specified here first. Keep it short.

## 1. Baseline (done)
- **Goal:** Replicate the honours-project GARCH(1,1) on daily BTC-USD log returns in Python
  and match the EViews estimates.
- **Data:** BTC-USD daily, Feb 2015 - Jan 2025, n = 3,652 (see data/README.md).
- **Outputs:** alpha, beta, persistence, half-life, long-run annualised vol, AIC;
  Normal vs Student-t comparison; conditional volatility chart.
- **Validation:** Python estimates vs EViews output (state tolerance once checked).

## 2. Next: Asymmetric models (EGARCH, GJR-GARCH)
- **Goal:** Test for a leverage effect in BTC volatility.
- **Inputs:** same returns series as baseline.
- **Outputs:** asymmetry term with standard error and p-value; AIC/BIC vs GARCH(1,1)-t.
- **Method:** <!-- library, distribution, mean equation -->
- **Tests:** <!-- known-value test, e.g. fit on a simulated series with known params -->
- **Out of scope:** forecasting (that's section 3).

## 3. Later: Out-of-sample forecasts and VaR backtest
- **Goal:** <!-- e.g. 1-day 99% VaR from rolling GARCH forecasts, Kupiec p > 0.05 -->
- **Split dates:** <!-- train end / test start; no look-ahead (R5) -->
- **Tests:** <!-- breach count, Kupiec and Christoffersen tests -->
