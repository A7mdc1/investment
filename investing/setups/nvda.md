---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $200.75 ahead of the 2026-08-26 print"
entry_price: 200.75
stop_price: 191.90
stop_logic: "chandelier trail: HH22 $214.39 - 3x ATR $7.50 = $191.90 — exit when decline exceeds ~3 average daily ranges"
target_price: 214.02
target_logic: "T1 $214.02 = entry $200.75 + 1.5x R (R=$8.85); T2 $227.29 = entry + 3x R; structure ceiling = 52w high $236.18"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $26043.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
