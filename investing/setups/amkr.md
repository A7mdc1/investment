---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $51.56 ahead of the 2026-10-26 print"
entry_price: 51.56
stop_price: 45.39
stop_logic: "chandelier trail: HH22 $52.78 - 3x ATR $2.46 = $45.39 — exit when decline exceeds ~3 average daily ranges"
target_price: 60.82
target_logic: "T1 $60.82 = entry $51.56 + 1.5x R (R=$6.17); T2 $70.07 = entry + 3x R; structure ceiling = 52w high $96.55"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $208.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.46)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
