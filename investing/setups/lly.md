---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1271.55 ahead of the 2026-10-29 print"
entry_price: 1271.55
stop_price: 1200.40
stop_logic: "chandelier trail: HH22 $1311.75 - 3x ATR $37.12 = $1200.40 — exit when decline exceeds ~3 average daily ranges"
target_price: 1378.28
target_logic: "T1 $1378.28 = entry $1271.55 + 1.5x R (R=$71.15); T2 $1485.00 = entry + 3x R; structure ceiling = 52w high $1312.23"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2674.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($37.12)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
