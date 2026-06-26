"""
utils.py

Version : 1.0
Project : NASA-CMAPSS-RUL
Author  : Sarthak Thapliyal

General utility functions used throughout the project.
"""

from __future__ import annotations

import random
from typing import Iterable

import numpy as np
import pandas as pd


# ============================================================
# RANDOM SEED
# ============================================================

def set_random_seed(seed: int = 42) -> None:
    """
    Set random seed for reproducibility.

    Parameters
    ----------
    seed : int
        Random seed.
    """

    random.seed(seed)
    np.random.seed(seed)


# ============================================================
# DATAFRAME VALIDATION
# ============================================================

def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Ensure input is a valid pandas DataFrame.

    Raises
    ------
    TypeError
        If input is not a pandas DataFrame.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )


# ============================================================
# COLUMN VALIDATION
# ============================================================

def validate_required_columns(
    df: pd.DataFrame,
    required_columns: Iterable[str]
) -> None:
    """
    Verify that all required columns exist.

    Parameters
    ----------
    df : pandas.DataFrame

    required_columns : iterable

    Raises
    ------
    ValueError
        If one or more columns are missing.
    """

    validate_dataframe(df)

    missing = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing:

        raise ValueError(
            f"Missing required columns: {missing}"
        )


# ============================================================
# DATASET SUMMARY
# ============================================================

def print_dataset_summary(df: pd.DataFrame) -> None:
    """
    Print a quick summary of a dataframe.
    """

    validate_dataframe(df)

    rows, cols = df.shape

    duplicates = df.duplicated().sum()

    missing = df.isna().sum().sum()

    memory = (
        df.memory_usage(deep=True).sum()
        / 1024**2
    )

    print("=" * 50)
    print("DATASET SUMMARY")
    print("=" * 50)

    print(f"Rows            : {rows:,}")
    print(f"Columns         : {cols}")

    print(f"Missing Values  : {missing:,}")

    print(f"Duplicate Rows  : {duplicates:,}")

    print(f"Memory Usage    : {memory:.2f} MB")

    print("=" * 50)