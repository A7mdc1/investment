---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $398.61 ahead of the 2026-09-03 print"
entry_price: 398.61
stop_price: 369.55
stop_logic: "chandelier trail: HH22 $462.69 - 3x ATR $31.05 = $369.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 442.20
target_logic: "T1 $442.20 = entry $398.61 + 1.5x R (R=$29.06); T2 $485.79 = entry + 3x R; structure ceiling = 52w high $637.78"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $855.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($31.05)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
