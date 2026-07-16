---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $400.01 ahead of the 2026-09-03 print"
entry_price: 400.01
stop_price: 368.31
stop_logic: "chandelier trail: HH22 $463.48 - 3x ATR $31.72 = $368.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 447.57
target_logic: "T1 $447.57 = entry $400.01 + 1.5x R (R=$31.70); T2 $495.12 = entry + 3x R; structure ceiling = 52w high $469.50"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3369.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($31.72)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
