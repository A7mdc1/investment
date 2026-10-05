---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $333.62 ahead of the 2026-10-29 print"
entry_price: 333.62
stop_price: 324.36
stop_logic: "chandelier trail: HH22 $345.34 - 3x ATR $6.99 = $324.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 347.50
target_logic: "T1 $347.50 = entry $333.62 + 1.5x R (R=$9.26); T2 $361.39 = entry + 3x R; structure ceiling = 52w high $345.36"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13551.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.99)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
