---
ticker: RCL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $297.27 ahead of the 2026-07-28 print"
entry_price: 297.27
stop_price: 292.34
stop_logic: "chandelier trail: HH22 $333.39 - 3x ATR $13.68 = $292.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 304.67
target_logic: "T1 $304.67 = entry $297.27 + 1.5x R (R=$4.93); T2 $312.07 = entry + 3x R; structure ceiling = 52w high $360.33"
holding_window_days: 21
catalyst: "2026-07-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $775.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.68)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
