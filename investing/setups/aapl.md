---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $336.64 ahead of the 2026-11-02 print"
entry_price: 336.64
stop_price: 325.41
stop_logic: "chandelier trail: HH22 $345.34 - 3x ATR $6.64 = $325.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 353.48
target_logic: "T1 $353.48 = entry $336.64 + 1.5x R (R=$11.23); T2 $370.32 = entry + 3x R; structure ceiling = 52w high $345.27"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $12667.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.64)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
