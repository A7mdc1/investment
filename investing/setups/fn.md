---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $484.73 ahead of the 2026-11-02 print"
entry_price: 484.73
stop_price: 437.78
stop_logic: "chandelier trail: HH22 $500.00 - 3x ATR $20.74 = $437.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 555.15
target_logic: "T1 $555.15 = entry $484.73 + 1.5x R (R=$46.95); T2 $625.57 = entry + 3x R; structure ceiling = 52w high $749.20"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $337.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($20.74)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
