---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $225.76 ahead of the 2026-11-05 print"
entry_price: 225.76
stop_price: 222.27
stop_logic: "chandelier trail: HH22 $258.25 - 3x ATR $11.99 = $222.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 231.00
target_logic: "T1 $231.00 = entry $225.76 + 1.5x R (R=$3.49); T2 $236.24 = entry + 3x R; structure ceiling = 52w high $292.82"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $870.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.99)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
