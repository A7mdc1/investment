---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $179.35 ahead of the 2026-11-23 print"
entry_price: 179.35
stop_price: 156.92
stop_logic: "chandelier trail: HH22 $190.64 - 3x ATR $11.24 = $156.92 — exit when decline exceeds ~3 average daily ranges"
target_price: 213.01
target_logic: "T1 $213.01 = entry $179.35 + 1.5x R (R=$22.44); T2 $246.66 = entry + 3x R; structure ceiling = 52w high $190.60"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $535.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.24)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
