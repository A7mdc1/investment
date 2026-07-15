---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $394.77 ahead of the 2026-09-03 print"
entry_price: 394.77
stop_price: 367.27
stop_logic: "chandelier trail: HH22 $463.48 - 3x ATR $32.07 = $367.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 436.04
target_logic: "T1 $436.04 = entry $394.77 + 1.5x R (R=$27.51); T2 $477.30 = entry + 3x R; structure ceiling = 52w high $469.41"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3312.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.07)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
