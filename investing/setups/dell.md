---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $497.71 ahead of the 2026-09-03 print"
entry_price: 497.71
stop_price: 405.81
stop_logic: "chandelier trail: HH22 $514.00 - 3x ATR $36.06 = $405.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 635.56
target_logic: "T1 $635.56 = entry $497.71 + 1.5x R (R=$91.90); T2 $773.41 = entry + 3x R; structure ceiling = 52w high $514.16"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2548.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($36.06)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
