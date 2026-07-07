---
ticker: DUOL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $129.72 ahead of the 2026-08-05 print"
entry_price: 129.72
stop_price: 111.80
stop_logic: "chandelier trail: HH22 $137.97 - 3x ATR $8.72 = $111.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 156.60
target_logic: "T1 $156.60 = entry $129.72 + 1.5x R (R=$17.92); T2 $183.47 = entry + 3x R; structure ceiling = 52w high $468.30"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $194.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.72)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
