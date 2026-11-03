---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $94.29 ahead of the 2026-11-24 print"
entry_price: 94.29
stop_price: 90.97
stop_logic: "chandelier trail: HH22 $100.58 - 3x ATR $3.20 = $90.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 99.27
target_logic: "T1 $99.27 = entry $94.29 + 1.5x R (R=$3.32); T2 $104.26 = entry + 3x R; structure ceiling = 52w high $100.63"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $256.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.20)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
