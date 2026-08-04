---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $86.90 ahead of the 2026-08-26 print"
entry_price: 86.90
stop_price: 73.24
stop_logic: "chandelier trail: HH22 $86.90 - 3x ATR $4.55 = $73.24 — exit when decline exceeds ~3 average daily ranges"
target_price: 107.39
target_logic: "T1 $107.39 = entry $86.90 + 1.5x R (R=$13.66); T2 $127.88 = entry + 3x R; structure ceiling = 52w high $100.58"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $167.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.55)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
