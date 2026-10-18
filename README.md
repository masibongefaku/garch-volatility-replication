# GARCH(1,1) Volatility Replication — Bitcoin

Python replication of the volatility modelling from my BComHons Economics research project
(University of Johannesburg, 2025), originally estimated in EViews.

## Key results (daily BTC-USD, Feb 2015 – Jan 2025, n = 3,652)
- α = 0.125, β = 0.840 → persistence α + β = 0.965
- Shock half-life ≈ 19 days; long-run volatility ≈ 79% annualised
- Largest volatility spike: March 2020 (COVID crash)

![Conditional volatility](figures/btc_garch_volatility.png)

## Extension: Student-t errors
| | Normal | Student-t |
|---|---|---|
| α + β | 0.965 | 1.000 |
| Half-life (days) | 19.4 | ∞ |
| ν (tail df) | – | 3.17 |
| AIC | 19,101.6 | 18,148.6 |

Fat-tailed errors fit decisively better (ΔAIC = −953) and push persistence to ≈ 1 (IGARCH-like), so the Normal model's 19-day half-life is not robust.

![Normal vs Student-t](figures/btc_garch_normal_vs_t.png)

## Run it
```bash
pip install -r requirements.txt
jupyter lab notebooks/01_btc_garch.ipynb
```

## Next steps
- EGARCH / GJR-GARCH for asymmetric (leverage) effects
- Rolling out-of-sample volatility forecasts and VaR backtest