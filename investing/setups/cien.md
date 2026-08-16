---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $428.77 ahead of the 2026-09-03 print"
entry_price: 428.77
stop_price: 372.10
stop_logic: "chandelier trail: HH22 $462.69 - 3x ATR $30.20 = $372.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 513.77
target_logic: "T1 $513.77 = entry $428.77 + 1.5x R (R=$56.67); T2 $598.77 = entry + 3x R; structure ceiling = 52w high $637.10"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $846.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($30.20)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
