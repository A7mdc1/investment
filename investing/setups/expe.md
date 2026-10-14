---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $270.50 ahead of the 2026-11-04 print"
entry_price: 270.50
stop_price: 263.25
stop_logic: "chandelier trail: HH22 $294.84 - 3x ATR $10.53 = $263.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 281.37
target_logic: "T1 $281.37 = entry $270.50 + 1.5x R (R=$7.25); T2 $292.24 = entry + 3x R; structure ceiling = 52w high $341.54"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $574.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($10.53)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
