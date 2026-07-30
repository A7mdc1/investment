---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $406.34 ahead of the 2026-09-03 print"
entry_price: 406.34
stop_price: 361.54
stop_logic: "chandelier trail: HH22 $462.72 - 3x ATR $33.73 = $361.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 473.54
target_logic: "T1 $473.54 = entry $406.34 + 1.5x R (R=$44.80); T2 $540.75 = entry + 3x R; structure ceiling = 52w high $468.67"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2776.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($33.73)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
