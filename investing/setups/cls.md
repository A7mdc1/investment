---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $348.11 ahead of the 2026-07-27 print"
entry_price: 348.11
stop_price: 344.42
stop_logic: "chandelier trail: HH22 $427.15 - 3x ATR $27.58 = $344.42 — exit when decline exceeds ~3 average daily ranges"
target_price: 353.65
target_logic: "T1 $353.65 = entry $348.11 + 1.5x R (R=$3.69); T2 $359.19 = entry + 3x R; structure ceiling = 52w high $474.26"
holding_window_days: 21
catalyst: "2026-07-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $635.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($27.58)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
