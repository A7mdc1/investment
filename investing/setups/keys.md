---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $357.82 ahead of the 2026-08-18 print"
entry_price: 357.82
stop_price: 322.74
stop_logic: "chandelier trail: HH22 $361.09 - 3x ATR $12.78 = $322.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 410.44
target_logic: "T1 $410.44 = entry $357.82 + 1.5x R (R=$35.08); T2 $463.05 = entry + 3x R; structure ceiling = 52w high $375.07"
holding_window_days: 21
catalyst: "2026-08-18 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $345.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($12.78)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
