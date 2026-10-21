---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $344.46 ahead of the 2026-11-02 print"
entry_price: 344.46
stop_price: 329.08
stop_logic: "chandelier trail: HH22 $348.15 - 3x ATR $6.36 = $329.08 — exit when decline exceeds ~3 average daily ranges"
target_price: 367.55
target_logic: "T1 $367.55 = entry $344.46 + 1.5x R (R=$15.39); T2 $390.63 = entry + 3x R; structure ceiling = 52w high $348.30"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $12151.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.36)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
