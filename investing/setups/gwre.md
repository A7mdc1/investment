---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $152.66 ahead of the 2026-09-03 print"
entry_price: 152.66
stop_price: 144.86
stop_logic: "chandelier trail: HH22 $170.00 - 3x ATR $8.38 = $144.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 164.36
target_logic: "T1 $164.36 = entry $152.66 + 1.5x R (R=$7.80); T2 $176.05 = entry + 3x R; structure ceiling = 52w high $272.61"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $183.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
