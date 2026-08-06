---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $86.59 ahead of the 2026-08-26 print"
entry_price: 86.59
stop_price: 73.98
stop_logic: "chandelier trail: HH22 $87.41 - 3x ATR $4.47 = $73.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 105.50
target_logic: "T1 $105.50 = entry $86.59 + 1.5x R (R=$12.61); T2 $124.41 = entry + 3x R; structure ceiling = 52w high $100.57"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $169.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.47)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
