---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $397.70 ahead of the 2026-09-02 print"
entry_price: 397.70
stop_price: 385.37
stop_logic: "chandelier trail: HH22 $432.73 - 3x ATR $15.79 = $385.37 — exit when decline exceeds ~3 average daily ranges"
target_price: 416.20
target_logic: "T1 $416.20 = entry $397.70 + 1.5x R (R=$12.33); T2 $434.69 = entry + 3x R; structure ceiling = 52w high $494.04"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $7142.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.79)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
