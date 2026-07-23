---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $516.90 ahead of the 2026-08-17 print"
entry_price: 516.90
stop_price: 493.93
stop_logic: "chandelier trail: HH22 $596.34 - 3x ATR $34.14 = $493.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 551.37
target_logic: "T1 $551.37 = entry $516.90 + 1.5x R (R=$22.98); T2 $585.84 = entry + 3x R; structure ceiling = 52w high $749.14"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $550.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($34.14)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
