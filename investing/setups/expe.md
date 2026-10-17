---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $288.95 ahead of the 2026-11-04 print"
entry_price: 288.95
stop_price: 264.67
stop_logic: "chandelier trail: HH22 $298.63 - 3x ATR $11.32 = $264.67 — exit when decline exceeds ~3 average daily ranges"
target_price: 325.37
target_logic: "T1 $325.37 = entry $288.95 + 1.5x R (R=$24.28); T2 $361.79 = entry + 3x R; structure ceiling = 52w high $341.55"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $584.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
