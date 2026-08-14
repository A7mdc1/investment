---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $225.25 ahead of the 2026-08-26 print"
entry_price: 225.25
stop_price: 205.86
stop_logic: "chandelier trail: HH22 $227.49 - 3x ATR $7.21 = $205.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 254.35
target_logic: "T1 $254.35 = entry $225.25 + 1.5x R (R=$19.40); T2 $283.44 = entry + 3x R; structure ceiling = 52w high $236.36"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $24813.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.21)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
