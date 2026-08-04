---
ticker: ARW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $228.10 ahead of the 2026-08-06 print"
entry_price: 228.10
stop_price: 204.66
stop_logic: "chandelier trail: HH22 $228.10 - 3x ATR $7.81 = $204.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 263.26
target_logic: "T1 $263.26 = entry $228.10 + 1.5x R (R=$23.44); T2 $298.42 = entry + 3x R; structure ceiling = 52w high $237.36"
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $105.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.81)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
