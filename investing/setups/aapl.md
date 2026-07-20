---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $324.56 ahead of the 2026-07-30 print"
entry_price: 324.56
stop_price: 309.19
stop_logic: "chandelier trail: HH22 $334.99 - 3x ATR $8.60 = $309.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 347.62
target_logic: "T1 $347.62 = entry $324.56 + 1.5x R (R=$15.37); T2 $370.68 = entry + 3x R; structure ceiling = 52w high $334.94"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $19409.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.60)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
