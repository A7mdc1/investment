---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.62 ahead of the 2026-08-04 print"
entry_price: 18.62
stop_price: 16.72
stop_logic: "chandelier trail: HH22 $18.98 - 3x ATR $0.75 = $16.72 — exit when decline exceeds ~3 average daily ranges"
target_price: 21.47
target_logic: "T1 $21.47 = entry $18.62 + 1.5x R (R=$1.90); T2 $24.33 = entry + 3x R; structure ceiling = 52w high $18.98"
holding_window_days: 21
catalyst: "2026-08-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $41.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.75)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
