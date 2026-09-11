---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $66.45 ahead of the 2026-10-22 print"
entry_price: 66.45
stop_price: 65.77
stop_logic: "chandelier trail: HH22 $72.56 - 3x ATR $2.26 = $65.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 67.47
target_logic: "T1 $67.47 = entry $66.45 + 1.5x R (R=$0.68); T2 $68.49 = entry + 3x R; structure ceiling = 52w high $72.54"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $204.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.26)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
