---
ticker: SMCI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $28.93 ahead of the 2026-08-11 print"
entry_price: 28.93
stop_price: 27.59
stop_logic: "chandelier trail: HH22 $33.68 - 3x ATR $2.03 = $27.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 30.95
target_logic: "T1 $30.95 = entry $28.93 + 1.5x R (R=$1.34); T2 $32.96 = entry + 3x R; structure ceiling = 52w high $62.36"
holding_window_days: 21
catalyst: "2026-08-11 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1338.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.03)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
