---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $50.75 ahead of the 2026-10-26 print"
entry_price: 50.75
stop_price: 49.14
stop_logic: "chandelier trail: HH22 $56.56 - 3x ATR $2.47 = $49.14 — exit when decline exceeds ~3 average daily ranges"
target_price: 53.16
target_logic: "T1 $53.16 = entry $50.75 + 1.5x R (R=$1.61); T2 $55.57 = entry + 3x R; structure ceiling = 52w high $96.48"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $184.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.47)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
