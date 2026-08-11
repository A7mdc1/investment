---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $153.14 holding the uptrend (no breakdown on volume)"
entry_price: 153.14
stop_price: 149.88
stop_logic: "chandelier trail: HH22 $161.67 - 3x ATR $3.93 = $149.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 158.04
target_logic: "T1 $158.04 = entry $153.14 + 1.5x R (R=$3.27); T2 $162.94 = entry + 3x R; structure ceiling = 52w high $175.23"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2165.2M; pass"
invalidation: "loses EMA20 $153.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
