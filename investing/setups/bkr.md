---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $57.49 ahead of the 2026-10-27 print"
entry_price: 57.49
stop_price: 53.38
stop_logic: "chandelier trail: HH22 $58.19 - 3x ATR $1.60 = $53.38 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.64
target_logic: "T1 $63.64 = entry $57.49 + 1.5x R (R=$4.10); T2 $69.80 = entry + 3x R; structure ceiling = 52w high $69.93"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $329.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.60)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
