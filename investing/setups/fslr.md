---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $201.01 ahead of the 2026-10-29 print"
entry_price: 201.01
stop_price: 195.89
stop_logic: "chandelier trail: HH22 $221.40 - 3x ATR $8.50 = $195.89 — exit when decline exceeds ~3 average daily ranges"
target_price: 208.71
target_logic: "T1 $208.71 = entry $201.01 + 1.5x R (R=$5.13); T2 $216.40 = entry + 3x R; structure ceiling = 52w high $321.11"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $408.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
