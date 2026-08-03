---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $320.30 ahead of the 2026-08-18 print"
entry_price: 320.30
stop_price: 292.59
stop_logic: "chandelier trail: HH22 $333.34 - 3x ATR $13.58 = $292.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 361.86
target_logic: "T1 $361.86 = entry $320.30 + 1.5x R (R=$27.71); T2 $403.42 = entry + 3x R; structure ceiling = 52w high $375.06"
holding_window_days: 21
catalyst: "2026-08-18 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $388.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.58)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
