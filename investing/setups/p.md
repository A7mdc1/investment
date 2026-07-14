---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $77.63 ahead of the 2026-08-26 print"
entry_price: 77.63
stop_price: 70.14
stop_logic: "chandelier trail: HH22 $82.57 - 3x ATR $4.14 = $70.14 — exit when decline exceeds ~3 average daily ranges"
target_price: 88.87
target_logic: "T1 $88.87 = entry $77.63 + 1.5x R (R=$7.49); T2 $100.11 = entry + 3x R; structure ceiling = 52w high $100.56"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $219.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.14)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
