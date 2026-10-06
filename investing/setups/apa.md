---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $44.28 ahead of the 2026-11-04 print"
entry_price: 44.28
stop_price: 42.71
stop_logic: "chandelier trail: HH22 $47.44 - 3x ATR $1.58 = $42.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 46.65
target_logic: "T1 $46.65 = entry $44.28 + 1.5x R (R=$1.58); T2 $49.02 = entry + 3x R; structure ceiling = 52w high $47.47"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $266.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.58)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
