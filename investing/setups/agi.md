---
ticker: AGI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $29.58 ahead of the 2026-07-29 print"
entry_price: 29.58
stop_price: 28.60
stop_logic: "chandelier trail: HH22 $32.34 - 3x ATR $1.25 = $28.60 — exit when decline exceeds ~3 average daily ranges"
target_price: 31.05
target_logic: "T1 $31.05 = entry $29.58 + 1.5x R (R=$0.98); T2 $32.52 = entry + 3x R; structure ceiling = 52w high $55.29"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $121.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.25)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
