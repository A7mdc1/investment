---
ticker: DDS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $656.38 ahead of the 2026-11-12 print"
entry_price: 656.38
stop_price: 599.25
stop_logic: "chandelier trail: HH22 $665.25 - 3x ATR $22.00 = $599.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 742.07
target_logic: "T1 $742.07 = entry $656.38 + 1.5x R (R=$57.13); T2 $827.76 = entry + 3x R; structure ceiling = 52w high $710.37"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $115.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($22.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
