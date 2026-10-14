---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $343.51 ahead of the 2026-11-02 print"
entry_price: 343.51
stop_price: 329.08
stop_logic: "chandelier trail: HH22 $348.15 - 3x ATR $6.36 = $329.08 — exit when decline exceeds ~3 average daily ranges"
target_price: 365.15
target_logic: "T1 $365.15 = entry $343.51 + 1.5x R (R=$14.43); T2 $386.80 = entry + 3x R; structure ceiling = 52w high $348.03"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $12384.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.36)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
