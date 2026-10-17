---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $178.98 ahead of the 2026-10-30 print"
entry_price: 178.98
stop_price: 168.86
stop_logic: "chandelier trail: HH22 $179.16 - 3x ATR $3.43 = $168.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 194.17
target_logic: "T1 $194.17 = entry $178.98 + 1.5x R (R=$10.12); T2 $209.35 = entry + 3x R; structure ceiling = 52w high $179.16"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1950.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.43)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
