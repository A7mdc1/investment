---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $17.50 ahead of the 2026-11-03 print"
entry_price: 17.50
stop_price: 17.44
stop_logic: "chandelier trail: HH22 $19.27 - 3x ATR $0.61 = $17.44 — exit when decline exceeds ~3 average daily ranges"
target_price: 17.59
target_logic: "T1 $17.59 = entry $17.50 + 1.5x R (R=$0.06); T2 $17.69 = entry + 3x R; structure ceiling = 52w high $19.73"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $24.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.61)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
