---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $175.34 ahead of the 2026-09-03 print"
entry_price: 175.34
stop_price: 151.87
stop_logic: "chandelier trail: HH22 $178.07 - 3x ATR $8.73 = $151.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 210.55
target_logic: "T1 $210.55 = entry $175.34 + 1.5x R (R=$23.47); T2 $245.76 = entry + 3x R; structure ceiling = 52w high $272.69"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $188.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.73)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
