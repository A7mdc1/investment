---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $444.47 ahead of the 2026-09-01 print"
entry_price: 444.47
stop_price: 411.00
stop_logic: "chandelier trail: HH22 $514.00 - 3x ATR $34.33 = $411.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 494.68
target_logic: "T1 $494.68 = entry $444.47 + 1.5x R (R=$33.47); T2 $544.89 = entry + 3x R; structure ceiling = 52w high $513.84"
holding_window_days: 21
catalyst: "2026-09-01 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2555.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($34.33)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
