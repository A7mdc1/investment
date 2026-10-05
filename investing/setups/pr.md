---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $22.55 ahead of the 2026-11-04 print"
entry_price: 22.55
stop_price: 22.45
stop_logic: "chandelier trail: HH22 $24.48 - 3x ATR $0.68 = $22.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 22.69
target_logic: "T1 $22.69 = entry $22.55 + 1.5x R (R=$0.09); T2 $22.83 = entry + 3x R; structure ceiling = 52w high $24.48"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $232.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.68)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
