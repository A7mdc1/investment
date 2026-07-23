---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $442.22 ahead of the 2026-09-03 print"
entry_price: 442.22
stop_price: 365.69
stop_logic: "chandelier trail: HH22 $462.72 - 3x ATR $32.34 = $365.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 557.02
target_logic: "T1 $557.02 = entry $442.22 + 1.5x R (R=$76.53); T2 $671.82 = entry + 3x R; structure ceiling = 52w high $468.45"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3055.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.34)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
