---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $59.25 ahead of the 2026-11-04 print"
entry_price: 59.25
stop_price: 55.46
stop_logic: "chandelier trail: HH22 $59.45 - 3x ATR $1.33 = $55.46 — exit when decline exceeds ~3 average daily ranges"
target_price: 64.94
target_logic: "T1 $64.94 = entry $59.25 + 1.5x R (R=$3.79); T2 $70.63 = entry + 3x R; structure ceiling = 52w high $64.61"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $63.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.33)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
