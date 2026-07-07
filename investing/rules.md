---
# === TUNABLE KNOBS (verdict.py reads this block) ===
# Edit numbers here; the engine picks them up. These encode an evidence-based
# short-term / swing framework. They are YOUR policy, not advice from the tool.

# risk & sizing
risk_per_trade_pct: 1.5          # risk per trade (Van Tharp 1-2% rule)
max_position_pct: 22             # single-name weight cap -> TRIM above this
portfolio_heat_pct: 8            # max total open risk across positions
rebalance_band_pct: 20           # relative tolerance band (Daryanani 2008)
min_names_for_concentration: 4   # below this, ignore concentration (tiny book)

# exit / stop discipline
atr_period: 22                   # ATR + chandelier lookback
atr_stop_mult: 3.0               # chandelier multiplier (2 short swing .. 5 volatile)
ema_fast: 20                     # close < EMA_fast -> REVIEW (momentum fading)
ema_slow: 50
momentum_stop_bom_pct: 15        # Han/Zhou/Zhu beginning-of-month drop -> SELL (momentum trades)
drawdown_review_pct: 20          # down > this vs cost -> REVIEW thesis
take_profit_r: 1.5               # at +1.5R, TRIM partial + move stop to breakeven
pe_rich: 50                      # rich multiple -> HOLD, do not add
vol_throttle_atr_pct: 6          # daily ATR% above this -> de-risk note

# === SHORT-TERM RECOMMENDER (screener.py) scoring weights ===
# Weights need not sum to 1 (composite is normalised). Momentum dominates.
screen_weight_momentum: 0.40     # 3m + 6m momentum (skip last month)
screen_weight_trend: 0.25        # price vs EMA_fast / EMA_slow
screen_weight_rsi: 0.15          # prefer strong-but-not-overbought (~55-70)
screen_weight_volume: 0.10       # relative volume (interest)
screen_weight_lowvol: 0.10       # lower ATR% scores higher (risk-adjust)
screen_weight_compliance: 0.0    # 0 = informational only (you decide in your own tool)
screen_buy_candidate_score: 65   # composite >= this -> BUY-CANDIDATE, else RESEARCH
screen_min_price: 1.0            # below this -> AVOID (illiquid/penny)
compliance_gate: true            # holdings verdict gate; set false to disable hard SELL

# === TARGETS (targets.py): price target, scale-out sell plan, duration ===

target_method: r_multiple        # r_multiple | structure | atr (structure uses lower of struct vs R)
reward_risk: 3.0                 # swing default 3:1 (use 2.0 for shorter holds)
atr_target_mult: 4.0             # for target_method=atr: entry + k*ATR
target_atr_mult: 10.0            # cap technical_target_stop at price + N*ATR (crashed-stock sanity bound)
t1_r: 1.5                        # Target 1 at +1.5R -> take partial, stop to breakeven
t1_fraction: 0.5                 # fraction of position sold at T1
t2_r: 3.0                        # Target 2 at +3R -> trail remainder to here

# targeted holding duration + time-stop, by trade_type (calendar days)
## duration_days_swing: 21          # ~days-to-weeks
duration_days_momentum: 90       # weeks-to-few-months
duration_days_catalyst: 45       # ~20-60 trading-day PEAD drift window
duration_days_core: 365
time_stop_progress: 0.5          # if < this fraction of the way to T1 by duration -> time-stop

# === PM DECISION ENGINE (recommend.py / verdict.py — see PM_FRAMEWORK.md) ===
# recommend.py / discover.py use reward_risk_min / catalyst_horizon_days for new ideas.
# verdict.py uses reward_risk_compressed / dead_money_days for existing holdings.
reward_risk_min: 3.0              # min R:R for BUY-CANDIDATE — new ideas (recommend.py / discover.py)
reward_risk_min_swing: 2.0        # relaxed floor for short-horizon swing setups
catalyst_horizon_days: 60         # no catalyst inside this window -> cap at RESEARCH (recommend.py)
earnings_gap_assumption_pct: 25   # assumed adverse overnight gap for sizing through a print (recommend.py)

# === TRADE JOURNAL (apply_txn.py logs; journal.py reports) ===
journal_benchmark: SPUS           # same-day benchmark price logged per trade for the counterfactual
journal_min_trades: 20            # below this many closed trades -> "sample too small" note (never a limit)
reward_risk_compressed: 1.3       # current R:R below this on open holding -> TRIM (verdict.py)
dead_money_days: 60               # catalyst passed N days ago, no re-rating -> REVIEW (verdict.py)
edge_required_for_buy: true       # no variant view articulated -> cap at RESEARCH
review_cadence_days: 90           # re-underwrite at least this often even with no trigger

