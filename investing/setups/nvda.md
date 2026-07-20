---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $203.57 ahead of the 2026-08-26 print"
entry_price: 203.57
stop_price: 193.01
stop_logic: "chandelier trail: HH22 $213.99 - 3x ATR $6.99 = $193.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 219.41
target_logic: "T1 $219.41 = entry $203.57 + 1.5x R (R=$10.56); T2 $235.25 = entry + 3x R; structure ceiling = 52w high $236.16"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $27223.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.99)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
