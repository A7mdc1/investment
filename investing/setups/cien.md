---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $445.39 ahead of the 2026-09-09 print"
entry_price: 445.39
stop_price: 401.90
stop_logic: "chandelier trail: HH22 $494.53 - 3x ATR $30.88 = $401.90 — exit when decline exceeds ~3 average daily ranges"
target_price: 510.64
target_logic: "T1 $510.64 = entry $445.39 + 1.5x R (R=$43.49); T2 $575.88 = entry + 3x R; structure ceiling = 52w high $637.19"
holding_window_days: 21
catalyst: "2026-09-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1382.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($30.88)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
