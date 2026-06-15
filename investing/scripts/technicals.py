"""technicals.py — compute swing-trading indicators from daily price history.

fetch(ticker, cfg) tries yfinance; returns a dict of indicators or None on failure
(the verdict engine then skips technical rules gracefully). compute_from_df() is a
pure function so the math is testable without a network.
"""
from __future__ import annotations
import sys


def compute_from_df(df, cfg: dict) -> dict:
    """df: DataFrame with columns High, Low, Close, indexed by date (ascending)."""
    import pandas as pd  # local import so the module loads without pandas present
    n = int(cfg.get("atr_period", 22))
    high, low, close = df["High"], df["Low"], df["Close"]
    prev_close = close.shift(1)
    tr = pd.concat([(high - low),
                    (high - prev_close).abs(),
                    (low - prev_close).abs()], axis=1).max(axis=1)
    atr = tr.rolling(n).mean()
    atr_last = float(atr.iloc[-1])
    price = float(close.iloc[-1])

    ema_fast = float(close.ewm(span=int(cfg.get("ema_fast", 20)), adjust=False).mean().iloc[-1])
    ema_slow = float(close.ewm(span=int(cfg.get("ema_slow", 50)), adjust=False).mean().iloc[-1])
    hh = float(high.rolling(n).max().iloc[-1])
    chandelier = hh - float(cfg.get("atr_stop_mult", 3.0)) * atr_last

    def mom(skip, look):
        if len(close) > look:
            return float(close.iloc[-1 - skip] / close.iloc[-1 - look] - 1)
        return None

    # RSI(14), Wilder-style simple average
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain.iloc[-1] / loss.iloc[-1] if loss.iloc[-1] else float("inf")
    rsi = 100.0 if rs == float("inf") else 100 - 100 / (1 + rs)

    # relative volume (last vs 20-day average) if available
    rel_vol = None
    if "Volume" in df.columns:
        v = df["Volume"]
        avg = v.rolling(20).mean().iloc[-1]
        if avg:
            rel_vol = float(v.iloc[-1] / avg)

    # distance from 52-week high
    hi52 = float(high.rolling(min(252, len(high))).max().iloc[-1])
    dist_52w_high = (price / hi52 - 1) if hi52 else None

    # beginning-of-month close + drop
    bom_price, bom_drop = None, None
    try:
        idx = df.index
        cur = idx[-1]
        month_mask = (idx.year == cur.year) & (idx.month == cur.month)
        bom_price = float(close[month_mask].iloc[0])
        bom_drop = price / bom_price - 1
    except Exception:
        pass

    return {
        "price": round(price, 4),
        "atr": round(atr_last, 4),
        "atr_pct": round(atr_last / price * 100, 2) if price else None,
        "ema_fast": round(ema_fast, 4),
        "ema_slow": round(ema_slow, 4),
        "chandelier_stop": round(chandelier, 4),
        "mom_12_1": mom(21, 252),   # 12-month return, skip last month
        "mom_6_1": mom(21, 126),    # 6-month return, skip last month
        "mom_3_1": mom(21, 63),     # 3-month return, skip last month
        "rsi14": round(rsi, 1),
        "rel_volume": round(rel_vol, 2) if rel_vol is not None else None,
        "dist_52w_high_pct": round(dist_52w_high * 100, 1) if dist_52w_high is not None else None,
        "bom_price": round(bom_price, 4) if bom_price else None,
        "bom_drop_pct": round(bom_drop * 100, 2) if bom_drop is not None else None,
    }


def fetch(ticker: str, cfg: dict):
    try:
        import yfinance as yf
        df = yf.Ticker(ticker).history(period="1y")
        if df is None or df.empty or len(df) < int(cfg.get("atr_period", 22)) + 5:
            return None
        df = df.dropna(subset=["High", "Low", "Close"])
        keep = [c for c in ["High", "Low", "Close", "Volume"] if c in df.columns]
        return compute_from_df(df[keep], cfg)
    except Exception as e:
        print(f"[warn] technicals {ticker}: {e}", file=sys.stderr)
        return None
