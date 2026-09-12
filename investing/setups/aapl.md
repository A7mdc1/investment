---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $332.27 ahead of the 2026-10-29 print"
entry_price: 332.27
stop_price: 314.76
stop_logic: "chandelier trail: HH22 $336.22 - 3x ATR $7.15 = $314.76 — exit when decline exceeds ~3 average daily ranges"
target_price: 358.53
target_logic: "T1 $358.53 = entry $332.27 + 1.5x R (R=$17.51); T2 $384.79 = entry + 3x R; structure ceiling = 52w high $344.32"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13497.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.15)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
