---
ticker: ZS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $142.00 ahead of the 2026-09-02 print"
entry_price: 142.00
stop_price: 134.15
stop_logic: "chandelier trail: HH22 $155.36 - 3x ATR $7.07 = $134.15 — exit when decline exceeds ~3 average daily ranges"
target_price: 153.79
target_logic: "T1 $153.79 = entry $142.00 + 1.5x R (R=$7.86); T2 $165.57 = entry + 3x R; structure ceiling = 52w high $337.30"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $491.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.07)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
