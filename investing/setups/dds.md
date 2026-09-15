---
ticker: DDS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $648.64 ahead of the 2026-11-12 print"
entry_price: 648.64
stop_price: 593.25
stop_logic: "chandelier trail: HH22 $665.25 - 3x ATR $24.00 = $593.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 731.73
target_logic: "T1 $731.73 = entry $648.64 + 1.5x R (R=$55.39); T2 $814.81 = entry + 3x R; structure ceiling = 52w high $710.45"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $100.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($24.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
