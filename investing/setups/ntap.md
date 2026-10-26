---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $223.59 ahead of the 2026-12-01 print"
entry_price: 223.59
stop_price: 213.95
stop_logic: "chandelier trail: HH22 $240.87 - 3x ATR $8.97 = $213.95 — exit when decline exceeds ~3 average daily ranges"
target_price: 238.05
target_logic: "T1 $238.05 = entry $223.59 + 1.5x R (R=$9.64); T2 $252.51 = entry + 3x R; structure ceiling = 52w high $240.94"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $538.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.97)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
