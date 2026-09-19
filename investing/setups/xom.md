---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $163.54 ahead of the 2026-10-30 print"
entry_price: 163.54
stop_price: 158.82
stop_logic: "chandelier trail: HH22 $169.64 - 3x ATR $3.61 = $158.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 170.62
target_logic: "T1 $170.62 = entry $163.54 + 1.5x R (R=$4.72); T2 $177.71 = entry + 3x R; structure ceiling = 52w high $174.16"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2407.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.61)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
