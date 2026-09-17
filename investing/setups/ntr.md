---
ticker: NTR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $79.00 ahead of the 2026-11-04 print"
entry_price: 79.00
stop_price: 75.71
stop_logic: "chandelier trail: HH22 $82.55 - 3x ATR $2.28 = $75.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 83.93
target_logic: "T1 $83.93 = entry $79.00 + 1.5x R (R=$3.29); T2 $88.86 = entry + 3x R; structure ceiling = 52w high $83.95"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $196.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.28)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
