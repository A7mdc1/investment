---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $475.46 ahead of the 2026-09-03 print"
entry_price: 475.46
stop_price: 381.79
stop_logic: "chandelier trail: HH22 $485.70 - 3x ATR $34.64 = $381.79 — exit when decline exceeds ~3 average daily ranges"
target_price: 615.97
target_logic: "T1 $615.97 = entry $475.46 + 1.5x R (R=$93.67); T2 $756.48 = entry + 3x R; structure ceiling = 52w high $485.66"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2669.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($34.64)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
