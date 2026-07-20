---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $84.98 ahead of the 2026-08-27 print"
entry_price: 84.98
stop_price: 79.75
stop_logic: "chandelier trail: HH22 $87.35 - 3x ATR $2.53 = $79.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 92.84
target_logic: "T1 $92.84 = entry $84.98 + 1.5x R (R=$5.24); T2 $100.70 = entry + 3x R; structure ceiling = 52w high $87.34"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $299.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.53)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
