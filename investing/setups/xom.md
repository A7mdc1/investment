---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $176.90 ahead of the 2026-10-30 print"
entry_price: 176.90
stop_price: 166.82
stop_logic: "chandelier trail: HH22 $177.36 - 3x ATR $3.51 = $166.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 192.02
target_logic: "T1 $192.02 = entry $176.90 + 1.5x R (R=$10.08); T2 $207.13 = entry + 3x R; structure ceiling = 52w high $177.43"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2064.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.51)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
