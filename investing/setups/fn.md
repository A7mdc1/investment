---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $570.22 ahead of the 2026-08-17 print"
entry_price: 570.22
stop_price: 475.61
stop_logic: "chandelier trail: HH22 $590.76 - 3x ATR $38.38 = $475.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 712.14
target_logic: "T1 $712.14 = entry $570.22 + 1.5x R (R=$94.62); T2 $854.07 = entry + 3x R; structure ceiling = 52w high $749.30"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $381.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($38.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
