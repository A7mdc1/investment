---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $173.32 holding the uptrend (no breakdown on volume)"
entry_price: 173.32
stop_price: 167.31
stop_logic: "chandelier trail: HH22 $183.98 - 3x ATR $5.56 = $167.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 182.34
target_logic: "T1 $182.34 = entry $173.32 + 1.5x R (R=$6.01); T2 $191.36 = entry + 3x R; structure ceiling = 52w high $233.76"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $384.1M; pass"
invalidation: "loses EMA20 $173.32 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
