---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1273.46 ahead of the 2026-10-29 print"
entry_price: 1273.46
stop_price: 1207.51
stop_logic: "chandelier trail: HH22 $1321.21 - 3x ATR $37.90 = $1207.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 1372.38
target_logic: "T1 $1372.38 = entry $1273.46 + 1.5x R (R=$65.95); T2 $1471.30 = entry + 3x R; structure ceiling = 52w high $1321.02"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2798.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($37.90)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
