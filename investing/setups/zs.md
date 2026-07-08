---
ticker: ZS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $143.05 ahead of the 2026-09-02 print"
entry_price: 143.05
stop_price: 134.50
stop_logic: "chandelier trail: HH22 $155.36 - 3x ATR $6.95 = $134.50 — exit when decline exceeds ~3 average daily ranges"
target_price: 155.88
target_logic: "T1 $155.88 = entry $143.05 + 1.5x R (R=$8.55); T2 $168.70 = entry + 3x R; structure ceiling = 52w high $337.38"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $503.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.95)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
