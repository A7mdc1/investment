---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $153.42 ahead of the 2026-09-03 print"
entry_price: 153.42
stop_price: 144.93
stop_logic: "chandelier trail: HH22 $170.00 - 3x ATR $8.36 = $144.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 166.16
target_logic: "T1 $166.16 = entry $153.42 + 1.5x R (R=$8.49); T2 $178.89 = entry + 3x R; structure ceiling = 52w high $272.50"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $180.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.36)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
