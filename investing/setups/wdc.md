---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $524.56 ahead of the 2026-08-05 print"
entry_price: 524.56
stop_price: 450.66
stop_logic: "chandelier trail: HH22 $609.47 - 3x ATR $52.94 = $450.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 635.41
target_logic: "T1 $635.41 = entry $524.56 + 1.5x R (R=$73.90); T2 $746.26 = entry + 3x R; structure ceiling = 52w high $799.63"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $3720.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($52.94)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
