---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $402.38 ahead of the 2026-11-02 print"
entry_price: 402.38
stop_price: 400.03
stop_logic: "chandelier trail: HH22 $453.94 - 3x ATR $17.97 = $400.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 405.90
target_logic: "T1 $405.90 = entry $402.38 + 1.5x R (R=$2.35); T2 $409.43 = entry + 3x R; structure ceiling = 52w high $749.31"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $314.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($17.97)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
