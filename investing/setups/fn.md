---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $542.51 ahead of the 2026-08-17 print"
entry_price: 542.51
stop_price: 441.77
stop_logic: "chandelier trail: HH22 $547.57 - 3x ATR $35.27 = $441.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 693.62
target_logic: "T1 $693.62 = entry $542.51 + 1.5x R (R=$100.74); T2 $844.73 = entry + 3x R; structure ceiling = 52w high $749.32"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $367.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($35.27)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
