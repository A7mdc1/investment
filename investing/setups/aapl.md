---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $332.71 ahead of the 2026-10-29 print"
entry_price: 332.71
stop_price: 324.75
stop_logic: "chandelier trail: HH22 $345.34 - 3x ATR $6.86 = $324.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 344.64
target_logic: "T1 $344.64 = entry $332.71 + 1.5x R (R=$7.96); T2 $356.58 = entry + 3x R; structure ceiling = 52w high $345.49"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13568.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.86)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
