---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $386.04 ahead of the 2026-09-03 print"
entry_price: 386.04
stop_price: 380.08
stop_logic: "chandelier trail: HH22 $466.66 - 3x ATR $28.86 = $380.08 — exit when decline exceeds ~3 average daily ranges"
target_price: 394.98
target_logic: "T1 $394.98 = entry $386.04 + 1.5x R (R=$5.96); T2 $403.91 = entry + 3x R; structure ceiling = 52w high $637.03"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $773.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($28.86)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
