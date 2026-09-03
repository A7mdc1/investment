---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $68.17 ahead of the 2026-10-22 print"
entry_price: 68.17
stop_price: 65.69
stop_logic: "chandelier trail: HH22 $71.93 - 3x ATR $2.08 = $65.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 71.89
target_logic: "T1 $71.89 = entry $68.17 + 1.5x R (R=$2.48); T2 $75.60 = entry + 3x R; structure ceiling = 52w high $71.91"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $182.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.08)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
