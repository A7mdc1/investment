---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1372.68 holding the uptrend (no breakdown on volume)"
entry_price: 1372.68
stop_price: 1332.32
stop_logic: "chandelier trail: HH22 $1475.25 - 3x ATR $47.64 = $1332.32 — exit when decline exceeds ~3 average daily ranges"
target_price: 1433.22
target_logic: "T1 $1433.22 = entry $1372.68 + 1.5x R (R=$40.36); T2 $1493.76 = entry + 3x R; structure ceiling = 52w high $1475.66"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4130.8M; pass"
invalidation: "loses EMA20 $1372.68 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
