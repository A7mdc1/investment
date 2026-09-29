---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $54.05 ahead of the 2026-10-26 print"
entry_price: 54.05
stop_price: 47.85
stop_logic: "chandelier trail: HH22 $55.13 - 3x ATR $2.43 = $47.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.34
target_logic: "T1 $63.34 = entry $54.05 + 1.5x R (R=$6.20); T2 $72.64 = entry + 3x R; structure ceiling = 52w high $96.52"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $188.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.43)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
