---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $200.90 ahead of the 2026-08-05 print"
entry_price: 200.90
stop_price: 184.54
stop_logic: "chandelier trail: HH22 $201.21 - 3x ATR $5.56 = $184.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 225.45
target_logic: "T1 $225.45 = entry $200.90 + 1.5x R (R=$16.36); T2 $250.00 = entry + 3x R; structure ceiling = 52w high $201.31"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $520.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.56)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
