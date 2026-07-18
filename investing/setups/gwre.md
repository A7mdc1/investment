---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $150.02 ahead of the 2026-09-03 print"
entry_price: 150.02
stop_price: 131.32
stop_logic: "chandelier trail: HH22 $152.19 - 3x ATR $6.96 = $131.32 — exit when decline exceeds ~3 average daily ranges"
target_price: 178.07
target_logic: "T1 $178.07 = entry $150.02 + 1.5x R (R=$18.70); T2 $206.11 = entry + 3x R; structure ceiling = 52w high $272.76"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $232.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.96)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
