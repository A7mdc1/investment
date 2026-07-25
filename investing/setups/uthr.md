---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $528.47 ahead of the 2026-08-05 print"
entry_price: 528.47
stop_price: 523.16
stop_logic: "chandelier trail: HH22 $563.70 - 3x ATR $13.51 = $523.16 — exit when decline exceeds ~3 average daily ranges"
target_price: 536.43
target_logic: "T1 $536.43 = entry $528.47 + 1.5x R (R=$5.31); T2 $544.39 = entry + 3x R; structure ceiling = 52w high $609.54"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $227.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.51)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
