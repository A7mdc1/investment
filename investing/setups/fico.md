---
ticker: FICO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1286.51 ahead of the 2026-07-29 print"
entry_price: 1286.51
stop_price: 1134.67
stop_logic: "chandelier trail: HH22 $1295.57 - 3x ATR $53.63 = $1134.67 — exit when decline exceeds ~3 average daily ranges"
target_price: 1514.28
target_logic: "T1 $1514.28 = entry $1286.51 + 1.5x R (R=$151.84); T2 $1742.04 = entry + 3x R; structure ceiling = 52w high $1997.69"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $360.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($53.63)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
