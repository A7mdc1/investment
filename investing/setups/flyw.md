---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.95 ahead of the 2026-11-03 print"
entry_price: 18.95
stop_price: 17.78
stop_logic: "chandelier trail: HH22 $19.54 - 3x ATR $0.59 = $17.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 20.71
target_logic: "T1 $20.71 = entry $18.95 + 1.5x R (R=$1.17); T2 $22.47 = entry + 3x R; structure ceiling = 52w high $19.74"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $22.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.59)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
