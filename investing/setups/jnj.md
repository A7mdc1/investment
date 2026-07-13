---
ticker: JNJ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $257.99 ahead of the 2026-07-15 print"
entry_price: 257.99
stop_price: 251.47
stop_logic: "chandelier trail: HH22 $269.43 - 3x ATR $5.99 = $251.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 267.77
target_logic: "T1 $267.77 = entry $257.99 + 1.5x R (R=$6.52); T2 $277.54 = entry + 3x R; structure ceiling = 52w high $269.30"
holding_window_days: 21
catalyst: "2026-07-15 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2147.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.99)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
