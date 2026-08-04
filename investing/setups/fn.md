---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $534.43 ahead of the 2026-08-17 print"
entry_price: 534.43
stop_price: 437.41
stop_logic: "chandelier trail: HH22 $540.56 - 3x ATR $34.38 = $437.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 679.95
target_logic: "T1 $679.95 = entry $534.43 + 1.5x R (R=$97.02); T2 $825.48 = entry + 3x R; structure ceiling = 52w high $748.50"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $371.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($34.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
