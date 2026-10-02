---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $279.96 ahead of the 2026-11-05 print"
entry_price: 279.96
stop_price: 248.19
stop_logic: "chandelier trail: HH22 $281.99 - 3x ATR $11.27 = $248.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 327.61
target_logic: "T1 $327.61 = entry $279.96 + 1.5x R (R=$31.77); T2 $375.26 = entry + 3x R; structure ceiling = 52w high $292.85"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $794.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.27)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
