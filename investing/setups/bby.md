---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $86.42 ahead of the 2026-08-27 print"
entry_price: 86.42
stop_price: 83.13
stop_logic: "chandelier trail: HH22 $91.27 - 3x ATR $2.71 = $83.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 91.36
target_logic: "T1 $91.36 = entry $86.42 + 1.5x R (R=$3.29); T2 $96.30 = entry + 3x R; structure ceiling = 52w high $91.26"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $267.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.71)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
