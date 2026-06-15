"""screener.py — short-term candidate RANKER.

Scores a universe YOU define (universe.md) by mechanical short-term signals —
momentum, trend, RSI, relative volume, volatility — and ranks them. It does NOT
predict winners and does NOT assert any will be profitable; it surfaces facts and
orders them by criteria you set in rules.md. Compliance is informational only by
default (weight 0) — you decide that in your own tool. Verbs: BUY-CANDIDATE
(cleared your mechanical bar) / RESEARCH / AVOID.
"""
from __future__ import annotations
import json
import os
import re
import sys
import yaml
import technicals

HERE = os.path.dirname(__file__)
RULES = os.path.join(HERE, "..", "rules.md")
UNIVERSE = os.path.join(HERE, "..", "universe.md")


def load_cfg() -> dict:
    txt = open(RULES, encoding="utf-8").read()
    return (yaml.safe_load(txt.split("---", 2)[1]) or {}) if txt.startswith("---") else {}


def load_universe() -> list[str]:
    out = []
    for line in open(UNIVERSE, encoding="utf-8"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if re.fullmatch(r"[A-Za-z][A-Za-z.\-]{0,9}", s):
            out.append(s.upper())
    return out


def _norm(vals):
    """min-max to 0..1; if all equal or single, return 0.5 each."""
    xs = [v for v in vals if v is not None]
    if len(xs) < 2 or max(xs) == min(xs):
        return [0.5 if v is not None else 0.0 for v in vals]
    lo, hi = min(xs), max(xs)
    return [((v - lo) / (hi - lo)) if v is not None else 0.0 for v in vals]


def rsi_score(r):
    """Prefer ~55-70 (strong, not overbought). 0..1."""
    if r is None:
        return None
    if r >= 80:
        return 0.2
    if r < 40:
        return 0.2
    return max(0.0, 1 - abs(r - 62) / 22)


def score_universe(rows: list[dict], cfg: dict) -> list[dict]:
    """rows: [{ticker, tech}]. Pure function (testable without network)."""
    w = {k: float(cfg.get(f"screen_weight_{k}", d)) for k, d in
         [("momentum", .4), ("trend", .25), ("rsi", .15),
          ("volume", .1), ("lowvol", .1), ("compliance", 0.0)]}

    def comp(t):  # raw component metrics
        if not t:
            return {}
        mom = None
        if t.get("mom_3_1") is not None and t.get("mom_6_1") is not None:
            mom = 0.5 * t["mom_3_1"] + 0.5 * t["mom_6_1"]
        trend = None
        if t.get("ema_slow"):
            trend = t["price"] / t["ema_slow"] - 1
        return {"mom": mom, "trend": trend, "rsi": rsi_score(t.get("rsi14")),
                "vol": t.get("rel_volume"), "lowvol": (-t["atr_pct"] if t.get("atr_pct") else None)}

    metrics = [comp(r.get("tech")) for r in rows]
    nm = {k: _norm([m.get(k) for m in metrics]) for k in ["mom", "trend", "vol", "lowvol"]}
    out = []
    for i, r in enumerate(rows):
        t = r.get("tech")
        if not t or t.get("price") is None:
            out.append({"ticker": r["ticker"], "verdict": "AVOID",
                        "score": None, "why": "no price data"})
            continue
        if t["price"] < float(cfg.get("screen_min_price", 1.0)):
            out.append({"ticker": r["ticker"], "verdict": "AVOID",
                        "score": 0, "why": f"price ${t['price']:g} < min"})
            continue
        rsi_s = metrics[i].get("rsi") or 0.0
        comp_score = (w["momentum"] * nm["mom"][i] + w["trend"] * nm["trend"][i] +
                      w["rsi"] * rsi_s + w["volume"] * nm["vol"][i] +
                      w["lowvol"] * nm["lowvol"][i])
        denom = sum(w[k] for k in ["momentum", "trend", "rsi", "volume", "lowvol"]) or 1
        score = round(comp_score / denom * 100, 1)
        verb = "BUY-CANDIDATE" if score >= float(cfg.get("screen_buy_candidate_score", 65)) else "RESEARCH"
        out.append({
            "ticker": r["ticker"], "verdict": verb, "score": score,
            "signals": {"mom_3_1_pct": round(t["mom_3_1"]*100,1) if t.get("mom_3_1") is not None else None,
                        "mom_6_1_pct": round(t["mom_6_1"]*100,1) if t.get("mom_6_1") is not None else None,
                        "rsi14": t.get("rsi14"), "rel_volume": t.get("rel_volume"),
                        "atr_pct": t.get("atr_pct"),
                        "vs_ema50_pct": round((t["price"]/t["ema_slow"]-1)*100,1) if t.get("ema_slow") else None,
                        "dist_52w_high_pct": t.get("dist_52w_high_pct")},
            "compliance": "verify in your own tool (informational; weight %.2f)" % w["compliance"],
        })
    return sorted(out, key=lambda x: (x["score"] is not None, x["score"] or 0), reverse=True)


def main():
    cfg = load_cfg()
    tickers = load_universe()
    if not tickers:
        print(json.dumps({"error": "universe.md is empty — add tickers to rank"}))
        return
    rows = [{"ticker": t, "tech": technicals.fetch(t, cfg)} for t in tickers]
    ranked = score_universe(rows, cfg)
    print(json.dumps({
        "ranked": ranked,
        "disclaimer": ("Mechanical ranking of YOUR universe by signals you set. Not a "
                       "prediction or advice; verify compliance and decide yourself. "
                       "BUY-CANDIDATE = cleared the mechanical bar, not 'will rise'."),
    }, indent=2))


if __name__ == "__main__":
    main()
