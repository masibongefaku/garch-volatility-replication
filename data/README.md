# Data

No data files are committed. The notebook downloads prices live on every run (rule R6).

| Item | Value |
|---|---|
| Source | Yahoo Finance via `yfinance` 1.7.0 |
| Call | `yf.Ticker("BTC-USD").history(start="2015-02-01", end="2025-02-01")["Close"]` |
| Series | BTC-USD daily close, timezone stripped (`tz_localize(None)`) |
| Date range | 2015-02-01 to 2025-01-31 (`end` is exclusive) |
| Frequency | Daily, 7 days a week (crypto trades every day) |
| Returns | `100 * ln(P_t / P_t-1)`, first NaN dropped -> n = 3,652 |
| Loaded in | `notebooks/01_btc_garch.ipynb`, cell 2 |
| Results last produced | 2026-10-18 (last notebook commit) |

## Known limitation
Yahoo can revise historical prices, and the data is re-downloaded each run, so a future
run may not reproduce the README numbers exactly. Fix (planned): save a CSV snapshot to
`data/sample/` and load from it by default.

Original honours research estimates were done in EViews.
