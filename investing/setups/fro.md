---
ticker: FRO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.90 ahead of the 2026-11-30 print"
entry_price: 56.90
stop_price: 52.26
stop_logic: "chandelier trail: HH22 $59.75 - 3x ATR $2.50 = $52.26 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.86
target_logic: "T1 $63.86 = entry $56.90 + 1.5x R (R=$4.64); T2 $70.83 = entry + 3x R; structure ceiling = 52w high $59.77"
holding_window_days: 21
catalyst: "2026-11-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $232.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
