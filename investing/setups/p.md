---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $112.87 ahead of the 2026-08-26 print"
entry_price: 112.87
stop_price: 103.02
stop_logic: "chandelier trail: HH22 $119.10 - 3x ATR $5.36 = $103.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 127.64
target_logic: "T1 $127.64 = entry $112.87 + 1.5x R (R=$9.85); T2 $142.41 = entry + 3x R; structure ceiling = 52w high $119.06"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $277.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.36)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
