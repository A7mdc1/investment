---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $529.85 ahead of the 2026-07-29 print"
entry_price: 529.85
stop_price: 523.97
stop_logic: "chandelier trail: HH22 $563.70 - 3x ATR $13.24 = $523.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 538.67
target_logic: "T1 $538.67 = entry $529.85 + 1.5x R (R=$5.88); T2 $547.48 = entry + 3x R; structure ceiling = 52w high $609.02"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $289.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.24)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
