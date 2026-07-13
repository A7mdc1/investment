---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $422.69 ahead of the 2026-09-03 print"
entry_price: 422.69
stop_price: 371.41
stop_logic: "chandelier trail: HH22 $460.50 - 3x ATR $29.70 = $371.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 499.61
target_logic: "T1 $499.61 = entry $422.69 + 1.5x R (R=$51.28); T2 $576.53 = entry + 3x R; structure ceiling = 52w high $469.66"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3213.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.70)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
