---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $39.64 ahead of the 2026-11-12 print"
entry_price: 39.64
stop_price: 33.94
stop_logic: "chandelier trail: HH22 $41.10 - 3x ATR $2.38 = $33.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 48.18
target_logic: "T1 $48.18 = entry $39.64 + 1.5x R (R=$5.70); T2 $56.73 = entry + 3x R; structure ceiling = 52w high $70.53"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $55.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
