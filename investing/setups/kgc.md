---
ticker: KGC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $23.71 ahead of the 2026-07-29 print"
entry_price: 23.71
stop_price: 22.66
stop_logic: "chandelier trail: HH22 $25.65 - 3x ATR $1.00 = $22.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 25.29
target_logic: "T1 $25.29 = entry $23.71 + 1.5x R (R=$1.05); T2 $26.87 = entry + 3x R; structure ceiling = 52w high $39.00"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $179.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
