---
ticker: SMCI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $30.22 ahead of the 2026-08-11 print"
entry_price: 30.22
stop_price: 26.28
stop_logic: "chandelier trail: HH22 $32.59 - 3x ATR $2.10 = $26.28 — exit when decline exceeds ~3 average daily ranges"
target_price: 36.13
target_logic: "T1 $36.13 = entry $30.22 + 1.5x R (R=$3.94); T2 $42.03 = entry + 3x R; structure ceiling = 52w high $58.79"
holding_window_days: 21
catalyst: "2026-08-11 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1232.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.10)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
