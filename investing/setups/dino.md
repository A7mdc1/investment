---
ticker: DINO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $82.25 ahead of the 2026-07-28 print"
entry_price: 82.25
stop_price: 76.21
stop_logic: "chandelier trail: HH22 $83.84 - 3x ATR $2.55 = $76.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 91.32
target_logic: "T1 $91.32 = entry $82.25 + 1.5x R (R=$6.04); T2 $100.38 = entry + 3x R; structure ceiling = 52w high $83.84"
holding_window_days: 21
catalyst: "2026-07-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $174.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.55)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
