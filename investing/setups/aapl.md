---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $337.70 ahead of the 2026-10-29 print"
entry_price: 337.70
stop_price: 320.60
stop_logic: "chandelier trail: HH22 $341.80 - 3x ATR $7.07 = $320.60 — exit when decline exceeds ~3 average daily ranges"
target_price: 363.35
target_logic: "T1 $363.35 = entry $337.70 + 1.5x R (R=$17.10); T2 $389.00 = entry + 3x R; structure ceiling = 52w high $344.24"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13644.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.07)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
