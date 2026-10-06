---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $16.77 ahead of the 2026-10-23 print"
entry_price: 16.77
stop_price: 16.26
stop_logic: "chandelier trail: HH22 $19.12 - 3x ATR $0.95 = $16.26 — exit when decline exceeds ~3 average daily ranges"
target_price: 17.55
target_logic: "T1 $17.55 = entry $16.77 + 1.5x R (R=$0.52); T2 $18.33 = entry + 3x R; structure ceiling = 52w high $30.44"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $190.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.95)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
