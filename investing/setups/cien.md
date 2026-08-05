---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $410.82 ahead of the 2026-09-09 print"
entry_price: 410.82
stop_price: 396.48
stop_logic: "chandelier trail: HH22 $485.69 - 3x ATR $29.74 = $396.48 — exit when decline exceeds ~3 average daily ranges"
target_price: 432.33
target_logic: "T1 $432.33 = entry $410.82 + 1.5x R (R=$14.34); T2 $453.83 = entry + 3x R; structure ceiling = 52w high $637.92"
holding_window_days: 21
catalyst: "2026-09-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $764.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.74)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
