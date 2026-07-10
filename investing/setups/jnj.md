---
ticker: JNJ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $256.13 ahead of the 2026-07-15 print"
entry_price: 256.13
stop_price: 250.94
stop_logic: "chandelier trail: HH22 $269.43 - 3x ATR $6.17 = $250.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 263.92
target_logic: "T1 $263.92 = entry $256.13 + 1.5x R (R=$5.19); T2 $271.71 = entry + 3x R; structure ceiling = 52w high $269.33"
holding_window_days: 21
catalyst: "2026-07-15 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2164.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.17)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
