---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $25.71 ahead of the 2026-11-04 print"
entry_price: 25.71
stop_price: 23.83
stop_logic: "chandelier trail: HH22 $25.96 - 3x ATR $0.71 = $23.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 28.54
target_logic: "T1 $28.54 = entry $25.71 + 1.5x R (R=$1.88); T2 $31.36 = entry + 3x R; structure ceiling = 52w high $25.97"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $200.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.71)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
