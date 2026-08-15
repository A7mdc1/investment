---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $118.16 ahead of the 2026-08-26 print"
entry_price: 118.16
stop_price: 103.47
stop_logic: "chandelier trail: HH22 $118.81 - 3x ATR $5.11 = $103.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 140.19
target_logic: "T1 $140.19 = entry $118.16 + 1.5x R (R=$14.69); T2 $162.22 = entry + 3x R; structure ceiling = 52w high $118.75"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $253.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.11)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
