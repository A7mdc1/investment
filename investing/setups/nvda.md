---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $208.19 ahead of the 2026-08-26 print"
entry_price: 208.19
stop_price: 193.65
stop_logic: "chandelier trail: HH22 $213.99 - 3x ATR $6.78 = $193.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 230.00
target_logic: "T1 $230.00 = entry $208.19 + 1.5x R (R=$14.54); T2 $251.81 = entry + 3x R; structure ceiling = 52w high $236.31"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $28518.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.78)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
