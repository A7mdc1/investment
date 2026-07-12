---
ticker: ZS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $139.27 ahead of the 2026-09-02 print"
entry_price: 139.27
stop_price: 133.57
stop_logic: "chandelier trail: HH22 $155.36 - 3x ATR $7.26 = $133.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 147.82
target_logic: "T1 $147.82 = entry $139.27 + 1.5x R (R=$5.70); T2 $156.36 = entry + 3x R; structure ceiling = 52w high $337.22"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $509.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.26)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
