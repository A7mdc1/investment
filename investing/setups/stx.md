---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $910.34 ahead of the 2026-07-28 print"
entry_price: 910.34
stop_price: 889.96
stop_logic: "chandelier trail: HH22 $1144.18 - 3x ATR $84.74 = $889.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 940.91
target_logic: "T1 $940.91 = entry $910.34 + 1.5x R (R=$20.38); T2 $971.49 = entry + 3x R; structure ceiling = 52w high $1143.64"
holding_window_days: 21
catalyst: "2026-07-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $4924.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($84.74)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
