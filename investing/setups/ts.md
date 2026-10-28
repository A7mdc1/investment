---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $60.56 ahead of the 2026-11-04 print"
entry_price: 60.56
stop_price: 56.17
stop_logic: "chandelier trail: HH22 $60.84 - 3x ATR $1.56 = $56.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 67.15
target_logic: "T1 $67.15 = entry $60.56 + 1.5x R (R=$4.39); T2 $73.74 = entry + 3x R; structure ceiling = 52w high $64.63"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $62.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.56)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
