---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $371.84 ahead of the 2026-09-03 print"
entry_price: 371.84
stop_price: 363.71
stop_logic: "chandelier trail: HH22 $425.81 - 3x ATR $20.70 = $363.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 384.04
target_logic: "T1 $384.04 = entry $371.84 + 1.5x R (R=$8.13); T2 $396.23 = entry + 3x R; structure ceiling = 52w high $494.47"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $11684.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($20.70)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
