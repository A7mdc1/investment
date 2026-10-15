---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $93.33 ahead of the 2026-11-24 print"
entry_price: 93.33
stop_price: 88.05
stop_logic: "chandelier trail: HH22 $96.53 - 3x ATR $2.83 = $88.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 101.26
target_logic: "T1 $101.26 = entry $93.33 + 1.5x R (R=$5.28); T2 $109.18 = entry + 3x R; structure ceiling = 52w high $96.51"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $267.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.83)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
