---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $65.52 ahead of the 2026-10-22 print"
entry_price: 65.52
stop_price: 65.45
stop_logic: "chandelier trail: HH22 $72.46 - 3x ATR $2.34 = $65.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.63
target_logic: "T1 $65.63 = entry $65.52 + 1.5x R (R=$0.07); T2 $65.74 = entry + 3x R; structure ceiling = 52w high $72.48"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $209.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.34)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
