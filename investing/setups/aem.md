---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $145.44 ahead of the 2026-07-29 print"
entry_price: 145.44
stop_price: 144.81
stop_logic: "chandelier trail: HH22 $160.55 - 3x ATR $5.25 = $144.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 146.37
target_logic: "T1 $146.37 = entry $145.44 + 1.5x R (R=$0.62); T2 $147.30 = entry + 3x R; structure ceiling = 52w high $254.70"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $368.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.25)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
