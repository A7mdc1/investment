---
ticker: PAY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $28.15 ahead of the 2026-08-03 print"
entry_price: 28.15
stop_price: 25.00
stop_logic: "chandelier trail: HH22 $28.28 - 3x ATR $1.09 = $25.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 32.87
target_logic: "T1 $32.87 = entry $28.15 + 1.5x R (R=$3.15); T2 $37.59 = entry + 3x R; structure ceiling = 52w high $39.37"
holding_window_days: 21
catalyst: "2026-08-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $33.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.09)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
