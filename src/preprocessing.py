"""
preprocessing.py

Version : 1.2
Project : NASA-CMAPSS-RUL
Author  : Sarthak Thapliyal

Preprocessing utilities for NASA C-MAPSS Remaining Useful Life prediction.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler


# ============================================================
# RUL GENERATION
# ============================================================

def calculate_rul(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Remaining Useful Life (RUL).

    RUL = Maximum cycle - Current cycle
    """

    df = df.copy()

    max_cycle = (
        df.groupby("engine_id")["cycle"]
        .max()
        .reset_index()
        .rename(columns={"cycle": "max_cycle"})
    )

    df = df.merge(max_cycle, on="engine_id")

    df["RUL"] = df["max_cycle"] - df["cycle"]

    df.drop(columns=["max_cycle"], inplace=True)

    return df


# ============================================================
# RUL CAPPING
# ============================================================

def cap_rul(df: pd.DataFrame, max_rul: int = 125) -> pd.DataFrame:
    """
    Cap RUL values.
    """

    df = df.copy()

    df["RUL"] = df["RUL"].clip(upper=max_rul)

    return df


# ============================================================
# CONSTANT FEATURE DETECTION
# ============================================================

def get_constant_features(df: pd.DataFrame) -> list:
    """
    Return all constant columns.
    """

    constant_columns = []

    for column in df.columns:

        if df[column].nunique() == 1:
            constant_columns.append(column)

    return constant_columns


# ============================================================
# REMOVE CONSTANT FEATURES
# ============================================================

def remove_constant_features(df: pd.DataFrame):
    """
    Remove constant columns.

    Returns
    -------
    cleaned_dataframe
    removed_columns
    """

    df = df.copy()

    constant_columns = get_constant_features(df)

    cleaned_df = df.drop(columns=constant_columns)

    return cleaned_df, constant_columns


# ============================================================
# FEATURE MANAGEMENT
# ============================================================

def get_feature_columns(df: pd.DataFrame) -> list:
    """
    Return all feature columns.

    Excludes:
    - engine_id
    - cycle
    - RUL
    """

    excluded = [
        "engine_id",
        "cycle",
        "RUL"
    ]

    return [col for col in df.columns if col not in excluded]


def get_target_column() -> str:
    """
    Return target column name.
    """

    return "RUL"


# ============================================================
# FEATURE SCALING
# ============================================================

def fit_scaler(df: pd.DataFrame):
    """
    Fit StandardScaler using feature columns.
    """

    feature_columns = get_feature_columns(df)

    scaler = StandardScaler()

    scaler.fit(df[feature_columns])

    return scaler


def transform_features(
    df: pd.DataFrame,
    scaler: StandardScaler
):
    """
    Transform feature columns using fitted scaler.
    """

    df = df.copy()

    feature_columns = get_feature_columns(df)

    df[feature_columns] = scaler.transform(
        df[feature_columns]
    )

    return df