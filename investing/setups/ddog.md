---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $224.50 ahead of the 2026-11-05 print"
entry_price: 224.50
stop_price: 223.61
stop_logic: "chandelier trail: HH22 $262.99 - 3x ATR $13.13 = $223.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 225.83
target_logic: "T1 $225.83 = entry $224.50 + 1.5x R (R=$0.89); T2 $227.16 = entry + 3x R; structure ceiling = 52w high $292.70"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $906.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.13)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
