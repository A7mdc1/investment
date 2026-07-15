---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $85.74 ahead of the 2026-08-27 print"
entry_price: 85.74
stop_price: 78.73
stop_logic: "chandelier trail: HH22 $86.35 - 3x ATR $2.54 = $78.73 — exit when decline exceeds ~3 average daily ranges"
target_price: 96.26
target_logic: "T1 $96.26 = entry $85.74 + 1.5x R (R=$7.01); T2 $106.78 = entry + 3x R; structure ceiling = 52w high $86.34"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $302.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.54)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
