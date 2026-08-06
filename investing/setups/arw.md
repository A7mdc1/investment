---
ticker: ARW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $224.18 ahead of the 2026-08-06 print"
entry_price: 224.18
stop_price: 206.63
stop_logic: "chandelier trail: HH22 $230.45 - 3x ATR $7.94 = $206.63 — exit when decline exceeds ~3 average daily ranges"
target_price: 250.51
target_logic: "T1 $250.51 = entry $224.18 + 1.5x R (R=$17.55); T2 $276.84 = entry + 3x R; structure ceiling = 52w high $237.23"
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $105.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.94)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
