---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $96.25 ahead of the 2026-11-24 print"
entry_price: 96.25
stop_price: 91.11
stop_logic: "chandelier trail: HH22 $100.58 - 3x ATR $3.16 = $91.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 103.97
target_logic: "T1 $103.97 = entry $96.25 + 1.5x R (R=$5.14); T2 $111.68 = entry + 3x R; structure ceiling = 52w high $100.57"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $259.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.16)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
