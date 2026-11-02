---
ticker: BF-B
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $30.09 ahead of the 2026-12-03 print"
entry_price: 30.09
stop_price: 27.85
stop_logic: "chandelier trail: HH22 $30.20 - 3x ATR $0.78 = $27.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 33.46
target_logic: "T1 $33.46 = entry $30.09 + 1.5x R (R=$2.24); T2 $36.82 = entry + 3x R; structure ceiling = 52w high $30.84"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $72.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.78)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Beverages - Wineries & Distilleries' matches 'distiller' — core business fails screen
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
