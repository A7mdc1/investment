---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $44.89 ahead of the 2026-11-04 print"
entry_price: 44.89
stop_price: 41.85
stop_logic: "chandelier trail: HH22 $46.10 - 3x ATR $1.42 = $41.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 49.45
target_logic: "T1 $49.45 = entry $44.89 + 1.5x R (R=$3.04); T2 $54.00 = entry + 3x R; structure ceiling = 52w high $46.09"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $207.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.42)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
