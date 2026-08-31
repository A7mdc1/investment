---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $159.29 ahead of the 2026-10-30 print"
entry_price: 159.29
stop_price: 157.86
stop_logic: "chandelier trail: HH22 $168.64 - 3x ATR $3.59 = $157.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 161.43
target_logic: "T1 $161.43 = entry $159.29 + 1.5x R (R=$1.43); T2 $163.57 = entry + 3x R; structure ceiling = 52w high $174.09"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2167.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.59)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
