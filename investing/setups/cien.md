---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $408.40 ahead of the 2026-09-09 print"
entry_price: 408.40
stop_price: 402.01
stop_logic: "chandelier trail: HH22 $494.53 - 3x ATR $30.84 = $402.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 417.98
target_logic: "T1 $417.98 = entry $408.40 + 1.5x R (R=$6.39); T2 $427.56 = entry + 3x R; structure ceiling = 52w high $637.13"
holding_window_days: 21
catalyst: "2026-09-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1059.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($30.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
