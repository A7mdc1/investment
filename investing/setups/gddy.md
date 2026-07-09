---
ticker: GDDY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $87.58 ahead of the 2026-07-30 print"
entry_price: 87.58
stop_price: 79.13
stop_logic: "chandelier trail: HH22 $91.20 - 3x ATR $4.02 = $79.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 100.26
target_logic: "T1 $100.26 = entry $87.58 + 1.5x R (R=$8.45); T2 $112.94 = entry + 3x R; structure ceiling = 52w high $178.01"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $212.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.02)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: debt/mcap 33% > 33%
---

## Notes
Scaffolded 2026-07-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
