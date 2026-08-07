---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $565.73 ahead of the 2026-08-17 print"
entry_price: 565.73
stop_price: 471.40
stop_logic: "chandelier trail: HH22 $579.47 - 3x ATR $36.02 = $471.40 — exit when decline exceeds ~3 average daily ranges"
target_price: 707.22
target_logic: "T1 $707.22 = entry $565.73 + 1.5x R (R=$94.33); T2 $848.71 = entry + 3x R; structure ceiling = 52w high $749.31"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $374.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($36.02)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
