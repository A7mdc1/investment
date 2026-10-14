---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $359.88 ahead of the 2026-11-24 print"
entry_price: 359.88
stop_price: 358.65
stop_logic: "chandelier trail: HH22 $389.93 - 3x ATR $10.43 = $358.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 361.74
target_logic: "T1 $361.74 = entry $359.88 + 1.5x R (R=$1.23); T2 $363.59 = entry + 3x R; structure ceiling = 52w high $389.91"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $404.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($10.43)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
