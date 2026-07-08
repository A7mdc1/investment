---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $200.79 ahead of the 2026-08-26 print"
entry_price: 200.79
stop_price: 194.16
stop_logic: "chandelier trail: HH22 $214.87 - 3x ATR $6.90 = $194.16 — exit when decline exceeds ~3 average daily ranges"
target_price: 210.73
target_logic: "T1 $210.73 = entry $200.79 + 1.5x R (R=$6.63); T2 $220.67 = entry + 3x R; structure ceiling = 52w high $236.50"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $29460.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.90)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
