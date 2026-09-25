---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $53.79 ahead of the 2026-10-26 print"
entry_price: 53.79
stop_price: 47.40
stop_logic: "chandelier trail: HH22 $54.89 - 3x ATR $2.50 = $47.40 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.37
target_logic: "T1 $63.37 = entry $53.79 + 1.5x R (R=$6.39); T2 $72.95 = entry + 3x R; structure ceiling = 52w high $96.57"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $194.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
