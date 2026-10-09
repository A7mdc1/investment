---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $491.60 ahead of the 2026-11-02 print"
entry_price: 491.60
stop_price: 448.44
stop_logic: "chandelier trail: HH22 $515.00 - 3x ATR $22.19 = $448.44 — exit when decline exceeds ~3 average daily ranges"
target_price: 556.34
target_logic: "T1 $556.34 = entry $491.60 + 1.5x R (R=$43.16); T2 $621.09 = entry + 3x R; structure ceiling = 52w high $749.39"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $356.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($22.19)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
