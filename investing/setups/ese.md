---
ticker: ESE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $323.67 ahead of the 2026-08-10 print"
entry_price: 323.67
stop_price: 322.73
stop_logic: "chandelier trail: HH22 $362.06 - 3x ATR $13.11 = $322.73 — exit when decline exceeds ~3 average daily ranges"
target_price: 325.06
target_logic: "T1 $325.06 = entry $323.67 + 1.5x R (R=$0.93); T2 $326.46 = entry + 3x R; structure ceiling = 52w high $362.04"
holding_window_days: 21
catalyst: "2026-08-10 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $104.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.11)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
