---
ticker: AA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $51.33 ahead of the 2026-10-15 print"
entry_price: 51.33
stop_price: 49.13
stop_logic: "chandelier trail: HH22 $55.05 - 3x ATR $1.97 = $49.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 54.63
target_logic: "T1 $54.63 = entry $51.33 + 1.5x R (R=$2.20); T2 $57.92 = entry + 3x R; structure ceiling = 52w high $84.15"
holding_window_days: 21
catalyst: "2026-10-15 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $240.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.97)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
