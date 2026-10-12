---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1178.11 ahead of the 2026-10-29 print"
entry_price: 1178.11
stop_price: 1118.59
stop_logic: "chandelier trail: HH22 $1215.00 - 3x ATR $32.14 = $1118.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 1267.38
target_logic: "T1 $1267.38 = entry $1178.11 + 1.5x R (R=$59.52); T2 $1356.66 = entry + 3x R; structure ceiling = 52w high $1293.20"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2553.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.14)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
