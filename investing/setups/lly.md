---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1147.79 ahead of the 2026-10-29 print"
entry_price: 1147.79
stop_price: 1126.50
stop_logic: "chandelier trail: HH22 $1215.00 - 3x ATR $29.50 = $1126.50 — exit when decline exceeds ~3 average daily ranges"
target_price: 1179.71
target_logic: "T1 $1179.71 = entry $1147.79 + 1.5x R (R=$21.28); T2 $1211.64 = entry + 3x R; structure ceiling = 52w high $1292.55"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2554.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
