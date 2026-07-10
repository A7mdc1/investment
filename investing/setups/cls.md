---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $357.15 ahead of the 2026-07-27 print"
entry_price: 357.15
stop_price: 341.75
stop_logic: "chandelier trail: HH22 $414.13 - 3x ATR $24.13 = $341.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 380.26
target_logic: "T1 $380.26 = entry $357.15 + 1.5x R (R=$15.41); T2 $403.37 = entry + 3x R; structure ceiling = 52w high $474.31"
holding_window_days: 21
catalyst: "2026-07-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $598.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($24.13)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
