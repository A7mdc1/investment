---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $207.30 ahead of the 2026-08-26 print"
entry_price: 207.30
stop_price: 193.24
stop_logic: "chandelier trail: HH22 $213.99 - 3x ATR $6.92 = $193.24 — exit when decline exceeds ~3 average daily ranges"
target_price: 228.39
target_logic: "T1 $228.39 = entry $207.30 + 1.5x R (R=$14.06); T2 $249.49 = entry + 3x R; structure ceiling = 52w high $236.37"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $28496.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.92)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
