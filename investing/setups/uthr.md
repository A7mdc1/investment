---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $535.67 ahead of the 2026-07-29 print"
entry_price: 535.67
stop_price: 524.00
stop_logic: "chandelier trail: HH22 $563.70 - 3x ATR $13.23 = $524.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 553.18
target_logic: "T1 $553.18 = entry $535.67 + 1.5x R (R=$11.67); T2 $570.69 = entry + 3x R; structure ceiling = 52w high $609.41"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $297.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.23)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
