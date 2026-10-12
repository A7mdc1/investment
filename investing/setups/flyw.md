---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.59 ahead of the 2026-11-03 print"
entry_price: 18.59
stop_price: 17.30
stop_logic: "chandelier trail: HH22 $18.80 - 3x ATR $0.50 = $17.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 20.52
target_logic: "T1 $20.52 = entry $18.59 + 1.5x R (R=$1.29); T2 $22.45 = entry + 3x R; structure ceiling = 52w high $19.73"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $24.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.50)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
