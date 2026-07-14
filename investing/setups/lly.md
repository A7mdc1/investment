---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1153.67 ahead of the 2026-08-05 print"
entry_price: 1153.67
stop_price: 1134.95
stop_logic: "chandelier trail: HH22 $1249.45 - 3x ATR $38.17 = $1134.95 — exit when decline exceeds ~3 average daily ranges"
target_price: 1181.76
target_logic: "T1 $1181.76 = entry $1153.67 + 1.5x R (R=$18.72); T2 $1209.84 = entry + 3x R; structure ceiling = 52w high $1249.91"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3550.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($38.17)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
