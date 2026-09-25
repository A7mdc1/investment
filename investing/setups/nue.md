---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $247.76 ahead of the 2026-10-26 print"
entry_price: 247.76
stop_price: 246.11
stop_logic: "chandelier trail: HH22 $268.47 - 3x ATR $7.45 = $246.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 250.23
target_logic: "T1 $250.23 = entry $247.76 + 1.5x R (R=$1.65); T2 $252.70 = entry + 3x R; structure ceiling = 52w high $279.95"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $300.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.45)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
