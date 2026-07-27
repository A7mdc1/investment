---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $423.60 ahead of the 2026-09-03 print"
entry_price: 423.60
stop_price: 366.61
stop_logic: "chandelier trail: HH22 $462.72 - 3x ATR $32.03 = $366.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 509.08
target_logic: "T1 $509.08 = entry $423.60 + 1.5x R (R=$56.99); T2 $594.56 = entry + 3x R; structure ceiling = 52w high $468.58"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2816.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.03)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
