---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $69.06 ahead of the 2026-12-03 print"
entry_price: 69.06
stop_price: 62.68
stop_logic: "chandelier trail: HH22 $73.56 - 3x ATR $3.63 = $62.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 78.62
target_logic: "T1 $78.62 = entry $69.06 + 1.5x R (R=$6.38); T2 $88.18 = entry + 3x R; structure ceiling = 52w high $73.54"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1273.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.63)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
