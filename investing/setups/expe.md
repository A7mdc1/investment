---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $270.62 ahead of the 2026-11-04 print"
entry_price: 270.62
stop_price: 262.42
stop_logic: "chandelier trail: HH22 $294.84 - 3x ATR $10.81 = $262.42 — exit when decline exceeds ~3 average daily ranges"
target_price: 282.93
target_logic: "T1 $282.93 = entry $270.62 + 1.5x R (R=$8.20); T2 $295.23 = entry + 3x R; structure ceiling = 52w high $341.69"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $584.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($10.81)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
