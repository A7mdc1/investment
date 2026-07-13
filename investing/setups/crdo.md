---
ticker: CRDO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $238.39 ahead of the 2026-09-02 print"
entry_price: 238.39
stop_price: 224.34
stop_logic: "chandelier trail: HH22 $308.67 - 3x ATR $28.11 = $224.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 259.46
target_logic: "T1 $259.46 = entry $238.39 + 1.5x R (R=$14.05); T2 $280.53 = entry + 3x R; structure ceiling = 52w high $308.80"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2374.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($28.11)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
