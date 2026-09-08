---
ticker: SOLV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $90.19 ahead of the 2026-11-05 print"
entry_price: 90.19
stop_price: 87.28
stop_logic: "chandelier trail: HH22 $94.16 - 3x ATR $2.29 = $87.28 — exit when decline exceeds ~3 average daily ranges"
target_price: 94.56
target_logic: "T1 $94.56 = entry $90.19 + 1.5x R (R=$2.91); T2 $98.93 = entry + 3x R; structure ceiling = 52w high $94.14"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $83.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.29)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
