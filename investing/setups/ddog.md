---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $271.44 ahead of the 2026-11-05 print"
entry_price: 271.44
stop_price: 243.98
stop_logic: "chandelier trail: HH22 $280.70 - 3x ATR $12.24 = $243.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 312.62
target_logic: "T1 $312.62 = entry $271.44 + 1.5x R (R=$27.46); T2 $353.80 = entry + 3x R; structure ceiling = 52w high $292.81"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $819.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($12.24)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
