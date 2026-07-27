---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $88.56 ahead of the 2026-08-27 print"
entry_price: 88.56
stop_price: 81.51
stop_logic: "chandelier trail: HH22 $88.75 - 3x ATR $2.41 = $81.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 99.14
target_logic: "T1 $99.14 = entry $88.56 + 1.5x R (R=$7.05); T2 $109.72 = entry + 3x R; structure ceiling = 52w high $88.74"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $277.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.41)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
