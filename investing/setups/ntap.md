---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $230.09 ahead of the 2026-12-01 print"
entry_price: 230.09
stop_price: 213.22
stop_logic: "chandelier trail: HH22 $240.87 - 3x ATR $9.22 = $213.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 255.40
target_logic: "T1 $255.40 = entry $230.09 + 1.5x R (R=$16.87); T2 $280.71 = entry + 3x R; structure ceiling = 52w high $240.93"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $536.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($9.22)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
