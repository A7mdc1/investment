---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $533.74 ahead of the 2026-07-29 print"
entry_price: 533.74
stop_price: 523.83
stop_logic: "chandelier trail: HH22 $563.70 - 3x ATR $13.29 = $523.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 548.59
target_logic: "T1 $548.59 = entry $533.74 + 1.5x R (R=$9.90); T2 $563.44 = entry + 3x R; structure ceiling = 52w high $609.29"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $294.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.29)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
