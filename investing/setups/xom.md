---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $173.97 ahead of the 2026-10-30 print"
entry_price: 173.97
stop_price: 164.07
stop_logic: "chandelier trail: HH22 $174.89 - 3x ATR $3.61 = $164.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 188.82
target_logic: "T1 $188.82 = entry $173.97 + 1.5x R (R=$9.90); T2 $203.68 = entry + 3x R; structure ceiling = 52w high $174.84"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2063.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.61)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
