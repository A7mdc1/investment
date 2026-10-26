---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $282.05 ahead of the 2026-11-04 print"
entry_price: 282.05
stop_price: 257.85
stop_logic: "chandelier trail: HH22 $300.68 - 3x ATR $14.28 = $257.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 318.36
target_logic: "T1 $318.36 = entry $282.05 + 1.5x R (R=$24.21); T2 $354.67 = entry + 3x R; structure ceiling = 52w high $300.70"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $713.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($14.28)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
