---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $57.97 ahead of the 2026-11-04 print"
entry_price: 57.97
stop_price: 54.95
stop_logic: "chandelier trail: HH22 $59.45 - 3x ATR $1.50 = $54.95 — exit when decline exceeds ~3 average daily ranges"
target_price: 62.50
target_logic: "T1 $62.50 = entry $57.97 + 1.5x R (R=$3.02); T2 $67.03 = entry + 3x R; structure ceiling = 52w high $64.63"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $62.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
