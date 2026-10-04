---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $68.56 ahead of the 2026-10-29 print"
entry_price: 68.56
stop_price: 65.10
stop_logic: "chandelier trail: HH22 $72.46 - 3x ATR $2.45 = $65.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 73.75
target_logic: "T1 $73.75 = entry $68.56 + 1.5x R (R=$3.46); T2 $78.94 = entry + 3x R; structure ceiling = 52w high $72.47"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $204.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.45)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
