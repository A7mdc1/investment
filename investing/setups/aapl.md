---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $332.10 ahead of the 2026-07-30 print"
entry_price: 332.10
stop_price: 307.27
stop_logic: "chandelier trail: HH22 $332.37 - 3x ATR $8.37 = $307.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 369.33
target_logic: "T1 $369.33 = entry $332.10 + 1.5x R (R=$24.82); T2 $406.56 = entry + 3x R; structure ceiling = 52w high $332.43"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $19232.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.37)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
