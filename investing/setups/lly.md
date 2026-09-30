---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1187.19 ahead of the 2026-10-29 print"
entry_price: 1187.19
stop_price: 1127.49
stop_logic: "chandelier trail: HH22 $1214.99 - 3x ATR $29.16 = $1127.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 1276.74
target_logic: "T1 $1276.74 = entry $1187.19 + 1.5x R (R=$59.70); T2 $1366.29 = entry + 3x R; structure ceiling = 52w high $1293.24"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2532.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.16)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
