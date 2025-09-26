import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter

def describe_categorical(df, columns = None, round_pct = 1, top_n = None):
    """
    Prints counts and percentages for categorical columns in a compact format.

    Parameters:
    - df: pandas DataFrame
    - columns: str or list of column names (optional). If None, use all categorical columns.
    - round_pct: int, number of decimal places to round percentages
    - top_n: int or None, show only top N most frequent values
    """
    # Allow single column as string
    if isinstance(columns, str):
        columns = [columns]

    # Use all categorical columns if none provided
    if columns is None:
        columns = df.select_dtypes(include=["category", "object"]).columns.tolist()

    # Validate columns are categorical
    for col in columns:
        if col not in df.columns:
            print(f"[Warning] Column '{col}' not found in DataFrame.")
            continue
        if df[col].dtype not in ["object", "category"]:
            print(f"[Skipped] Column '{col}' is not categorical.")
            continue

        counts = df[col].value_counts()
        percentages = df[col].value_counts(normalize = True) * 100
        desc = [
            f"{idx}: {cnt} ({pct:.{round_pct}f}%)"
            for idx, cnt, pct in zip(counts.index, counts, percentages)
        ]
        
        if top_n is not None:
            desc = desc[:top_n]

        print(f"\n=== {col} ===")
        print("\n".join(desc))


def thousands_formatter(x, pos):
    """
    Formats x-axis tick values into a more readable string format with dollar sign and 'K' for thousands.

    Parameters:
    x (float): The tick value.
    pos (int): The tick position (required by matplotlib but unused here).

    Returns:
    str: Formatted tick label, e.g., $50K for 50000.
    """
    return f'${int(x / 1000):,}K'
