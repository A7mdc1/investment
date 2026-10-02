---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1139.64 ahead of the 2026-10-29 print"
entry_price: 1139.64
stop_price: 1126.73
stop_logic: "chandelier trail: HH22 $1215.00 - 3x ATR $29.42 = $1126.73 — exit when decline exceeds ~3 average daily ranges"
target_price: 1159.01
target_logic: "T1 $1159.01 = entry $1139.64 + 1.5x R (R=$12.91); T2 $1178.38 = entry + 3x R; structure ceiling = 52w high $1292.11"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2529.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.42)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
