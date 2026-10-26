---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.22 ahead of the 2026-10-27 print"
entry_price: 56.22
stop_price: 53.45
stop_logic: "chandelier trail: HH22 $58.19 - 3x ATR $1.58 = $53.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 60.36
target_logic: "T1 $60.36 = entry $56.22 + 1.5x R (R=$2.77); T2 $64.51 = entry + 3x R; structure ceiling = 52w high $69.92"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $314.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.58)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
