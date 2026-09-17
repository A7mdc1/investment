---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $17.52 ahead of the 2026-10-23 print"
entry_price: 17.52
stop_price: 16.55
stop_logic: "chandelier trail: HH22 $19.78 - 3x ATR $1.08 = $16.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 18.97
target_logic: "T1 $18.97 = entry $17.52 + 1.5x R (R=$0.97); T2 $20.43 = entry + 3x R; structure ceiling = 52w high $30.47"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $187.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.08)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
