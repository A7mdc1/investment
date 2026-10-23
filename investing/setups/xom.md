---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $182.29 ahead of the 2026-10-30 print"
entry_price: 182.29
stop_price: 172.85
stop_logic: "chandelier trail: HH22 $183.75 - 3x ATR $3.63 = $172.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 196.45
target_logic: "T1 $196.45 = entry $182.29 + 1.5x R (R=$9.44); T2 $210.61 = entry + 3x R; structure ceiling = 52w high $183.76"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1899.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.63)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
