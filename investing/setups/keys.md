---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $339.45 ahead of the 2026-08-18 print"
entry_price: 339.45
stop_price: 304.47
stop_logic: "chandelier trail: HH22 $343.87 - 3x ATR $13.13 = $304.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 391.92
target_logic: "T1 $391.92 = entry $339.45 + 1.5x R (R=$34.98); T2 $444.39 = entry + 3x R; structure ceiling = 52w high $375.08"
holding_window_days: 21
catalyst: "2026-08-18 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $378.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.13)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
