---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1197.58 ahead of the 2026-10-29 print"
entry_price: 1197.58
stop_price: 1123.03
stop_logic: "chandelier trail: HH22 $1215.00 - 3x ATR $30.66 = $1123.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 1309.41
target_logic: "T1 $1309.41 = entry $1197.58 + 1.5x R (R=$74.55); T2 $1421.24 = entry + 3x R; structure ceiling = 52w high $1293.28"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2530.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($30.66)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
