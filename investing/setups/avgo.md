---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $381.85 ahead of the 2026-09-03 print"
entry_price: 381.85
stop_price: 361.82
stop_logic: "chandelier trail: HH22 $407.52 - 3x ATR $15.23 = $361.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 411.89
target_logic: "T1 $411.89 = entry $381.85 + 1.5x R (R=$20.03); T2 $441.93 = entry + 3x R; structure ceiling = 52w high $493.98"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $7925.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.23)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
