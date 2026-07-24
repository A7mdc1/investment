---
ticker: SFD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $26.20 ahead of the 2026-08-11 print"
entry_price: 26.20
stop_price: 25.19
stop_logic: "chandelier trail: HH22 $26.81 - 3x ATR $0.54 = $25.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 27.73
target_logic: "T1 $27.73 = entry $26.20 + 1.5x R (R=$1.02); T2 $29.25 = entry + 3x R; structure ceiling = 52w high $29.44"
holding_window_days: 21
catalyst: "2026-08-11 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $32.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.54)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
