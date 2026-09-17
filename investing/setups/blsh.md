---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $35.73 ahead of the 2026-11-12 print"
entry_price: 35.73
stop_price: 32.37
stop_logic: "chandelier trail: HH22 $39.55 - 3x ATR $2.40 = $32.37 — exit when decline exceeds ~3 average daily ranges"
target_price: 40.77
target_logic: "T1 $40.77 = entry $35.73 + 1.5x R (R=$3.36); T2 $45.82 = entry + 3x R; structure ceiling = 52w high $74.91"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $52.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.40)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
