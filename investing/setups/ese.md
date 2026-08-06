---
ticker: ESE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $330.24 ahead of the 2026-08-06 print"
entry_price: 330.24
stop_price: 305.94
stop_logic: "chandelier trail: HH22 $339.22 - 3x ATR $11.10 = $305.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 366.70
target_logic: "T1 $366.70 = entry $330.24 + 1.5x R (R=$24.31); T2 $403.16 = entry + 3x R; structure ceiling = 52w high $362.11"
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $54.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.10)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
