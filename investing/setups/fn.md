---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $455.14 ahead of the 2026-11-02 print"
entry_price: 455.14
stop_price: 410.49
stop_logic: "chandelier trail: HH22 $468.00 - 3x ATR $19.17 = $410.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 522.12
target_logic: "T1 $522.12 = entry $455.14 + 1.5x R (R=$44.65); T2 $589.09 = entry + 3x R; structure ceiling = 52w high $748.59"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $300.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($19.17)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
