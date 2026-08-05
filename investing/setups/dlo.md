---
ticker: DLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $15.22 ahead of the 2026-08-13 print"
entry_price: 15.22
stop_price: 14.01
stop_logic: "chandelier trail: HH22 $15.65 - 3x ATR $0.55 = $14.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 17.03
target_logic: "T1 $17.03 = entry $15.22 + 1.5x R (R=$1.21); T2 $18.84 = entry + 3x R; structure ceiling = 52w high $16.51"
holding_window_days: 21
catalyst: "2026-08-13 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $25.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.55)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
