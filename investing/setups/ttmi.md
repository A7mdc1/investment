---
ticker: TTMI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $134.41 ahead of the 2026-08-05 print"
entry_price: 134.41
stop_price: 125.14
stop_logic: "chandelier trail: HH22 $161.01 - 3x ATR $11.96 = $125.14 — exit when decline exceeds ~3 average daily ranges"
target_price: 148.30
target_logic: "T1 $148.30 = entry $134.41 + 1.5x R (R=$9.26); T2 $162.20 = entry + 3x R; structure ceiling = 52w high $224.01"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $318.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.96)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
