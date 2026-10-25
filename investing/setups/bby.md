---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $99.87 ahead of the 2026-11-24 print"
entry_price: 99.87
stop_price: 91.88
stop_logic: "chandelier trail: HH22 $100.58 - 3x ATR $2.90 = $91.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 111.86
target_logic: "T1 $111.86 = entry $99.87 + 1.5x R (R=$7.99); T2 $123.85 = entry + 3x R; structure ceiling = 52w high $100.57"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $260.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.90)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
