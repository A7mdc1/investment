---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.66 ahead of the 2026-10-23 print"
entry_price: 18.66
stop_price: 16.21
stop_logic: "chandelier trail: HH22 $19.26 - 3x ATR $1.02 = $16.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 22.33
target_logic: "T1 $22.33 = entry $18.66 + 1.5x R (R=$2.45); T2 $26.00 = entry + 3x R; structure ceiling = 52w high $30.48"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $193.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.02)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
