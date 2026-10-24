---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $58.23 ahead of the 2026-11-04 print"
entry_price: 58.23
stop_price: 54.94
stop_logic: "chandelier trail: HH22 $59.45 - 3x ATR $1.50 = $54.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.16
target_logic: "T1 $63.16 = entry $58.23 + 1.5x R (R=$3.29); T2 $68.09 = entry + 3x R; structure ceiling = 52w high $64.63"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $63.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
