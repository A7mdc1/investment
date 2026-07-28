---
ticker: PAAS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $43.49 ahead of the 2026-08-12 print"
entry_price: 43.49
stop_price: 41.95
stop_logic: "chandelier trail: HH22 $47.37 - 3x ATR $1.81 = $41.95 — exit when decline exceeds ~3 average daily ranges"
target_price: 45.81
target_logic: "T1 $45.81 = entry $43.49 + 1.5x R (R=$1.54); T2 $48.13 = entry + 3x R; structure ceiling = 52w high $69.59"
holding_window_days: 21
catalyst: "2026-08-12 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $165.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.81)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
