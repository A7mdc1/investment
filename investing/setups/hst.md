---
ticker: HST
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $24.95 ahead of the 2026-11-04 print"
entry_price: 24.95
stop_price: 23.76
stop_logic: "chandelier trail: HH22 $25.30 - 3x ATR $0.51 = $23.76 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.74
target_logic: "T1 $26.74 = entry $24.95 + 1.5x R (R=$1.19); T2 $28.53 = entry + 3x R; structure ceiling = 52w high $25.49"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $190.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.51)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
