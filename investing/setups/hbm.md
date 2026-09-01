---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $27.38 ahead of the 2026-10-29 print"
entry_price: 27.38
stop_price: 26.88
stop_logic: "chandelier trail: HH22 $30.82 - 3x ATR $1.31 = $26.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 28.13
target_logic: "T1 $28.13 = entry $27.38 + 1.5x R (R=$0.50); T2 $28.88 = entry + 3x R; structure ceiling = 52w high $32.13"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $125.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.31)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
