---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $412.49 ahead of the 2026-11-02 print"
entry_price: 412.49
stop_price: 374.64
stop_logic: "chandelier trail: HH22 $428.50 - 3x ATR $17.95 = $374.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 469.25
target_logic: "T1 $469.25 = entry $412.49 + 1.5x R (R=$37.85); T2 $526.02 = entry + 3x R; structure ceiling = 52w high $748.61"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $295.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($17.95)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
