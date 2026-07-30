---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $526.81 ahead of the 2026-08-05 print"
entry_price: 526.81
stop_price: 506.05
stop_logic: "chandelier trail: HH22 $663.98 - 3x ATR $52.64 = $506.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 557.93
target_logic: "T1 $557.93 = entry $526.81 + 1.5x R (R=$20.75); T2 $589.06 = entry + 3x R; structure ceiling = 52w high $799.40"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $3742.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($52.64)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
