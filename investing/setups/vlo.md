---
ticker: VLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $346.98 ahead of the 2026-10-22 print"
entry_price: 346.98
stop_price: 319.86
stop_logic: "chandelier trail: HH22 $353.00 - 3x ATR $11.05 = $319.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 387.65
target_logic: "T1 $387.65 = entry $346.98 + 1.5x R (R=$27.12); T2 $428.32 = entry + 3x R; structure ceiling = 52w high $352.98"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $792.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.05)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
