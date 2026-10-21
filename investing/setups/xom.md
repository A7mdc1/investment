---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $177.41 ahead of the 2026-10-30 print"
entry_price: 177.41
stop_price: 170.01
stop_logic: "chandelier trail: HH22 $180.26 - 3x ATR $3.42 = $170.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 188.50
target_logic: "T1 $188.50 = entry $177.41 + 1.5x R (R=$7.40); T2 $199.60 = entry + 3x R; structure ceiling = 52w high $180.29"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1872.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.42)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
