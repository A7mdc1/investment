---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $177.37 ahead of the 2026-10-30 print"
entry_price: 177.37
stop_price: 168.60
stop_logic: "chandelier trail: HH22 $178.69 - 3x ATR $3.36 = $168.60 — exit when decline exceeds ~3 average daily ranges"
target_price: 190.52
target_logic: "T1 $190.52 = entry $177.37 + 1.5x R (R=$8.77); T2 $203.67 = entry + 3x R; structure ceiling = 52w high $178.62"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1879.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.36)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
