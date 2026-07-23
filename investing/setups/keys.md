---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $327.97 ahead of the 2026-08-18 print"
entry_price: 327.97
stop_price: 325.11
stop_logic: "chandelier trail: HH22 $368.99 - 3x ATR $14.63 = $325.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 332.26
target_logic: "T1 $332.26 = entry $327.97 + 1.5x R (R=$2.86); T2 $336.54 = entry + 3x R; structure ceiling = 52w high $374.82"
holding_window_days: 21
catalyst: "2026-08-18 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $502.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($14.63)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
