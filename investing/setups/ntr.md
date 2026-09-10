---
ticker: NTR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $79.61 ahead of the 2026-11-04 print"
entry_price: 79.61
stop_price: 76.37
stop_logic: "chandelier trail: HH22 $82.55 - 3x ATR $2.06 = $76.37 — exit when decline exceeds ~3 average daily ranges"
target_price: 84.48
target_logic: "T1 $84.48 = entry $79.61 + 1.5x R (R=$3.25); T2 $89.35 = entry + 3x R; structure ceiling = 52w high $83.98"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $190.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.06)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
