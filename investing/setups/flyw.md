---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $18.03 ahead of the 2026-08-04 print"
entry_price: 18.03
stop_price: 16.69
stop_logic: "chandelier trail: HH22 $18.92 - 3x ATR $0.74 = $16.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 20.04
target_logic: "T1 $20.04 = entry $18.03 + 1.5x R (R=$1.34); T2 $22.06 = entry + 3x R; structure ceiling = 52w high $18.92"
holding_window_days: 21
catalyst: "2026-08-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $42.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.74)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
