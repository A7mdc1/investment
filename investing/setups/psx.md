---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $196.62 ahead of the 2026-08-05 print"
entry_price: 196.62
stop_price: 179.69
stop_logic: "chandelier trail: HH22 $196.65 - 3x ATR $5.65 = $179.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 222.02
target_logic: "T1 $222.02 = entry $196.62 + 1.5x R (R=$16.93); T2 $247.42 = entry + 3x R; structure ceiling = 52w high $196.62"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $517.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.65)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
