---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $569.32 ahead of the 2026-08-17 print"
entry_price: 569.32
stop_price: 475.60
stop_logic: "chandelier trail: HH22 $590.76 - 3x ATR $38.39 = $475.60 — exit when decline exceeds ~3 average daily ranges"
target_price: 709.89
target_logic: "T1 $709.89 = entry $569.32 + 1.5x R (R=$93.72); T2 $850.47 = entry + 3x R; structure ceiling = 52w high $749.11"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $371.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($38.39)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
