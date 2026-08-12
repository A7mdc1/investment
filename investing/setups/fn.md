---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $583.18 ahead of the 2026-08-17 print"
entry_price: 583.18
stop_price: 470.51
stop_logic: "chandelier trail: HH22 $585.45 - 3x ATR $38.31 = $470.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 752.18
target_logic: "T1 $752.18 = entry $583.18 + 1.5x R (R=$112.67); T2 $921.18 = entry + 3x R; structure ceiling = 52w high $748.63"
holding_window_days: 21
catalyst: "2026-08-17 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $373.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($38.31)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
