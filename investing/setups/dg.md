---
ticker: DG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $123.28 ahead of the 2026-08-27 print"
entry_price: 123.28
stop_price: 119.21
stop_logic: "chandelier trail: HH22 $131.25 - 3x ATR $4.01 = $119.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 129.38
target_logic: "T1 $129.38 = entry $123.28 + 1.5x R (R=$4.07); T2 $135.49 = entry + 3x R; structure ceiling = 52w high $156.65"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $239.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.01)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: debt/mcap 58% > 33%
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
