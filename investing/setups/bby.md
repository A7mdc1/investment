---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $90.77 ahead of the 2026-08-27 print"
entry_price: 90.77
stop_price: 83.42
stop_logic: "chandelier trail: HH22 $90.99 - 3x ATR $2.52 = $83.42 — exit when decline exceeds ~3 average daily ranges"
target_price: 101.79
target_logic: "T1 $101.79 = entry $90.77 + 1.5x R (R=$7.35); T2 $112.81 = entry + 3x R; structure ceiling = 52w high $90.95"
holding_window_days: 21
catalyst: "2026-08-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $272.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.52)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
