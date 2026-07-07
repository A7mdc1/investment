---
ticker: GDDY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $90.37 ahead of the 2026-07-30 print"
entry_price: 90.37
stop_price: 79.00
stop_logic: "chandelier trail: HH22 $91.19 - 3x ATR $4.06 = $79.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 107.42
target_logic: "T1 $107.42 = entry $90.37 + 1.5x R (R=$11.37); T2 $124.48 = entry + 3x R; structure ceiling = 52w high $179.66"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $212.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.06)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
