---
ticker: DLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $14.49 ahead of the 2026-08-13 print"
entry_price: 14.49
stop_price: 13.55
stop_logic: "chandelier trail: HH22 $15.51 - 3x ATR $0.65 = $13.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 15.90
target_logic: "T1 $15.90 = entry $14.49 + 1.5x R (R=$0.94); T2 $17.31 = entry + 3x R; structure ceiling = 52w high $16.50"
holding_window_days: 21
catalyst: "2026-08-13 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $46.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.65)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
