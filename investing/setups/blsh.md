---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $38.01 ahead of the 2026-11-12 print"
entry_price: 38.01
stop_price: 32.10
stop_logic: "chandelier trail: HH22 $39.55 - 3x ATR $2.49 = $32.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 46.88
target_logic: "T1 $46.88 = entry $38.01 + 1.5x R (R=$5.91); T2 $55.75 = entry + 3x R; structure ceiling = 52w high $74.97"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $53.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.49)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
