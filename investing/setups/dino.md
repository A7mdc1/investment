---
ticker: DINO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $89.73 ahead of the 2026-07-28 print"
entry_price: 89.73
stop_price: 85.34
stop_logic: "chandelier trail: HH22 $93.66 - 3x ATR $2.77 = $85.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 96.31
target_logic: "T1 $96.31 = entry $89.73 + 1.5x R (R=$4.39); T2 $102.89 = entry + 3x R; structure ceiling = 52w high $93.66"
holding_window_days: 21
catalyst: "2026-07-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $207.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.77)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
