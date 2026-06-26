"""
preprocessing.py

Preprocessing utilities for the NASA C-MAPSS Remaining Useful Life (RUL) project.

Author: Sarthak Thapliyal
Project: NASA-CMAPSS-RUL
"""

import pandas as pd


def calculate_rul(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Remaining Useful Life (RUL) for each engine.

    RUL = Maximum cycle of an engine - Current cycle

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing:
            - engine_id
            - cycle

    Returns
    -------
    pandas.DataFrame
        DataFrame with an additional 'RUL' column.
    """

    df = df.copy()

    # Find maximum cycle for every engine
    max_cycle = (
        df.groupby("engine_id")["cycle"]
        .max()
        .reset_index()
        .rename(columns={"cycle": "max_cycle"})
    )

    # Merge maximum cycle back into original dataframe
    df = df.merge(max_cycle, on="engine_id")

    # Calculate Remaining Useful Life
    df["RUL"] = df["max_cycle"] - df["cycle"]

    # Remove helper column
    df.drop(columns=["max_cycle"], inplace=True)

    return df


def cap_rul(df: pd.DataFrame, max_rul: int = 125) -> pd.DataFrame:
    """
    Cap RUL values at a specified maximum.

    Example
    -------
    Before:
        191, 190, 189, ..., 130, 129, ...

    After (max_rul = 125):
        125, 125, 125, ..., 125, 124, ...

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing an 'RUL' column.

    max_rul : int, default=125
        Maximum RUL value.

    Returns
    -------
    pandas.DataFrame
        DataFrame with capped RUL values.
    """

    df = df.copy()

    df["RUL"] = df["RUL"].clip(upper=max_rul)

    return df