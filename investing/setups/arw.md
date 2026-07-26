---
ticker: ARW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $212.27 ahead of the 2026-08-06 print"
entry_price: 212.27
stop_price: 209.47
stop_logic: "chandelier trail: HH22 $232.93 - 3x ATR $7.82 = $209.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 216.46
target_logic: "T1 $216.46 = entry $212.27 + 1.5x R (R=$2.80); T2 $220.66 = entry + 3x R; structure ceiling = 52w high $237.44"
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $120.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.82)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
