---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $55.91 ahead of the 2026-10-26 print"
entry_price: 55.91
stop_price: 48.97
stop_logic: "chandelier trail: HH22 $56.29 - 3x ATR $2.44 = $48.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 66.31
target_logic: "T1 $66.31 = entry $55.91 + 1.5x R (R=$6.94); T2 $76.72 = entry + 3x R; structure ceiling = 52w high $96.55"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $192.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.44)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
