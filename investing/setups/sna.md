---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $367.25 ahead of the 2026-10-22 print"
entry_price: 367.25
stop_price: 361.91
stop_logic: "chandelier trail: HH22 $378.29 - 3x ATR $5.46 = $361.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 375.26
target_logic: "T1 $375.26 = entry $367.25 + 1.5x R (R=$5.34); T2 $383.27 = entry + 3x R; structure ceiling = 52w high $420.19"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $97.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.46)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
