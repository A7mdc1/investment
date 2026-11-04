---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $100.37 ahead of the 2026-11-24 print"
entry_price: 100.37
stop_price: 90.52
stop_logic: "chandelier trail: HH22 $100.79 - 3x ATR $3.42 = $90.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 115.14
target_logic: "T1 $115.14 = entry $100.37 + 1.5x R (R=$9.85); T2 $129.91 = entry + 3x R; structure ceiling = 52w high $100.77"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $255.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.42)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
