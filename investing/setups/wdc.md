---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $566.43 ahead of the 2026-08-05 print"
entry_price: 566.43
stop_price: 561.04
stop_logic: "chandelier trail: HH22 $729.00 - 3x ATR $55.99 = $561.04 — exit when decline exceeds ~3 average daily ranges"
target_price: 574.52
target_logic: "T1 $574.52 = entry $566.43 + 1.5x R (R=$5.39); T2 $582.60 = entry + 3x R; structure ceiling = 52w high $800.04"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $4788.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($55.99)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
