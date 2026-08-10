---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $535.15 ahead of the 2026-08-17 print"
entry_price: 535.15
stop_price: 468.83
stop_logic: "chandelier trail: HH22 $579.47 - 3x ATR $36.88 = $468.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 634.65
target_logic: "T1 $634.65 = entry $535.15 + 1.5x R (R=$66.33); T2 $734.14 = entry + 3x R; structure ceiling = 52w high $748.47"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $377.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($36.88)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
