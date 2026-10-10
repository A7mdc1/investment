---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $187.30 ahead of the 2026-11-23 print"
entry_price: 187.30
stop_price: 167.14
stop_logic: "chandelier trail: HH22 $201.99 - 3x ATR $11.62 = $167.14 — exit when decline exceeds ~3 average daily ranges"
target_price: 217.55
target_logic: "T1 $217.55 = entry $187.30 + 1.5x R (R=$20.16); T2 $247.79 = entry + 3x R; structure ceiling = 52w high $202.05"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $596.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.62)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
