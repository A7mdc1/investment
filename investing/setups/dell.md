---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $403.98 ahead of the 2026-09-03 print"
entry_price: 403.98
stop_price: 365.88
stop_logic: "chandelier trail: HH22 $463.48 - 3x ATR $32.53 = $365.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 461.14
target_logic: "T1 $461.14 = entry $403.98 + 1.5x R (R=$38.10); T2 $518.29 = entry + 3x R; structure ceiling = 52w high $469.20"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3327.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.53)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
