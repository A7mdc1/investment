---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $402.89 ahead of the 2026-11-02 print"
entry_price: 402.89
stop_price: 400.21
stop_logic: "chandelier trail: HH22 $457.00 - 3x ATR $18.93 = $400.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 406.91
target_logic: "T1 $406.91 = entry $402.89 + 1.5x R (R=$2.68); T2 $410.93 = entry + 3x R; structure ceiling = 52w high $748.87"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $333.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($18.93)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
