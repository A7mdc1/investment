---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $411.78 ahead of the 2026-11-02 print"
entry_price: 411.78
stop_price: 400.51
stop_logic: "chandelier trail: HH22 $453.94 - 3x ATR $17.81 = $400.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 428.68
target_logic: "T1 $428.68 = entry $411.78 + 1.5x R (R=$11.27); T2 $445.58 = entry + 3x R; structure ceiling = 52w high $748.69"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $299.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($17.81)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
