---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $46.93 ahead of the 2026-11-04 print"
entry_price: 46.93
stop_price: 42.72
stop_logic: "chandelier trail: HH22 $47.28 - 3x ATR $1.52 = $42.72 — exit when decline exceeds ~3 average daily ranges"
target_price: 53.25
target_logic: "T1 $53.25 = entry $46.93 + 1.5x R (R=$4.21); T2 $59.57 = entry + 3x R; structure ceiling = 52w high $47.26"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $222.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.52)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
