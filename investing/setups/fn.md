---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $463.69 ahead of the 2026-11-02 print"
entry_price: 463.69
stop_price: 410.84
stop_logic: "chandelier trail: HH22 $467.37 - 3x ATR $18.84 = $410.84 — exit when decline exceeds ~3 average daily ranges"
target_price: 542.96
target_logic: "T1 $542.96 = entry $463.69 + 1.5x R (R=$52.85); T2 $622.23 = entry + 3x R; structure ceiling = 52w high $749.10"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $306.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($18.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
