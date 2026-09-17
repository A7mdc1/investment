---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $201.50 ahead of the 2026-10-29 print"
entry_price: 201.50
stop_price: 199.59
stop_logic: "chandelier trail: HH22 $225.00 - 3x ATR $8.47 = $199.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 204.36
target_logic: "T1 $204.36 = entry $201.50 + 1.5x R (R=$1.91); T2 $207.22 = entry + 3x R; structure ceiling = 52w high $320.86"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $391.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.47)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
