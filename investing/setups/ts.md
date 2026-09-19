---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.25 ahead of the 2026-11-04 print"
entry_price: 56.25
stop_price: 54.19
stop_logic: "chandelier trail: HH22 $58.16 - 3x ATR $1.32 = $54.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.35
target_logic: "T1 $59.35 = entry $56.25 + 1.5x R (R=$2.06); T2 $62.44 = entry + 3x R; structure ceiling = 52w high $64.58"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $63.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
