---
ticker: SNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $258.28 ahead of the 2026-09-24 print"
entry_price: 258.28
stop_price: 243.36
stop_logic: "chandelier trail: HH22 $269.01 - 3x ATR $8.55 = $243.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 280.66
target_logic: "T1 $280.66 = entry $258.28 + 1.5x R (R=$14.92); T2 $303.03 = entry + 3x R; structure ceiling = 52w high $295.85"
holding_window_days: 21
catalyst: "2026-09-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $159.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.55)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
