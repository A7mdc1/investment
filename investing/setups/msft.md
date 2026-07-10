---
ticker: MSFT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $385.18 ahead of the 2026-07-29 print"
entry_price: 385.18
stop_price: 375.66
stop_logic: "chandelier trail: HH22 $411.98 - 3x ATR $12.11 = $375.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 399.46
target_logic: "T1 $399.46 = entry $385.18 + 1.5x R (R=$9.52); T2 $413.75 = entry + 3x R; structure ceiling = 52w high $551.04"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $17928.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($12.11)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
