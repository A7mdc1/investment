---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.02 ahead of the 2026-10-26 print"
entry_price: 56.02
stop_price: 49.17
stop_logic: "chandelier trail: HH22 $56.53 - 3x ATR $2.45 = $49.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 66.29
target_logic: "T1 $66.29 = entry $56.02 + 1.5x R (R=$6.85); T2 $76.56 = entry + 3x R; structure ceiling = 52w high $96.42"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $198.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.45)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
