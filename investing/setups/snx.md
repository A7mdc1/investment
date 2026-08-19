---
ticker: SNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $252.66 ahead of the 2026-09-24 print"
entry_price: 252.66
stop_price: 242.02
stop_logic: "chandelier trail: HH22 $269.01 - 3x ATR $9.00 = $242.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 268.62
target_logic: "T1 $268.62 = entry $252.66 + 1.5x R (R=$10.64); T2 $284.58 = entry + 3x R; structure ceiling = 52w high $295.85"
holding_window_days: 21
catalyst: "2026-09-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $168.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($9.00)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
