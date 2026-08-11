---
ticker: SNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $255.60 ahead of the 2026-09-24 print"
entry_price: 255.60
stop_price: 242.91
stop_logic: "chandelier trail: HH22 $269.01 - 3x ATR $8.70 = $242.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 274.63
target_logic: "T1 $274.63 = entry $255.60 + 1.5x R (R=$12.69); T2 $293.67 = entry + 3x R; structure ceiling = 52w high $295.83"
holding_window_days: 21
catalyst: "2026-09-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $170.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.70)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
