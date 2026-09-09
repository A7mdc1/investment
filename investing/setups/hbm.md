---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $29.00 ahead of the 2026-10-29 print"
entry_price: 29.00
stop_price: 26.87
stop_logic: "chandelier trail: HH22 $30.81 - 3x ATR $1.31 = $26.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 32.18
target_logic: "T1 $32.18 = entry $29.00 + 1.5x R (R=$2.13); T2 $35.37 = entry + 3x R; structure ceiling = 52w high $32.15"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $113.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.31)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
