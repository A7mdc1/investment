---
ticker: SIMO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $318.86 ahead of the 2026-07-30 print"
entry_price: 318.86
stop_price: 273.25
stop_logic: "chandelier trail: HH22 $355.00 - 3x ATR $27.25 = $273.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 387.27
target_logic: "T1 $387.27 = entry $318.86 + 1.5x R (R=$45.61); T2 $455.68 = entry + 3x R; structure ceiling = 52w high $355.08"
holding_window_days: 21
catalyst: "2026-07-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $271.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($27.25)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
