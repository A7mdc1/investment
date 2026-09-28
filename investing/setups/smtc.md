---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $171.75 ahead of the 2026-11-23 print"
entry_price: 171.75
stop_price: 156.75
stop_logic: "chandelier trail: HH22 $190.64 - 3x ATR $11.30 = $156.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 194.25
target_logic: "T1 $194.25 = entry $171.75 + 1.5x R (R=$15.00); T2 $216.76 = entry + 3x R; structure ceiling = 52w high $190.62"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $525.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.30)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
