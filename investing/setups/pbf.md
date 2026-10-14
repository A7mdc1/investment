---
ticker: PBF
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $88.86 ahead of the 2026-10-29 print"
entry_price: 88.86
stop_price: 78.08
stop_logic: "chandelier trail: HH22 $92.46 - 3x ATR $4.79 = $78.08 — exit when decline exceeds ~3 average daily ranges"
target_price: 105.04
target_logic: "T1 $105.04 = entry $88.86 + 1.5x R (R=$10.78); T2 $121.21 = entry + 3x R; structure ceiling = 52w high $92.47"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $267.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.79)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
