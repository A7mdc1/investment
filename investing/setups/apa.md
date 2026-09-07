---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $42.77 ahead of the 2026-11-04 print"
entry_price: 42.77
stop_price: 40.53
stop_logic: "chandelier trail: HH22 $45.13 - 3x ATR $1.53 = $40.53 — exit when decline exceeds ~3 average daily ranges"
target_price: 46.13
target_logic: "T1 $46.13 = entry $42.77 + 1.5x R (R=$2.24); T2 $49.49 = entry + 3x R; structure ceiling = 52w high $45.12"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $221.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.53)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
