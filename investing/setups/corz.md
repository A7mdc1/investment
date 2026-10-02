---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $16.36 ahead of the 2026-10-23 print"
entry_price: 16.36
stop_price: 16.11
stop_logic: "chandelier trail: HH22 $19.12 - 3x ATR $1.00 = $16.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 16.74
target_logic: "T1 $16.74 = entry $16.36 + 1.5x R (R=$0.25); T2 $17.12 = entry + 3x R; structure ceiling = 52w high $30.47"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $191.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
