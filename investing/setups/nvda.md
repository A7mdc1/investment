---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $217.70 ahead of the 2026-08-26 print"
entry_price: 217.70
stop_price: 201.86
stop_logic: "chandelier trail: HH22 $224.76 - 3x ATR $7.63 = $201.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 241.46
target_logic: "T1 $241.46 = entry $217.70 + 1.5x R (R=$15.84); T2 $265.23 = entry + 3x R; structure ceiling = 52w high $236.37"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $25545.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.63)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
