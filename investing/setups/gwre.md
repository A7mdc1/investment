---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $175.59 ahead of the 2026-09-03 print"
entry_price: 175.59
stop_price: 157.22
stop_logic: "chandelier trail: HH22 $183.98 - 3x ATR $8.92 = $157.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 203.15
target_logic: "T1 $203.15 = entry $175.59 + 1.5x R (R=$18.37); T2 $230.71 = entry + 3x R; structure ceiling = 52w high $272.66"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $183.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.92)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
