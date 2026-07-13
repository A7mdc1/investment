---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $82.50 ahead of the 2026-08-27 print"
entry_price: 82.50
stop_price: 76.59
stop_logic: "chandelier trail: HH22 $83.82 - 3x ATR $2.41 = $76.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 91.37
target_logic: "T1 $91.37 = entry $82.50 + 1.5x R (R=$5.91); T2 $100.24 = entry + 3x R; structure ceiling = 52w high $83.84"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $292.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.41)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
