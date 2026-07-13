---
ticker: CNQ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $42.86 ahead of the 2026-08-06 print"
entry_price: 42.86
stop_price: 42.82
stop_logic: "chandelier trail: HH22 $46.18 - 3x ATR $1.12 = $42.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 42.92
target_logic: "T1 $42.92 = entry $42.86 + 1.5x R (R=$0.04); T2 $42.99 = entry + 3x R; structure ceiling = 52w high $50.42"
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $427.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.12)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
