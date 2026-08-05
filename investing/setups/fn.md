---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $529.47 ahead of the 2026-08-17 print"
entry_price: 529.47
stop_price: 440.52
stop_logic: "chandelier trail: HH22 $545.52 - 3x ATR $35.00 = $440.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 662.90
target_logic: "T1 $662.90 = entry $529.47 + 1.5x R (R=$88.95); T2 $796.33 = entry + 3x R; structure ceiling = 52w high $748.90"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $370.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($35.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
