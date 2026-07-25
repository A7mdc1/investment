---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $206.84 ahead of the 2026-08-26 print"
entry_price: 206.84
stop_price: 193.31
stop_logic: "chandelier trail: HH22 $214.39 - 3x ATR $7.03 = $193.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 227.14
target_logic: "T1 $227.14 = entry $206.84 + 1.5x R (R=$13.53); T2 $247.44 = entry + 3x R; structure ceiling = 52w high $236.39"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $26811.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.03)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
