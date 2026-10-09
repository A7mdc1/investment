---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $291.10 ahead of the 2026-11-05 print"
entry_price: 291.10
stop_price: 258.23
stop_logic: "chandelier trail: HH22 $291.49 - 3x ATR $11.09 = $258.23 — exit when decline exceeds ~3 average daily ranges"
target_price: 340.39
target_logic: "T1 $340.39 = entry $291.10 + 1.5x R (R=$32.86); T2 $389.69 = entry + 3x R; structure ceiling = 52w high $292.85"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $763.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.09)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
