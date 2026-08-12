---
ticker: DDS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $641.67 ahead of the 2026-08-13 print"
entry_price: 641.67
stop_price: 584.54
stop_logic: "chandelier trail: HH22 $651.86 - 3x ATR $22.44 = $584.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 727.37
target_logic: "T1 $727.37 = entry $641.67 + 1.5x R (R=$57.13); T2 $813.07 = entry + 3x R; structure ceiling = 52w high $710.60"
holding_window_days: 21
catalyst: "2026-08-13 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $79.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($22.44)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
