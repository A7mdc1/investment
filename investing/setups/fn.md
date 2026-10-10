---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $486.28 ahead of the 2026-11-02 print"
entry_price: 486.28
stop_price: 448.44
stop_logic: "chandelier trail: HH22 $515.00 - 3x ATR $22.19 = $448.44 — exit when decline exceeds ~3 average daily ranges"
target_price: 543.04
target_logic: "T1 $543.04 = entry $486.28 + 1.5x R (R=$37.84); T2 $599.81 = entry + 3x R; structure ceiling = 52w high $749.28"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $363.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($22.19)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
