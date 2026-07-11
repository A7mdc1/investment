---
ticker: GDDY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $88.92 ahead of the 2026-07-30 print"
entry_price: 88.92
stop_price: 79.43
stop_logic: "chandelier trail: HH22 $91.20 - 3x ATR $3.92 = $79.43 — exit when decline exceeds ~3 average daily ranges"
target_price: 103.16
target_logic: "T1 $103.16 = entry $88.92 + 1.5x R (R=$9.49); T2 $117.39 = entry + 3x R; structure ceiling = 52w high $171.33"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $213.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.92)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
