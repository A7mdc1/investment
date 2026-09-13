---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $35.12 ahead of the 2026-11-12 print"
entry_price: 35.12
stop_price: 30.78
stop_logic: "chandelier trail: HH22 $37.10 - 3x ATR $2.11 = $30.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 41.62
target_logic: "T1 $41.62 = entry $35.12 + 1.5x R (R=$4.34); T2 $48.13 = entry + 3x R; structure ceiling = 52w high $75.04"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $51.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.11)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
