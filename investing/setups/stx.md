---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $922.50 ahead of the 2026-07-28 print"
entry_price: 922.50
stop_price: 861.36
stop_logic: "chandelier trail: HH22 $1111.00 - 3x ATR $83.21 = $861.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 1014.21
target_logic: "T1 $1014.21 = entry $922.50 + 1.5x R (R=$61.14); T2 $1105.92 = entry + 3x R; structure ceiling = 52w high $1144.54"
holding_window_days: 21
catalyst: "2026-07-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $4369.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($83.21)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
