import pandas as pd
import numpy as np
import re
from datetime import datetime


def parse_price(price_text):
    if pd.isna(price_text):
        return None
    # Extract first number with 2 to 7 digits
    match = re.search(r"\b\d{2,7}\b", price_text.replace(",", "").replace(" ", ""))
    if match:
        return float(match.group())
    return None


def prepare_prices(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["parsed_price"] = df["extracted_prices"].apply(parse_price)
    return df


def calculate_posting_frequency(dates: pd.Series) -> float:
    if dates.empty:
        return 0.0
    min_date = dates.min()
    max_date = dates.max()
    weeks = max((max_date - min_date).days / 7, 1)
    return round(len(dates) / weeks, 2)


def compute_vendor_metrics(df: pd.DataFrame) -> pd.DataFrame:
    vendors = []
    grouped = df.groupby("Channel Username")

    for vendor, group in grouped:
        vendor_name = vendor
        avg_views = group["Views"].mean()
        freq = calculate_posting_frequency(pd.to_datetime(group["Date"]))

        # Top post
        top_row = group.loc[group["Views"].idxmax()]
        top_product = top_row.get("extracted_products")
        top_price = parse_price(top_row.get("extracted_prices"))

        # Business profile
        avg_price = group["parsed_price"].dropna().mean()

        # Lending score (simple weighted average)
        lending_score = 0.5 * avg_views + 0.5 * freq

        vendors.append({
            "Vendor": vendor_name,
            "Avg. Views/Post": round(avg_views, 2),
            "Posts/Week": freq,
            "Avg. Price (ETB)": round(avg_price, 2) if not np.isnan(avg_price) else None,
            "Top Product": top_product,
            "Top Price (ETB)": top_price,
            "Lending Score": round(lending_score, 2)
        })

    return pd.DataFrame(vendors)


def save_scorecard(scorecard_df: pd.DataFrame, path="vendor_scorecard.csv"):
    scorecard_df.to_csv(path, index=False)
    print(f"[INFO] Scorecard saved to {path}")
