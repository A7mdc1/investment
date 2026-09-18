---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $335.05 ahead of the 2026-10-29 print"
entry_price: 335.05
stop_price: 316.36
stop_logic: "chandelier trail: HH22 $338.49 - 3x ATR $7.38 = $316.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 363.08
target_logic: "T1 $363.08 = entry $335.05 + 1.5x R (R=$18.69); T2 $391.11 = entry + 3x R; structure ceiling = 52w high $344.34"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13016.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
