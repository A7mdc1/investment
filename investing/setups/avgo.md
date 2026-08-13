---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $422.00 ahead of the 2026-09-02 print"
entry_price: 422.00
stop_price: 385.64
stop_logic: "chandelier trail: HH22 $432.73 - 3x ATR $15.70 = $385.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 476.55
target_logic: "T1 $476.55 = entry $422.00 + 1.5x R (R=$36.36); T2 $531.10 = entry + 3x R; structure ceiling = 52w high $494.15"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $6914.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.70)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
