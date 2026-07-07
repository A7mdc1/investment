---
ticker: VRNS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $45.67 ahead of the 2026-07-28 print"
entry_price: 45.67
stop_price: 39.71
stop_logic: "chandelier trail: HH22 $46.42 - 3x ATR $2.24 = $39.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 54.61
target_logic: "T1 $54.61 = entry $45.67 + 1.5x R (R=$5.96); T2 $63.56 = entry + 3x R; structure ceiling = 52w high $63.87"
holding_window_days: 21
catalyst: "2026-07-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $90.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.24)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
