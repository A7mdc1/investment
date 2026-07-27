---
ticker: PAAS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $44.19 ahead of the 2026-08-12 print"
entry_price: 44.19
stop_price: 41.98
stop_logic: "chandelier trail: HH22 $47.37 - 3x ATR $1.80 = $41.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 47.51
target_logic: "T1 $47.51 = entry $44.19 + 1.5x R (R=$2.21); T2 $50.83 = entry + 3x R; structure ceiling = 52w high $69.59"
holding_window_days: 21
catalyst: "2026-08-12 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $168.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.80)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
