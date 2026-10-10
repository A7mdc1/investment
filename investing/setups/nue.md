---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $250.33 ahead of the 2026-10-26 print"
entry_price: 250.33
stop_price: 245.21
stop_logic: "chandelier trail: HH22 $267.44 - 3x ATR $7.41 = $245.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 258.01
target_logic: "T1 $258.01 = entry $250.33 + 1.5x R (R=$5.12); T2 $265.70 = entry + 3x R; structure ceiling = 52w high $279.39"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $322.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.41)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
