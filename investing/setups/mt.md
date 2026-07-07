---
ticker: MT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $65.35 ahead of the 2026-07-30 print"
entry_price: 65.35
stop_price: 65.31
stop_logic: "chandelier trail: HH22 $72.50 - 3x ATR $2.40 = $65.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.42
target_logic: "T1 $65.42 = entry $65.35 + 1.5x R (R=$0.04); T2 $65.48 = entry + 3x R; structure ceiling = 52w high $72.53"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $112.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.40)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
