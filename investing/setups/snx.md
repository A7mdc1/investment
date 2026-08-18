---
ticker: SNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $257.74 ahead of the 2026-09-24 print"
entry_price: 257.74
stop_price: 244.05
stop_logic: "chandelier trail: HH22 $269.01 - 3x ATR $8.32 = $244.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 278.26
target_logic: "T1 $278.26 = entry $257.74 + 1.5x R (R=$13.69); T2 $298.79 = entry + 3x R; structure ceiling = 52w high $295.91"
holding_window_days: 21
catalyst: "2026-09-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $168.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
