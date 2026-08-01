---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $151.94 ahead of the 2026-09-03 print"
entry_price: 151.94
stop_price: 144.92
stop_logic: "chandelier trail: HH22 $170.00 - 3x ATR $8.36 = $144.92 — exit when decline exceeds ~3 average daily ranges"
target_price: 162.47
target_logic: "T1 $162.47 = entry $151.94 + 1.5x R (R=$7.02); T2 $172.99 = entry + 3x R; structure ceiling = 52w high $272.78"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $186.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.36)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
