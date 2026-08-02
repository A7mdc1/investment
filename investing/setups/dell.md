---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $405.37 ahead of the 2026-09-03 print"
entry_price: 405.37
stop_price: 360.62
stop_logic: "chandelier trail: HH22 $462.72 - 3x ATR $34.03 = $360.62 — exit when decline exceeds ~3 average daily ranges"
target_price: 472.50
target_logic: "T1 $472.50 = entry $405.37 + 1.5x R (R=$44.75); T2 $539.62 = entry + 3x R; structure ceiling = 52w high $468.64"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2798.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($34.03)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
