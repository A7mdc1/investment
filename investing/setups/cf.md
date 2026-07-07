---
ticker: CF
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $113.20 ahead of the 2026-08-05 print"
entry_price: 113.20
stop_price: 106.79
stop_logic: "chandelier trail: HH22 $118.60 - 3x ATR $3.94 = $106.79 — exit when decline exceeds ~3 average daily ranges"
target_price: 122.81
target_logic: "T1 $122.81 = entry $113.20 + 1.5x R (R=$6.41); T2 $132.42 = entry + 3x R; structure ceiling = 52w high $141.32"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $314.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.94)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
