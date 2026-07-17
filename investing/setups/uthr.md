---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $537.63 ahead of the 2026-07-29 print"
entry_price: 537.63
stop_price: 524.03
stop_logic: "chandelier trail: HH22 $563.70 - 3x ATR $13.22 = $524.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 558.03
target_logic: "T1 $558.03 = entry $537.63 + 1.5x R (R=$13.60); T2 $578.42 = entry + 3x R; structure ceiling = 52w high $609.56"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $290.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.22)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
