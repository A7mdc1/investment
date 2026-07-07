---
ticker: ALAB
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $432.74 ahead of the 2026-08-04 print"
entry_price: 432.74
stop_price: 371.67
stop_logic: "chandelier trail: HH22 $499.48 - 3x ATR $42.60 = $371.67 — exit when decline exceeds ~3 average daily ranges"
target_price: 524.34
target_logic: "T1 $524.34 = entry $432.74 + 1.5x R (R=$61.07); T2 $615.94 = entry + 3x R; structure ceiling = 52w high $499.70"
holding_window_days: 21
catalyst: "2026-08-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2622.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($42.60)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
