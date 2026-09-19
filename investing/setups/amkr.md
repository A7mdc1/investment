---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $50.30 ahead of the 2026-10-26 print"
entry_price: 50.30
stop_price: 47.57
stop_logic: "chandelier trail: HH22 $55.39 - 3x ATR $2.60 = $47.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 54.39
target_logic: "T1 $54.39 = entry $50.30 + 1.5x R (R=$2.73); T2 $58.48 = entry + 3x R; structure ceiling = 52w high $96.55"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $212.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.60)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
