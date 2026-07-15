---
ticker: PDFS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $51.81 ahead of the 2026-08-06 print"
entry_price: 51.81
stop_price: 57.92
stop_logic: "chandelier trail: HH22 $71.69 - 3x ATR $4.59 = $57.92 — exit when decline exceeds ~3 average daily ranges"
target_price: null
target_logic: null           # scaffold: target unavailable (needs entry>stop for R)
holding_window_days: 21
catalyst: "2026-08-06 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $45.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.59)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
