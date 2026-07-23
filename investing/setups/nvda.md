---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $209.48 ahead of the 2026-08-26 print"
entry_price: 209.48
stop_price: 193.10
stop_logic: "chandelier trail: HH22 $214.39 - 3x ATR $7.10 = $193.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 234.06
target_logic: "T1 $234.06 = entry $209.48 + 1.5x R (R=$16.38); T2 $258.63 = entry + 3x R; structure ceiling = 52w high $236.17"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $26536.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.10)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
