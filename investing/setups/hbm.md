---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $26.89 ahead of the 2026-10-29 print"
entry_price: 26.89
stop_price: 26.57
stop_logic: "chandelier trail: HH22 $30.56 - 3x ATR $1.33 = $26.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 27.38
target_logic: "T1 $27.38 = entry $26.89 + 1.5x R (R=$0.32); T2 $27.86 = entry + 3x R; structure ceiling = 52w high $32.13"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $103.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.33)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
