---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $328.12 ahead of the 2026-10-29 print"
entry_price: 328.12
stop_price: 323.17
stop_logic: "chandelier trail: HH22 $345.34 - 3x ATR $7.39 = $323.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 335.54
target_logic: "T1 $335.54 = entry $328.12 + 1.5x R (R=$4.95); T2 $342.96 = entry + 3x R; structure ceiling = 52w high $345.39"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13724.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.39)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
