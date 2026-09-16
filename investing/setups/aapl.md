---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $332.54 ahead of the 2026-10-29 print"
entry_price: 332.54
stop_price: 314.65
stop_logic: "chandelier trail: HH22 $336.22 - 3x ATR $7.19 = $314.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 359.37
target_logic: "T1 $359.37 = entry $332.54 + 1.5x R (R=$17.89); T2 $386.20 = entry + 3x R; structure ceiling = 52w high $344.24"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13072.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.19)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
