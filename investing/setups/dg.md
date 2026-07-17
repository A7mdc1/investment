---
ticker: DG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $126.25 ahead of the 2026-08-27 print"
entry_price: 126.25
stop_price: 118.06
stop_logic: "chandelier trail: HH22 $130.60 - 3x ATR $4.18 = $118.06 — exit when decline exceeds ~3 average daily ranges"
target_price: 138.52
target_logic: "T1 $138.52 = entry $126.25 + 1.5x R (R=$8.19); T2 $150.80 = entry + 3x R; structure ceiling = 52w high $156.63"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $334.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.18)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: debt/mcap 56% > 33%
---

## Notes
Scaffolded 2026-07-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
