---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.61 ahead of the 2026-11-03 print"
entry_price: 18.61
stop_price: 17.80
stop_logic: "chandelier trail: HH22 $19.54 - 3x ATR $0.58 = $17.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 19.82
target_logic: "T1 $19.82 = entry $18.61 + 1.5x R (R=$0.81); T2 $21.03 = entry + 3x R; structure ceiling = 52w high $19.73"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $24.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.58)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
