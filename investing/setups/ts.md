---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.34 ahead of the 2026-11-04 print"
entry_price: 56.34
stop_price: 54.28
stop_logic: "chandelier trail: HH22 $58.16 - 3x ATR $1.29 = $54.28 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.41
target_logic: "T1 $59.41 = entry $56.34 + 1.5x R (R=$2.05); T2 $62.49 = entry + 3x R; structure ceiling = 52w high $64.60"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $61.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.29)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
