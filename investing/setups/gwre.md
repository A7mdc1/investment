---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $141.89 ahead of the 2026-09-03 print"
entry_price: 141.89
stop_price: 126.00
stop_logic: "chandelier trail: HH22 $146.69 - 3x ATR $6.90 = $126.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 165.73
target_logic: "T1 $165.73 = entry $141.89 + 1.5x R (R=$15.89); T2 $189.56 = entry + 3x R; structure ceiling = 52w high $272.34"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $218.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.90)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
