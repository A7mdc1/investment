---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $316.46 ahead of the 2026-10-29 print"
entry_price: 316.46
stop_price: 310.88
stop_logic: "chandelier trail: HH22 $330.81 - 3x ATR $6.64 = $310.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 324.83
target_logic: "T1 $324.83 = entry $316.46 + 1.5x R (R=$5.58); T2 $333.20 = entry + 3x R; structure ceiling = 52w high $344.36"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $11979.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.64)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
