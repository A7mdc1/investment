---
ticker: ARW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $208.91 ahead of the 2026-08-06 print"
entry_price: 208.91
stop_price: 201.74
stop_logic: "chandelier trail: HH22 $225.62 - 3x ATR $7.96 = $201.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 219.66
target_logic: "T1 $219.66 = entry $208.91 + 1.5x R (R=$7.17); T2 $230.41 = entry + 3x R; structure ceiling = 52w high $237.40"
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $109.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.96)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
