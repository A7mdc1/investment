---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.85 ahead of the 2026-10-23 print"
entry_price: 18.85
stop_price: 18.17
stop_logic: "chandelier trail: HH22 $21.66 - 3x ATR $1.16 = $18.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 19.87
target_logic: "T1 $19.87 = entry $18.85 + 1.5x R (R=$0.68); T2 $20.90 = entry + 3x R; structure ceiling = 52w high $30.45"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $200.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.16)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
