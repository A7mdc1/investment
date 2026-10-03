---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $333.69 ahead of the 2026-10-29 print"
entry_price: 333.69
stop_price: 324.31
stop_logic: "chandelier trail: HH22 $345.34 - 3x ATR $7.01 = $324.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 347.76
target_logic: "T1 $347.76 = entry $333.69 + 1.5x R (R=$9.38); T2 $361.83 = entry + 3x R; structure ceiling = 52w high $345.43"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13988.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.01)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