# === AUTO-DISCOVERY (discover.py) ===
# Each LOCAL run auto-builds a candidate pool, runs the PM pipeline, and rewrites
# watchlist.md with the top-N by "max benefit". Needs live Yahoo data (blocked in
# sandboxes). Shariah ratio FLAG = absolute AVOID; clean stays UNVERIFIED (you
# still confirm the business screen in Zoya/Musaffa). EDGE is never auto-supplied.
discover_top_n: 20                # how many leads to keep + write to leads.md
discover_etfs: [SPUS]             # halal-ETF holdings as the Shariah-friendlier base pool
discover_screens: [growth_technology_stocks, undervalued_large_caps]  # dropped most_actives (sourced degenerate names)
discover_screen_count: 100        # names to pull per yfinance predefined screen
screen_min_mcap: 500e6            # liquidity floor: drop leads under this market cap (untradeable "reward")
screen_min_avg_dollar_vol: 5e6    # liquidity floor: drop leads under this 20d avg $ volume
discover_w_rr: 0.5                # max-benefit rank weight: asymmetry (reward:risk) leads
discover_w_score: 0.3             # ...then the mechanical signal score (screener.py)
discover_w_catalyst: 0.2          # ...then catalyst proximity (closer earnings ranks higher)
discover_rr_cap: 10.0             # winsorize R:R before ranking (kills 600:1 stop-artifact outliers)
discover_rr_floor: 3.0            # BUY-CANDIDATE floor for zero-edge discovered ideas (stricter than swing)
# reward_risk() also floors downside at 0.5*ATR — you cannot risk less than the noise
---

# Decision rules — YOUR pre-committed policy

A senior PM does not "rate" stocks; they make capital-allocation decisions on four
pillars: a falsifiable THESIS, a VARIANT PERCEPTION (a view that differs from
consensus and is correct), an explicit REWARD:RISK skew, and a SIZE scaled to
conviction. Every label below is the output of those pillars, not a score.
Full reasoning and citations: `PM_FRAMEWORK.md`.

## Vocabulary (seven labels, two domains)
Existing holdings resolve to ONE of: **SELL > TRIM > REVIEW > HOLD** (precedence
in that order). New ideas (watchlist/universe) triage to: **BUY-CANDIDATE |
RESEARCH | AVOID**. Never blend the two domains — a holding doesn't get "AVOID"
and a new idea doesn't get "HOLD".

## Gate order (run in this sequence, for both holdings and new ideas)
1. **Shariah knockout** — screened non-compliant -> AVOID (new idea) / SELL
   (holding). Absolute; never a tiebreaker. Re-test each audited statement.
2. **Edge test** — if `edge_required_for_buy` and no variant view can be
   articulated (the specific reason the market has this wrong: informational /
   analytical / behavioral edge), the idea cannot exceed RESEARCH.
3. **Asymmetry gate** — reward:risk >= `min_reward_risk` (or `min_reward_risk_swing`
   for short-horizon setups) required for BUY-CANDIDATE. Downside must be a
   defined, engineered stop — not an assertion that something "looks cheap".
4. **Catalyst-within-horizon gate** — no hard or soft catalyst inside the holding
   window -> at most RESEARCH for new ideas; "dead money" for an existing holding
   with no catalyst within `dead_money_days` -> REVIEW or TRIM (opportunity cost
   of capital tied up in a non-performing, thesis-intact position).
5. **Sizing** — from conviction x the 1%-style risk rule (`risk_per_trade_pct`)
   and the hard `max_position_pct` cap. Never let one position or one correlated
   cluster dominate the book.

The Shariah knockout is the only HARD gate; the others are pre-committed policy,
not divine instruction — but break them only on a written reason, not in the moment.

## Stage 1 — Compliance gate (runs first, binary)
- COMPLIANCE_GATE | screened non-compliant | SELL (exit; cure/purify per Zoya/Musaffa)
- COMPLIANCE_SCREEN | status unknown/doubtful or screen > 1 quarter old | REVIEW before any add
- Hard-excluded instruments (NEVER): short selling, options, futures, CFDs, margin/leverage.
- Min holding >= T+2 settlement (qabd); no intraday flips.

