---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $70.99 ahead of the 2026-10-22 print"
entry_price: 70.99
stop_price: 64.33
stop_logic: "chandelier trail: HH22 $71.34 - 3x ATR $2.34 = $64.33 — exit when decline exceeds ~3 average daily ranges"
target_price: 80.98
target_logic: "T1 $80.98 = entry $70.99 + 1.5x R (R=$6.66); T2 $90.98 = entry + 3x R; structure ceiling = 52w high $71.35"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $193.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.34)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
