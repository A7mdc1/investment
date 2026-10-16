---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $366.12 ahead of the 2026-10-22 print"
entry_price: 366.12
stop_price: 361.98
stop_logic: "chandelier trail: HH22 $378.29 - 3x ATR $5.44 = $361.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 372.31
target_logic: "T1 $372.31 = entry $366.12 + 1.5x R (R=$4.13); T2 $378.51 = entry + 3x R; structure ceiling = 52w high $420.34"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $91.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.44)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
