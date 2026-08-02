---
ticker: SNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $255.70 ahead of the 2026-09-24 print"
entry_price: 255.70
stop_price: 238.69
stop_logic: "chandelier trail: HH22 $266.80 - 3x ATR $9.37 = $238.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 281.21
target_logic: "T1 $281.21 = entry $255.70 + 1.5x R (R=$17.01); T2 $306.72 = entry + 3x R; structure ceiling = 52w high $295.95"
holding_window_days: 21
catalyst: "2026-09-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $201.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($9.37)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
