---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $394.94 ahead of the 2026-09-03 print"
entry_price: 394.94
stop_price: 366.78
stop_logic: "chandelier trail: HH22 $414.64 - 3x ATR $15.95 = $366.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 437.18
target_logic: "T1 $437.18 = entry $394.94 + 1.5x R (R=$28.16); T2 $479.41 = entry + 3x R; structure ceiling = 52w high $494.29"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $10622.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.95)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
