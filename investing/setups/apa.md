---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $44.58 ahead of the 2026-11-04 print"
entry_price: 44.58
stop_price: 41.86
stop_logic: "chandelier trail: HH22 $46.10 - 3x ATR $1.41 = $41.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 48.66
target_logic: "T1 $48.66 = entry $44.58 + 1.5x R (R=$2.72); T2 $52.73 = entry + 3x R; structure ceiling = 52w high $46.10"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $212.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.41)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
