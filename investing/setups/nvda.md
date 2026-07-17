---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $206.62 ahead of the 2026-08-26 print"
entry_price: 206.62
stop_price: 192.98
stop_logic: "chandelier trail: HH22 $213.99 - 3x ATR $7.00 = $192.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 227.08
target_logic: "T1 $227.08 = entry $206.62 + 1.5x R (R=$13.64); T2 $247.55 = entry + 3x R; structure ceiling = 52w high $236.14"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $28780.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
