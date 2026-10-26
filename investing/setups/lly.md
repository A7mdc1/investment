---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1279.14 ahead of the 2026-10-29 print"
entry_price: 1279.14
stop_price: 1210.70
stop_logic: "chandelier trail: HH22 $1321.21 - 3x ATR $36.84 = $1210.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 1381.80
target_logic: "T1 $1381.80 = entry $1279.14 + 1.5x R (R=$68.44); T2 $1484.46 = entry + 3x R; structure ceiling = 52w high $1321.43"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2747.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($36.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
