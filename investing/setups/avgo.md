---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $370.83 ahead of the 2026-09-03 print"
entry_price: 370.83
stop_price: 365.06
stop_logic: "chandelier trail: HH22 $414.64 - 3x ATR $16.53 = $365.06 — exit when decline exceeds ~3 average daily ranges"
target_price: 379.48
target_logic: "T1 $379.48 = entry $370.83 + 1.5x R (R=$5.77); T2 $388.13 = entry + 3x R; structure ceiling = 52w high $494.44"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $10000.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($16.53)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
