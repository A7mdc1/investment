---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $417.39 ahead of the 2026-11-02 print"
entry_price: 417.39
stop_price: 399.54
stop_logic: "chandelier trail: HH22 $453.94 - 3x ATR $18.13 = $399.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 444.17
target_logic: "T1 $444.17 = entry $417.39 + 1.5x R (R=$17.85); T2 $470.94 = entry + 3x R; structure ceiling = 52w high $749.35"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $309.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($18.13)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
