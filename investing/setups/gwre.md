---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $140.73 ahead of the 2026-09-03 print"
entry_price: 140.73
stop_price: 122.79
stop_logic: "chandelier trail: HH22 $143.45 - 3x ATR $6.89 = $122.79 — exit when decline exceeds ~3 average daily ranges"
target_price: 167.64
target_logic: "T1 $167.64 = entry $140.73 + 1.5x R (R=$17.94); T2 $194.55 = entry + 3x R; structure ceiling = 52w high $272.73"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $213.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.89)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
