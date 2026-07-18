---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $206.86 ahead of the 2026-08-05 print"
entry_price: 206.86
stop_price: 190.66
stop_logic: "chandelier trail: HH22 $207.14 - 3x ATR $5.49 = $190.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 231.16
target_logic: "T1 $231.16 = entry $206.86 + 1.5x R (R=$16.20); T2 $255.47 = entry + 3x R; structure ceiling = 52w high $207.07"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $538.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.49)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
