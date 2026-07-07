---
ticker: LIF
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.73 ahead of the 2026-08-10 print"
entry_price: 56.73
stop_price: 49.97
stop_logic: "chandelier trail: HH22 $59.45 - 3x ATR $3.16 = $49.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 66.87
target_logic: "T1 $66.87 = entry $56.73 + 1.5x R (R=$6.76); T2 $77.00 = entry + 3x R; structure ceiling = 52w high $112.56"
holding_window_days: 21
catalyst: "2026-08-10 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $39.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.16)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
