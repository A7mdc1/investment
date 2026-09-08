---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $158.81 ahead of the 2026-10-30 print"
entry_price: 158.81
stop_price: 158.43
stop_logic: "chandelier trail: HH22 $168.64 - 3x ATR $3.40 = $158.43 — exit when decline exceeds ~3 average daily ranges"
target_price: 159.40
target_logic: "T1 $159.40 = entry $158.81 + 1.5x R (R=$0.39); T2 $159.98 = entry + 3x R; structure ceiling = 52w high $174.14"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2146.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.40)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
