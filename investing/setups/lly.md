---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1283.41 ahead of the 2026-10-29 print"
entry_price: 1283.41
stop_price: 1211.15
stop_logic: "chandelier trail: HH22 $1321.21 - 3x ATR $36.69 = $1211.15 — exit when decline exceeds ~3 average daily ranges"
target_price: 1391.81
target_logic: "T1 $1391.81 = entry $1283.41 + 1.5x R (R=$72.26); T2 $1500.21 = entry + 3x R; structure ceiling = 52w high $1321.75"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2776.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($36.69)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
