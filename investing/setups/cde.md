---
ticker: CDE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $16.99 ahead of the 2026-08-05 print"
entry_price: 16.99
stop_price: 16.07
stop_logic: "chandelier trail: HH22 $19.47 - 3x ATR $1.13 = $16.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 18.38
target_logic: "T1 $18.38 = entry $16.99 + 1.5x R (R=$0.92); T2 $19.76 = entry + 3x R; structure ceiling = 52w high $27.76"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $825.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.13)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
