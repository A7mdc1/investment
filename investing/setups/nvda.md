---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $198.29 ahead of the 2026-08-26 print"
entry_price: 198.29
stop_price: 192.16
stop_logic: "chandelier trail: HH22 $214.39 - 3x ATR $7.41 = $192.16 — exit when decline exceeds ~3 average daily ranges"
target_price: 207.48
target_logic: "T1 $207.48 = entry $198.29 + 1.5x R (R=$6.13); T2 $216.67 = entry + 3x R; structure ceiling = 52w high $236.34"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $25233.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.41)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
