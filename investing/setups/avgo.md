---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $377.70 ahead of the 2026-09-03 print"
entry_price: 377.70
stop_price: 366.49
stop_logic: "chandelier trail: HH22 $414.64 - 3x ATR $16.05 = $366.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 394.51
target_logic: "T1 $394.51 = entry $377.70 + 1.5x R (R=$11.21); T2 $411.32 = entry + 3x R; structure ceiling = 52w high $494.37"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $10064.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($16.05)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
