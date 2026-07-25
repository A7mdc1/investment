---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $74.56 ahead of the 2026-08-26 print"
entry_price: 74.56
stop_price: 69.65
stop_logic: "chandelier trail: HH22 $82.57 - 3x ATR $4.31 = $69.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 81.93
target_logic: "T1 $81.93 = entry $74.56 + 1.5x R (R=$4.91); T2 $89.30 = entry + 3x R; structure ceiling = 52w high $100.62"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $190.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.31)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
