---
ticker: FRO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $53.65 ahead of the 2026-11-30 print"
entry_price: 53.65
stop_price: 49.19
stop_logic: "chandelier trail: HH22 $54.69 - 3x ATR $1.83 = $49.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 60.34
target_logic: "T1 $60.34 = entry $53.65 + 1.5x R (R=$4.46); T2 $67.03 = entry + 3x R; structure ceiling = 52w high $54.69"
holding_window_days: 21
catalyst: "2026-11-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $209.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.83)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
