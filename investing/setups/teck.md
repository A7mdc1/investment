---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $65.79 ahead of the 2026-10-22 print"
entry_price: 65.79
stop_price: 65.72
stop_logic: "chandelier trail: HH22 $72.56 - 3x ATR $2.28 = $65.72 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.90
target_logic: "T1 $65.90 = entry $65.79 + 1.5x R (R=$0.07); T2 $66.01 = entry + 3x R; structure ceiling = 52w high $72.54"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $204.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.28)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
