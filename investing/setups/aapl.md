---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $334.47 ahead of the 2026-10-29 print"
entry_price: 334.47
stop_price: 314.76
stop_logic: "chandelier trail: HH22 $336.22 - 3x ATR $7.15 = $314.76 — exit when decline exceeds ~3 average daily ranges"
target_price: 364.03
target_logic: "T1 $364.03 = entry $334.47 + 1.5x R (R=$19.71); T2 $393.59 = entry + 3x R; structure ceiling = 52w high $344.10"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13157.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.15)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
