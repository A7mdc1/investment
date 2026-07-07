---
ticker: PLTR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $132.54 ahead of the 2026-08-03 print"
entry_price: 132.54
stop_price: 131.84
stop_logic: "chandelier trail: HH22 $151.68 - 3x ATR $6.61 = $131.84 — exit when decline exceeds ~3 average daily ranges"
target_price: 133.59
target_logic: "T1 $133.59 = entry $132.54 + 1.5x R (R=$0.70); T2 $134.64 = entry + 3x R; structure ceiling = 52w high $207.42"
holding_window_days: 21
catalyst: "2026-08-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $5387.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.61)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
