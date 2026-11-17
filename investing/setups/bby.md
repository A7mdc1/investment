---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $99.93 ahead of the 2026-11-24 print"
entry_price: 99.93
stop_price: 95.21
stop_logic: "chandelier trail: HH22 $106.83 - 3x ATR $3.87 = $95.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 107.01
target_logic: "T1 $107.01 = entry $99.93 + 1.5x R (R=$4.72); T2 $114.10 = entry + 3x R; structure ceiling = 52w high $106.88"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $265.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.87)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
