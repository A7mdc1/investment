---
ticker: PENG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $47.36 ahead of the 2027-01-05 print"
entry_price: 47.36
stop_price: 47.11
stop_logic: "chandelier trail: HH22 $64.33 - 3x ATR $5.74 = $47.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 47.73
target_logic: "T1 $47.73 = entry $47.36 + 1.5x R (R=$0.25); T2 $48.10 = entry + 3x R; structure ceiling = 52w high $89.87"
holding_window_days: 21
catalyst: "2027-01-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $152.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.74)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
