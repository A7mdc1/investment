---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $52.84 ahead of the 2026-10-26 print"
entry_price: 52.84
stop_price: 47.27
stop_logic: "chandelier trail: HH22 $54.89 - 3x ATR $2.54 = $47.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 61.20
target_logic: "T1 $61.20 = entry $52.84 + 1.5x R (R=$5.57); T2 $69.55 = entry + 3x R; structure ceiling = 52w high $96.42"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $189.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.54)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
