---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $279.94 ahead of the 2026-11-04 print"
entry_price: 279.94
stop_price: 268.31
stop_logic: "chandelier trail: HH22 $301.81 - 3x ATR $11.17 = $268.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 297.38
target_logic: "T1 $297.38 = entry $279.94 + 1.5x R (R=$11.63); T2 $314.82 = entry + 3x R; structure ceiling = 52w high $341.39"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $426.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.17)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
