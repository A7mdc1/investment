---
ticker: SOLV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $90.28 ahead of the 2026-11-05 print"
entry_price: 90.28
stop_price: 83.00
stop_logic: "chandelier trail: HH22 $90.32 - 3x ATR $2.44 = $83.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 101.20
target_logic: "T1 $101.20 = entry $90.28 + 1.5x R (R=$7.28); T2 $112.12 = entry + 3x R; structure ceiling = 52w high $94.14"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $92.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.44)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
