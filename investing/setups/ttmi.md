---
ticker: TTMI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $133.20 ahead of the 2026-08-05 print"
entry_price: 133.20
stop_price: 119.68
stop_logic: "chandelier trail: HH22 $154.81 - 3x ATR $11.71 = $119.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 153.48
target_logic: "T1 $153.48 = entry $133.20 + 1.5x R (R=$13.52); T2 $173.75 = entry + 3x R; structure ceiling = 52w high $223.87"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $327.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.71)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
