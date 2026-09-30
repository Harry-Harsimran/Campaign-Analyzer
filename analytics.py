import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / "data" / "campaign_data.csv"


def load():
    df = pd.read_csv(DATA, parse_dates=["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)
    df["CAC"] = df["spend"] / df["customers_acquired"].where(df["customers_acquired"] > 0)
    df["ROI"] = (df["revenue"] - df["spend"]) / df["spend"]
    df["ROAS"] = df["revenue"] / df["spend"]
    df["conv_rate"] = df["customers_acquired"] / df["leads"].where(df["leads"] > 0)
    return df


def _totals(g):
    spend, rev = g["spend"].sum(), g["revenue"].sum()
    cust, leads, clicks = g["customers_acquired"].sum(), g["leads"].sum(), g["clicks"].sum()
    return {
        "spend": round(spend, 2), "revenue": round(rev, 2), "customers": int(cust),
        "CAC": round(spend / cust, 2) if cust else 0,
        "ROI": round((rev - spend) / spend, 2) if spend else 0,
        "ROAS": round(rev / spend, 2) if spend else 0,
        "click_to_lead": round(leads / clicks, 4) if clicks else 0,
        "lead_to_customer": round(cust / leads, 4) if leads else 0,
        "campaigns": len(g),
    }


def kpis(df):
    return _totals(df)


def _group(df, col):
    rows = []
    for name, g in df.groupby(col):
        rows.append({col: name, **_totals(g)})
    return rows


def by_channel(df):
    return sorted(_group(df, "channel"), key=lambda r: r["ROI"], reverse=True)


def by_type(df):
    return sorted(_group(df, "campaign_type"), key=lambda r: r["ROI"], reverse=True)


def by_month(df):
    return sorted(_group(df, "month"), key=lambda r: r["month"])


def campaigns(df, channel=None, ctype=None, sort="ROI", desc=True):
    if channel:
        df = df[df["channel"] == channel]
    if ctype:
        df = df[df["campaign_type"] == ctype]
    if sort not in df.columns:
        sort = "ROI"
    df = df.sort_values(sort, ascending=not desc)
    out = df[["campaign_id", "channel", "campaign_type", "date", "spend", "revenue",
              "customers_acquired", "CAC", "ROI", "ROAS", "conv_rate"]].copy()
    out["date"] = out["date"].dt.strftime("%Y-%m-%d")
    return out.round(3).to_dict("records")
