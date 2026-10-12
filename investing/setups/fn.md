---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $452.39 ahead of the 2026-11-02 print"
entry_price: 452.39
stop_price: 445.87
stop_logic: "chandelier trail: HH22 $515.00 - 3x ATR $23.04 = $445.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 462.17
target_logic: "T1 $462.17 = entry $452.39 + 1.5x R (R=$6.52); T2 $471.94 = entry + 3x R; structure ceiling = 52w high $748.99"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $359.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($23.04)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
