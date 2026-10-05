---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $44.32 ahead of the 2026-11-04 print"
entry_price: 44.32
stop_price: 42.77
stop_logic: "chandelier trail: HH22 $47.44 - 3x ATR $1.56 = $42.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 46.64
target_logic: "T1 $46.64 = entry $44.32 + 1.5x R (R=$1.55); T2 $48.96 = entry + 3x R; structure ceiling = 52w high $47.45"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $267.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.56)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
