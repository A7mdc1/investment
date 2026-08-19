---
ticker: AA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $50.43 ahead of the 2026-10-15 print"
entry_price: 50.43
stop_price: 49.30
stop_logic: "chandelier trail: HH22 $55.05 - 3x ATR $1.92 = $49.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 52.12
target_logic: "T1 $52.12 = entry $50.43 + 1.5x R (R=$1.12); T2 $53.80 = entry + 3x R; structure ceiling = 52w high $84.19"
holding_window_days: 21
catalyst: "2026-10-15 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $232.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.92)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
