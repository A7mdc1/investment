---
ticker: ULTA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $452.49 ahead of the 2026-08-27 print"
entry_price: 452.49
stop_price: 447.62
stop_logic: "chandelier trail: HH22 $493.98 - 3x ATR $15.45 = $447.62 — exit when decline exceeds ~3 average daily ranges"
target_price: 459.79
target_logic: "T1 $459.79 = entry $452.49 + 1.5x R (R=$4.87); T2 $467.09 = entry + 3x R; structure ceiling = 52w high $714.83"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $384.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.45)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
