---
ticker: DG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $125.75 ahead of the 2026-08-27 print"
entry_price: 125.75
stop_price: 117.91
stop_logic: "chandelier trail: HH22 $130.61 - 3x ATR $4.23 = $117.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 137.51
target_logic: "T1 $137.51 = entry $125.75 + 1.5x R (R=$7.84); T2 $149.27 = entry + 3x R; structure ceiling = 52w high $156.60"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $343.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.23)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: debt/mcap 57% > 33%
---

## Notes
Scaffolded 2026-07-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
