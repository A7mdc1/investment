---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $222.11 ahead of the 2026-12-01 print"
entry_price: 222.11
stop_price: 216.25
stop_logic: "chandelier trail: HH22 $240.87 - 3x ATR $8.21 = $216.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 230.90
target_logic: "T1 $230.90 = entry $222.11 + 1.5x R (R=$5.86); T2 $239.70 = entry + 3x R; structure ceiling = 52w high $240.90"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $556.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.21)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
