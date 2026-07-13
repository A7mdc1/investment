---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $316.35 ahead of the 2026-07-30 print"
entry_price: 316.35
stop_price: 298.70
stop_logic: "chandelier trail: HH22 $323.45 - 3x ATR $8.25 = $298.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 342.83
target_logic: "T1 $342.83 = entry $316.35 + 1.5x R (R=$17.65); T2 $369.30 = entry + 3x R; structure ceiling = 52w high $323.47"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $18749.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.25)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
