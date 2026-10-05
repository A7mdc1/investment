---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $58.59 ahead of the 2026-11-04 print"
entry_price: 58.59
stop_price: 54.81
stop_logic: "chandelier trail: HH22 $58.66 - 3x ATR $1.28 = $54.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 64.26
target_logic: "T1 $64.26 = entry $58.59 + 1.5x R (R=$3.78); T2 $69.93 = entry + 3x R; structure ceiling = 52w high $64.60"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $62.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.28)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
