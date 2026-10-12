---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $269.35 ahead of the 2026-11-04 print"
entry_price: 269.35
stop_price: 262.80
stop_logic: "chandelier trail: HH22 $294.84 - 3x ATR $10.68 = $262.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 279.16
target_logic: "T1 $279.16 = entry $269.35 + 1.5x R (R=$6.54); T2 $288.98 = entry + 3x R; structure ceiling = 52w high $341.38"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $597.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($10.68)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
