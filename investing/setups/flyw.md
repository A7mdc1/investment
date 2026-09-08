---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $17.98 ahead of the 2026-11-03 print"
entry_price: 17.98
stop_price: 17.62
stop_logic: "chandelier trail: HH22 $19.73 - 3x ATR $0.70 = $17.62 — exit when decline exceeds ~3 average daily ranges"
target_price: 18.52
target_logic: "T1 $18.52 = entry $17.98 + 1.5x R (R=$0.36); T2 $19.07 = entry + 3x R; structure ceiling = 52w high $19.74"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $25.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.70)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
