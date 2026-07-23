---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.40 ahead of the 2026-07-26 print"
entry_price: 56.40
stop_price: 54.24
stop_logic: "chandelier trail: HH22 $59.34 - 3x ATR $1.70 = $54.24 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.64
target_logic: "T1 $59.64 = entry $56.40 + 1.5x R (R=$2.16); T2 $62.88 = entry + 3x R; structure ceiling = 52w high $70.15"
holding_window_days: 21
catalyst: "2026-07-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $517.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.70)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
