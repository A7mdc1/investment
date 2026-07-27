---
ticker: DLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $14.82 ahead of the 2026-08-13 print"
entry_price: 14.82
stop_price: 13.53
stop_logic: "chandelier trail: HH22 $15.51 - 3x ATR $0.66 = $13.53 — exit when decline exceeds ~3 average daily ranges"
target_price: 16.76
target_logic: "T1 $16.76 = entry $14.82 + 1.5x R (R=$1.29); T2 $18.70 = entry + 3x R; structure ceiling = 52w high $16.50"
holding_window_days: 21
catalyst: "2026-08-13 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $38.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.66)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
