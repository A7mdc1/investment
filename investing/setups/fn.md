---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $525.77 ahead of the 2026-08-17 print"
entry_price: 525.77
stop_price: 469.75
stop_logic: "chandelier trail: HH22 $579.47 - 3x ATR $36.57 = $469.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 609.82
target_logic: "T1 $609.82 = entry $525.77 + 1.5x R (R=$56.03); T2 $693.86 = entry + 3x R; structure ceiling = 52w high $748.97"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $371.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($36.57)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
