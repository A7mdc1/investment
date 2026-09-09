---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $70.78 ahead of the 2026-10-22 print"
entry_price: 70.78
stop_price: 66.22
stop_logic: "chandelier trail: HH22 $72.56 - 3x ATR $2.11 = $66.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 77.61
target_logic: "T1 $77.61 = entry $70.78 + 1.5x R (R=$4.56); T2 $84.45 = entry + 3x R; structure ceiling = 52w high $72.59"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $196.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.11)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
