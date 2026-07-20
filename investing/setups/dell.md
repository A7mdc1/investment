---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $387.44 ahead of the 2026-09-03 print"
entry_price: 387.44
stop_price: 365.33
stop_logic: "chandelier trail: HH22 $463.48 - 3x ATR $32.72 = $365.33 — exit when decline exceeds ~3 average daily ranges"
target_price: 420.60
target_logic: "T1 $420.60 = entry $387.44 + 1.5x R (R=$22.11); T2 $453.76 = entry + 3x R; structure ceiling = 52w high $469.62"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3119.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.72)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
