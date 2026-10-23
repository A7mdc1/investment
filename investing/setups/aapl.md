---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $346.30 ahead of the 2026-11-02 print"
entry_price: 346.30
stop_price: 332.82
stop_logic: "chandelier trail: HH22 $351.73 - 3x ATR $6.30 = $332.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 366.52
target_logic: "T1 $366.52 = entry $346.30 + 1.5x R (R=$13.48); T2 $386.74 = entry + 3x R; structure ceiling = 52w high $351.57"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $12759.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.30)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
