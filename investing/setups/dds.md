---
ticker: DDS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $645.51 ahead of the 2026-11-12 print"
entry_price: 645.51
stop_price: 626.56
stop_logic: "chandelier trail: HH22 $702.30 - 3x ATR $25.25 = $626.56 — exit when decline exceeds ~3 average daily ranges"
target_price: 673.93
target_logic: "T1 $673.93 = entry $645.51 + 1.5x R (R=$18.95); T2 $702.35 = entry + 3x R; structure ceiling = 52w high $710.13"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $124.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($25.25)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
