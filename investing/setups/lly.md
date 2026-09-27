---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1183.46 ahead of the 2026-10-29 print"
entry_price: 1183.46
stop_price: 1147.84
stop_logic: "chandelier trail: HH22 $1235.78 - 3x ATR $29.31 = $1147.84 — exit when decline exceeds ~3 average daily ranges"
target_price: 1236.89
target_logic: "T1 $1236.89 = entry $1183.46 + 1.5x R (R=$35.62); T2 $1290.32 = entry + 3x R; structure ceiling = 52w high $1291.99"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2700.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.31)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
