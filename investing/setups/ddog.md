---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $233.38 ahead of the 2026-11-05 print"
entry_price: 233.38
stop_price: 220.31
stop_logic: "chandelier trail: HH22 $254.33 - 3x ATR $11.34 = $220.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 252.99
target_logic: "T1 $252.99 = entry $233.38 + 1.5x R (R=$13.07); T2 $272.60 = entry + 3x R; structure ceiling = 52w high $292.82"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $802.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.34)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
