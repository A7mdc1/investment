---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $37.75 ahead of the 2026-11-12 print"
entry_price: 37.75
stop_price: 34.20
stop_logic: "chandelier trail: HH22 $41.47 - 3x ATR $2.42 = $34.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 43.07
target_logic: "T1 $43.07 = entry $37.75 + 1.5x R (R=$3.55); T2 $48.39 = entry + 3x R; structure ceiling = 52w high $70.56"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $55.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.42)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
