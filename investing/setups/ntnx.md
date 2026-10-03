---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $72.29 ahead of the 2026-11-25 print"
entry_price: 72.29
stop_price: 67.17
stop_logic: "chandelier trail: HH22 $72.75 - 3x ATR $1.86 = $67.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 79.96
target_logic: "T1 $79.96 = entry $72.29 + 1.5x R (R=$5.12); T2 $87.64 = entry + 3x R; structure ceiling = 52w high $77.90"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $162.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.86)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
