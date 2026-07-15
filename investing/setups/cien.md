---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $415.81 ahead of the 2026-09-09 print"
entry_price: 415.81
stop_price: 399.11
stop_logic: "chandelier trail: HH22 $494.53 - 3x ATR $31.81 = $399.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 440.87
target_logic: "T1 $440.87 = entry $415.81 + 1.5x R (R=$16.71); T2 $465.93 = entry + 3x R; structure ceiling = 52w high $637.75"
holding_window_days: 21
catalyst: "2026-09-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1289.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($31.81)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
