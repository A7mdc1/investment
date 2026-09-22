---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $246.54 ahead of the 2026-11-05 print"
entry_price: 246.54
stop_price: 218.05
stop_logic: "chandelier trail: HH22 $251.99 - 3x ATR $11.31 = $218.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 289.28
target_logic: "T1 $289.28 = entry $246.54 + 1.5x R (R=$28.49); T2 $332.02 = entry + 3x R; structure ceiling = 52w high $292.80"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $814.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.31)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
