---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $17.58 ahead of the 2026-11-03 print"
entry_price: 17.58
stop_price: 17.49
stop_logic: "chandelier trail: HH22 $19.27 - 3x ATR $0.59 = $17.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 17.71
target_logic: "T1 $17.71 = entry $17.58 + 1.5x R (R=$0.09); T2 $17.84 = entry + 3x R; structure ceiling = 52w high $19.73"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $25.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.59)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
