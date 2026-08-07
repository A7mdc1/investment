---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $424.99 ahead of the 2026-09-02 print"
entry_price: 424.99
stop_price: 383.10
stop_logic: "chandelier trail: HH22 $430.82 - 3x ATR $15.91 = $383.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 487.82
target_logic: "T1 $487.82 = entry $424.99 + 1.5x R (R=$41.89); T2 $550.65 = entry + 3x R; structure ceiling = 52w high $494.17"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $7264.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.91)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
