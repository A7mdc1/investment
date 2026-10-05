---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $34.49 ahead of the 2026-11-12 print"
entry_price: 34.49
stop_price: 33.73
stop_logic: "chandelier trail: HH22 $41.47 - 3x ATR $2.58 = $33.73 — exit when decline exceeds ~3 average daily ranges"
target_price: 35.63
target_logic: "T1 $35.63 = entry $34.49 + 1.5x R (R=$0.76); T2 $36.76 = entry + 3x R; structure ceiling = 52w high $70.53"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $50.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.58)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
