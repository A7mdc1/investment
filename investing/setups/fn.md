---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $590.86 ahead of the 2026-08-17 print"
entry_price: 590.86
stop_price: 482.98
stop_logic: "chandelier trail: HH22 $597.87 - 3x ATR $38.30 = $482.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 752.68
target_logic: "T1 $752.68 = entry $590.86 + 1.5x R (R=$107.88); T2 $914.49 = entry + 3x R; structure ceiling = 52w high $748.87"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $368.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($38.30)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
