---
ticker: ALL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $254.47 ahead of the 2026-11-04 print"
entry_price: 254.47
stop_price: 243.52
stop_logic: "chandelier trail: HH22 $259.37 - 3x ATR $5.28 = $243.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 270.89
target_logic: "T1 $270.89 = entry $254.47 + 1.5x R (R=$10.95); T2 $287.31 = entry + 3x R; structure ceiling = 52w high $276.00"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $398.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.28)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
