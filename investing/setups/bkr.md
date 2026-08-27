---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $61.91 ahead of the 2026-10-22 print"
entry_price: 61.91
stop_price: 60.83
stop_logic: "chandelier trail: HH22 $65.44 - 3x ATR $1.54 = $60.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.52
target_logic: "T1 $63.52 = entry $61.91 + 1.5x R (R=$1.08); T2 $65.14 = entry + 3x R; structure ceiling = 52w high $69.95"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $370.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.54)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
