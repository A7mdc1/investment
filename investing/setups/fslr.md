---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $199.71 ahead of the 2026-10-29 print"
entry_price: 199.71
stop_price: 198.49
stop_logic: "chandelier trail: HH22 $225.00 - 3x ATR $8.84 = $198.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 201.53
target_logic: "T1 $201.53 = entry $199.71 + 1.5x R (R=$1.22); T2 $203.36 = entry + 3x R; structure ceiling = 52w high $321.08"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $404.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
