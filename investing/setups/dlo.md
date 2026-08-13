---
ticker: DLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $14.53 ahead of the 2026-08-13 print"
entry_price: 14.53
stop_price: 14.11
stop_logic: "chandelier trail: HH22 $15.65 - 3x ATR $0.51 = $14.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 15.15
target_logic: "T1 $15.15 = entry $14.53 + 1.5x R (R=$0.42); T2 $15.77 = entry + 3x R; structure ceiling = 52w high $16.51"
holding_window_days: 21
catalyst: "2026-08-13 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $25.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.51)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
