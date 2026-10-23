---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $55.42 ahead of the 2026-10-27 print"
entry_price: 55.42
stop_price: 53.69
stop_logic: "chandelier trail: HH22 $58.44 - 3x ATR $1.58 = $53.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 58.01
target_logic: "T1 $58.01 = entry $55.42 + 1.5x R (R=$1.73); T2 $60.61 = entry + 3x R; structure ceiling = 52w high $69.89"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $318.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.58)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
