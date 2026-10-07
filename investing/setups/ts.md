---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $55.66 ahead of the 2026-11-04 print"
entry_price: 55.66
stop_price: 54.55
stop_logic: "chandelier trail: HH22 $58.74 - 3x ATR $1.40 = $54.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 57.33
target_logic: "T1 $57.33 = entry $55.66 + 1.5x R (R=$1.11); T2 $59.00 = entry + 3x R; structure ceiling = 52w high $64.57"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $65.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.40)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
