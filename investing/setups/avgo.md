---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $390.52 ahead of the 2026-09-03 print"
entry_price: 390.52
stop_price: 361.94
stop_logic: "chandelier trail: HH22 $407.52 - 3x ATR $15.19 = $361.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 433.40
target_logic: "T1 $433.40 = entry $390.52 + 1.5x R (R=$28.59); T2 $476.28 = entry + 3x R; structure ceiling = 52w high $494.34"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $8423.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.19)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
