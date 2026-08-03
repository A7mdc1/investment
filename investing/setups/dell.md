---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $420.80 ahead of the 2026-09-03 print"
entry_price: 420.80
stop_price: 360.03
stop_logic: "chandelier trail: HH22 $462.72 - 3x ATR $34.23 = $360.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 511.95
target_logic: "T1 $511.95 = entry $420.80 + 1.5x R (R=$60.77); T2 $603.10 = entry + 3x R; structure ceiling = 52w high $468.60"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2696.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($34.23)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
