---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $448.35 ahead of the 2026-08-17 print"
entry_price: 448.35
stop_price: 445.11
stop_logic: "chandelier trail: HH22 $543.56 - 3x ATR $32.82 = $445.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 453.21
target_logic: "T1 $453.21 = entry $448.35 + 1.5x R (R=$3.24); T2 $458.07 = entry + 3x R; structure ceiling = 52w high $748.50"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $365.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.82)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
