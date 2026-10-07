---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $274.87 ahead of the 2026-11-05 print"
entry_price: 274.87
stop_price: 252.91
stop_logic: "chandelier trail: HH22 $285.68 - 3x ATR $10.92 = $252.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 307.82
target_logic: "T1 $307.82 = entry $274.87 + 1.5x R (R=$21.96); T2 $340.76 = entry + 3x R; structure ceiling = 52w high $292.73"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $734.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($10.92)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
