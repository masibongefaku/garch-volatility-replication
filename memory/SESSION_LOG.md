# SESSION LOG

One line per thing done. Include numbers where there are any.
Add entries with `python scripts/track.py log "..."`.

<!-- entries below, newest first -->

### 2026-10-21
- DONE: Fill data/README.md: confirm BTC-USD source and download date
- requirements.txt: 116 frozen pkgs (UTF-16) -> 6 direct deps (UTF-8); clean-venv install + imports verified
- DONE: Slim requirements.txt to direct deps only (it is a UTF-16 full pip freeze incl. Windows-only pywinpty)
- CI green on main (commit 43618a7): ruff clean, 3/3 tests pass on GitHub Actions

### 2026-10-19
- DONE: Merge chore/repo-kit into main and confirm CI is green
- Installed repo control kit (CLAUDE.md rules, memory/, track.py, CI, templates) on branch chore/repo-kit

### Before 2026-10-19 (from README)
- GARCH(1,1) Normal on daily BTC-USD, Feb 2015 - Jan 2025, n = 3,652: alpha = 0.125, beta = 0.840, persistence 0.965, half-life ~19.4 days, long-run vol ~79% annualised
- Student-t extension: persistence 1.000, nu = 3.17, AIC 18,148.6 vs 19,101.6 Normal (delta AIC = -953)
- Figures: btc_garch_volatility.png, btc_garch_normal_vs_t.png
