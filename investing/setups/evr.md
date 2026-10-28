---
ticker: EVR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $292.81 ahead of the 2026-10-28 print"
entry_price: 292.81
stop_price: 264.26
stop_logic: "chandelier trail: HH22 $292.96 - 3x ATR $9.57 = $264.26 — exit when decline exceeds ~3 average daily ranges"
target_price: 335.65
target_logic: "T1 $335.65 = entry $292.81 + 1.5x R (R=$28.56); T2 $378.48 = entry + 3x R; structure ceiling = 52w high $385.79"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $156.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($9.57)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
