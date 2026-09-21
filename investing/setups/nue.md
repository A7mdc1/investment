---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $244.82 ahead of the 2026-10-26 print"
entry_price: 244.82
stop_price: 244.04
stop_logic: "chandelier trail: HH22 $268.47 - 3x ATR $8.14 = $244.04 — exit when decline exceeds ~3 average daily ranges"
target_price: 246.00
target_logic: "T1 $246.00 = entry $244.82 + 1.5x R (R=$0.78); T2 $247.17 = entry + 3x R; structure ceiling = 52w high $280.12"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $289.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.14)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
