---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $200.40 ahead of the 2026-08-05 print"
entry_price: 200.40
stop_price: 185.88
stop_logic: "chandelier trail: HH22 $202.72 - 3x ATR $5.61 = $185.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 222.16
target_logic: "T1 $222.16 = entry $200.40 + 1.5x R (R=$14.51); T2 $243.93 = entry + 3x R; structure ceiling = 52w high $202.62"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $535.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.61)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
