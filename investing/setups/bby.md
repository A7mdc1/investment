---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $97.50 ahead of the 2026-11-24 print"
entry_price: 97.50
stop_price: 89.01
stop_logic: "chandelier trail: HH22 $97.88 - 3x ATR $2.96 = $89.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 110.24
target_logic: "T1 $110.24 = entry $97.50 + 1.5x R (R=$8.49); T2 $122.98 = entry + 3x R; structure ceiling = 52w high $97.89"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $242.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.96)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
