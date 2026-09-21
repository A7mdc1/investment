---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $39.72 ahead of the 2026-11-12 print"
entry_price: 39.72
stop_price: 33.33
stop_logic: "chandelier trail: HH22 $40.64 - 3x ATR $2.44 = $33.33 — exit when decline exceeds ~3 average daily ranges"
target_price: 49.31
target_logic: "T1 $49.31 = entry $39.72 + 1.5x R (R=$6.39); T2 $58.90 = entry + 3x R; structure ceiling = 52w high $74.94"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $55.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.44)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
