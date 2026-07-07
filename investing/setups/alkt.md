---
ticker: ALKT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.95 ahead of the 2026-07-29 print"
entry_price: 18.95
stop_price: 16.99
stop_logic: "chandelier trail: HH22 $19.48 - 3x ATR $0.83 = $16.99 — exit when decline exceeds ~3 average daily ranges"
target_price: 21.89
target_logic: "T1 $21.89 = entry $18.95 + 1.5x R (R=$1.96); T2 $24.83 = entry + 3x R; structure ceiling = 52w high $30.86"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $38.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.83)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
