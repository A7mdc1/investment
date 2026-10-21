---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $94.34 ahead of the 2026-11-24 print"
entry_price: 94.34
stop_price: 87.88
stop_logic: "chandelier trail: HH22 $96.53 - 3x ATR $2.88 = $87.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 104.03
target_logic: "T1 $104.03 = entry $94.34 + 1.5x R (R=$6.46); T2 $113.72 = entry + 3x R; structure ceiling = 52w high $96.56"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $247.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.88)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
