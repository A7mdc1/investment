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

# === PM-GRADE RECOMMENDATION ENGINE (recommend.py) ===
# Encodes the edge/asymmetry/catalyst gates from the PM decision-logic note
# (docs/Portfolio_Manager_Decision_Logic...md). The engine cannot supply a
# real analytical edge or conviction call — only you can. These knobs just
# set the mechanical floor it enforces before it will say BUY-CANDIDATE.
reward_risk_min: 3.0              # min upside:downside for BUY-CANDIDATE (institutional norm)
reward_risk_min_swing: 2.0        # relaxed floor for short-horizon swing setups
catalyst_horizon_days: 60         # no catalyst inside this window -> cap at RESEARCH
---

# Decision rules — YOUR pre-committed short-term policy

The engine resolves every holding to ONE verb (SELL > TRIM > REVIEW > HOLD) from
the rules below. Short-term focus: days-to-months, long-only, cash-funded.
Evidence sources in parentheses; full report in the research artifact.

## Stage 1 — Compliance gate (runs first, binary)
- COMPLIANCE_GATE | screened non-compliant | SELL (exit; cure/purify per Zoya/Musaffa)
- COMPLIANCE_SCREEN | status unknown/doubtful or screen > 1 quarter old | REVIEW before any add
- Hard-excluded instruments (NEVER): short selling, options, futures, CFDs, margin/leverage.
- Min holding >= T+2 settlement (qabd); no intraday flips.

## Stage 2 — Entry (BUY) — requires 2+ confirmations
- 6-12m momentum, top of universe, skipping last month (Jegadeesh & Titman 1993)
- breakout above resistance WITH volume confirmation
- pullback to EMA_fast in an uptrend (no tight stop here — Kaminski & Lo 2014)
- positive earnings-surprise drift / defined catalyst (PEAD; Bernard & Thomas 1989)
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
- HOLD while price > trailing stop AND thesis intact (let winners run).
- TAKE_PARTIAL | reached take_profit_r and not yet trimmed | TRIM ~1/3-1/2, stop -> breakeven
- CONCENTRATION | weight > max_position_pct | TRIM toward target
- VALUATION_RICH | P/E >= pe_rich | HOLD, do not add
- REBALANCE only when a position breaches its relative tolerance band.

## Stage 4 — SELL triggers (any one fires)
- HARD_STOP | price < initial_stop (front-matter) | SELL
- TRAIL_STOP | price < chandelier = HighestHigh(atr_period) - atr_stop_mult*ATR | SELL
- MOMENTUM_STOP | momentum trade down >= momentum_stop_bom_pct from month-open | SELL (Han/Zhou/Zhu)
- EMA_BREAK | swing trade closes < EMA_fast | REVIEW (early), < EMA_slow | SELL
- THESIS_BREAK | front-matter thesis_broken: true (set by research step) | SELL
- TIME_STOP | catalyst window elapsed with no move | REVIEW

## Discipline guards (counteract behavioral leaks)
- No averaging down on a broken thesis (disposition effect; Odean 1998).
- Stops/targets defined in ATR/technical terms, not entry price (anti-anchoring).
- If net-of-cost performance trails a Shariah benchmark over ~50 trades / 12 mo,
  cut turnover and lengthen holds toward buy-and-hold (Barber & Odean 2000).

# Notes
# - The engine never auto-trades. After you execute, run /apply-trade.
# - Confirm Shariah thresholds with a qualified Saudi authority — informational, not a fatwa.