## Stage 2 — Entry (BUY) — requires 2+ confirmations, plus the gates above
- 6-12m momentum, top of universe, skipping last month (Jegadeesh & Titman 1993)
- breakout above resistance WITH volume confirmation
- pullback to EMA_fast in an uptrend (no tight stop here — Kaminski & Lo 2014)
- positive earnings-surprise drift / defined catalyst (PEAD; Bernard & Thomas 1989)
- A variant view (why the market is wrong) and reward:risk >= min_reward_risk are
  required before BUY-CANDIDATE, not just a technical confirmation (edge + asymmetry gates).
Size = risk_per_trade_pct / stop-distance, capped at max_position_pct & portfolio_heat_pct.

`recommend.py` (new-idea funnel: screen -> RESEARCH -> BUY-CANDIDATE / AVOID)
adds two gates ahead of sizing, run in this order:
- EDGE_GATE | no stated reason the market is wrong (no thesis/"why" supplied) |
  capped at RESEARCH — a mechanical score alone is not an edge.
- ASYMMETRY_GATE | upside:downside < reward_risk_min (or reward_risk_min_swing
  for swing setups) | capped at RESEARCH; AVOID if there's no defined downside at all.
- CATALYST_GATE | no catalyst within catalyst_horizon_days | capped at RESEARCH
  ("dead money" — see Stage 4 TIME_STOP for existing holdings).

## Stage 3 — Manage (HOLD / TRIM)
- HOLD while price > trailing stop AND thesis intact AND you'd buy it here today
  (the active "would I buy this at today's price?" test — not inertia).
- TAKE_PARTIAL | reached take_profit_r and not yet trimmed | TRIM ~1/3-1/2, stop -> breakeven
- REWARD_RISK_COMPRESSED | current R:R < reward_risk_compressed (gap to target has closed) | TRIM
- CONCENTRATION | weight > max_position_pct | TRIM toward target
- VALUATION_RICH | P/E >= pe_rich | HOLD, do not add
- DEAD_MONEY | thesis intact but no catalyst within dead_money_days | REVIEW or TRIM
  (capital tied up with no near-term path to close the price/value gap is itself a cost)
- REBALANCE only when a position breaches its relative tolerance band.

## Stage 4 — SELL triggers (any one fires)
- HARD_STOP | price < initial_stop (front-matter) | SELL
- TRAIL_STOP | price < chandelier = HighestHigh(atr_period) - atr_stop_mult*ATR | SELL
- MOMENTUM_STOP | momentum trade down >= momentum_stop_bom_pct from month-open | SELL (Han/Zhou/Zhu)
- EMA_BREAK | swing trade closes < EMA_fast | REVIEW (early), < EMA_slow | SELL
- THESIS_BREAK | front-matter thesis_broken: true, OR invalidation trigger (front-matter
  `invalidation`) has occurred | SELL — the *why* is now false, not just the price
- TARGET_REACHED | price >= target_price and edge/variant view has closed | SELL
  (value realized; don't anchor to a high-water mark and ride it back down)
- TIME_STOP | catalyst window elapsed with no move | REVIEW

## Discipline guards (counteract behavioral leaks)
- No averaging down on a broken thesis (disposition effect; Odean 1998).
- Stops/targets defined in ATR/technical terms, not entry price (anti-anchoring).
- Don't sell *just* because price moved — sell on thesis break, target reached, or
  a better-skewed opportunity needing the capital (Marks, "Selling Out").
- Pre-mortem at entry: before opening, write the top 2-3 reasons this trade fails
  (front-matter `pre_mortem`). Imagining the failure first surfaces risks emotion
  later hides (Klein 2007, "prospective hindsight").
- Re-underwrite (re-run the full thesis test) at least every review_cadence_days,
  on every earnings print, and on every catalyst date — don't wait for a SELL
  trigger to revisit conviction.
- If net-of-cost performance trails a Shariah benchmark over ~50 trades / 12 mo,
  cut turnover and lengthen holds toward buy-and-hold (Barber & Odean 2000).
- Process over outcome: judge the engine's reasoning quality, not any single
  trade's P&L (Mauboussin). A good process can still lose; a bad one can still win.
- Be honest about the base rate: most retail short-term traders lose money net of
  costs (Chague, De-Losso & Giovannetti 2019). This process improves decision
  quality; it does not repeal that.

# Notes
# - The engine never auto-trades. After you execute, run /apply-trade.
# - Confirm Shariah thresholds with a qualified Saudi authority — informational, not a fatwa.
