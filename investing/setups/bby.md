---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $85.94 ahead of the 2026-08-27 print"
entry_price: 85.94
stop_price: 79.68
stop_logic: "chandelier trail: HH22 $87.33 - 3x ATR $2.55 = $79.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 95.33
target_logic: "T1 $95.33 = entry $85.94 + 1.5x R (R=$6.26); T2 $104.73 = entry + 3x R; structure ceiling = 52w high $87.34"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $308.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.55)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
