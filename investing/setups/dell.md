---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $448.74 ahead of the 2026-09-03 print"
entry_price: 448.74
stop_price: 381.34
stop_logic: "chandelier trail: HH22 $485.70 - 3x ATR $34.79 = $381.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 549.84
target_logic: "T1 $549.84 = entry $448.74 + 1.5x R (R=$67.40); T2 $650.95 = entry + 3x R; structure ceiling = 52w high $485.65"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2649.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($34.79)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
