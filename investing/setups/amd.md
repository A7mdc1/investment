---
ticker: AMD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $552.05 ahead of the 2026-08-04 print"
entry_price: 552.05
stop_price: 467.12
stop_logic: "chandelier trail: HH22 $584.73 - 3x ATR $39.20 = $467.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 679.45
target_logic: "T1 $679.45 = entry $552.05 + 1.5x R (R=$84.93); T2 $806.85 = entry + 3x R; structure ceiling = 52w high $584.80"
holding_window_days: 21
catalyst: "2026-08-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $16642.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($39.20)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
