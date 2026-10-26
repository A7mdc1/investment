---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $97.78 ahead of the 2026-11-24 print"
entry_price: 97.78
stop_price: 91.90
stop_logic: "chandelier trail: HH22 $100.58 - 3x ATR $2.89 = $91.90 — exit when decline exceeds ~3 average daily ranges"
target_price: 106.59
target_logic: "T1 $106.59 = entry $97.78 + 1.5x R (R=$5.87); T2 $115.40 = entry + 3x R; structure ceiling = 52w high $100.59"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $252.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.89)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
