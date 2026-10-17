---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $24.59 ahead of the 2026-11-04 print"
entry_price: 24.59
stop_price: 22.59
stop_logic: "chandelier trail: HH22 $24.62 - 3x ATR $0.68 = $22.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 27.58
target_logic: "T1 $27.58 = entry $24.59 + 1.5x R (R=$2.00); T2 $30.58 = entry + 3x R; structure ceiling = 52w high $24.61"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $199.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.68)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
