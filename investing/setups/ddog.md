---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $274.29 ahead of the 2026-11-05 print"
entry_price: 274.29
stop_price: 246.03
stop_logic: "chandelier trail: HH22 $280.70 - 3x ATR $11.56 = $246.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 316.68
target_logic: "T1 $316.68 = entry $274.29 + 1.5x R (R=$28.26); T2 $359.07 = entry + 3x R; structure ceiling = 52w high $292.73"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $811.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.56)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
