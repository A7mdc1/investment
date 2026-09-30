---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $26.79 ahead of the 2026-10-29 print"
entry_price: 26.79
stop_price: 25.96
stop_logic: "chandelier trail: HH22 $29.95 - 3x ATR $1.33 = $25.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 28.03
target_logic: "T1 $28.03 = entry $26.79 + 1.5x R (R=$0.83); T2 $29.28 = entry + 3x R; structure ceiling = 52w high $32.12"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $106.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.33)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
