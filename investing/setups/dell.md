---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $371.87 ahead of the 2026-09-03 print"
entry_price: 371.87
stop_price: 362.34
stop_logic: "chandelier trail: HH22 $462.72 - 3x ATR $33.46 = $362.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 386.17
target_logic: "T1 $386.17 = entry $371.87 + 1.5x R (R=$9.53); T2 $400.47 = entry + 3x R; structure ceiling = 52w high $468.94"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2777.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($33.46)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
