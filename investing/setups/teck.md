---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $67.09 ahead of the 2026-10-29 print"
entry_price: 67.09
stop_price: 62.54
stop_logic: "chandelier trail: HH22 $69.38 - 3x ATR $2.28 = $62.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 73.91
target_logic: "T1 $73.91 = entry $67.09 + 1.5x R (R=$4.55); T2 $80.73 = entry + 3x R; structure ceiling = 52w high $72.45"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $176.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.28)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
