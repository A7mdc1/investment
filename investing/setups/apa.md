---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $43.96 ahead of the 2026-11-04 print"
entry_price: 43.96
stop_price: 42.80
stop_logic: "chandelier trail: HH22 $47.44 - 3x ATR $1.55 = $42.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 45.71
target_logic: "T1 $45.71 = entry $43.96 + 1.5x R (R=$1.16); T2 $47.45 = entry + 3x R; structure ceiling = 52w high $47.42"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $236.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.55)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
