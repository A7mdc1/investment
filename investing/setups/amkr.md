---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $54.27 ahead of the 2026-10-26 print"
entry_price: 54.27
stop_price: 46.87
stop_logic: "chandelier trail: HH22 $54.46 - 3x ATR $2.53 = $46.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.35
target_logic: "T1 $65.35 = entry $54.27 + 1.5x R (R=$7.39); T2 $76.44 = entry + 3x R; structure ceiling = 52w high $96.56"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $207.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.53)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
