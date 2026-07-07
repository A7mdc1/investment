---
ticker: KLIC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $119.61 ahead of the 2026-08-06 print"
entry_price: 119.61
stop_price: 108.81
stop_logic: "chandelier trail: HH22 $135.80 - 3x ATR $9.00 = $108.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 135.81
target_logic: "T1 $135.81 = entry $119.61 + 1.5x R (R=$10.80); T2 $152.01 = entry + 3x R; structure ceiling = 52w high $135.77"
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $164.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($9.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
