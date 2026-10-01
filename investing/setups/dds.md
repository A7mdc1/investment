---
ticker: DDS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $670.01 ahead of the 2026-11-12 print"
entry_price: 670.01
stop_price: 639.43
stop_logic: "chandelier trail: HH22 $702.30 - 3x ATR $20.96 = $639.43 — exit when decline exceeds ~3 average daily ranges"
target_price: 715.88
target_logic: "T1 $715.88 = entry $670.01 + 1.5x R (R=$30.58); T2 $761.76 = entry + 3x R; structure ceiling = 52w high $709.76"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $116.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($20.96)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
