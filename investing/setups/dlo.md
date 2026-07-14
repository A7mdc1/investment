---
ticker: DLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $15.02 ahead of the 2026-08-13 print"
entry_price: 15.02
stop_price: 13.61
stop_logic: "chandelier trail: HH22 $15.51 - 3x ATR $0.63 = $13.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 17.13
target_logic: "T1 $17.13 = entry $15.02 + 1.5x R (R=$1.41); T2 $19.24 = entry + 3x R; structure ceiling = 52w high $16.51"
holding_window_days: 21
catalyst: "2026-08-13 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $45.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.63)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
