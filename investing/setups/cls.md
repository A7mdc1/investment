---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $342.00 ahead of the 2026-07-27 print"
entry_price: 342.00
stop_price: 306.80
stop_logic: "chandelier trail: HH22 $378.00 - 3x ATR $23.73 = $306.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 394.80
target_logic: "T1 $394.80 = entry $342.00 + 1.5x R (R=$35.20); T2 $447.61 = entry + 3x R; structure ceiling = 52w high $474.34"
holding_window_days: 21
catalyst: "2026-07-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $598.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($23.73)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
