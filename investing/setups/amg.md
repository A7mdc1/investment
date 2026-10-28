---
ticker: AMG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $390.51 ahead of the 2026-11-02 print"
entry_price: 390.51
stop_price: 366.58
stop_logic: "chandelier trail: HH22 $399.00 - 3x ATR $10.81 = $366.58 — exit when decline exceeds ~3 average daily ranges"
target_price: 426.40
target_logic: "T1 $426.40 = entry $390.51 + 1.5x R (R=$23.93); T2 $462.29 = entry + 3x R; structure ceiling = 52w high $398.89"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $99.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($10.81)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
