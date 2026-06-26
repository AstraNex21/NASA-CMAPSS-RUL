"""
data_loader.py

Version : 1.0
Project : NASA-CMAPSS-RUL
Author  : Sarthak Thapliyal

Utility functions for loading NASA C-MAPSS datasets.
"""

from pathlib import Path
import pandas as pd


# ============================================================
# COLUMN NAMES
# ============================================================

COLUMN_NAMES = [
    "engine_id",
    "cycle",
    "setting_1",
    "setting_2",
    "setting_3",
]

for i in range(1, 22):
    COLUMN_NAMES.append(f"sensor_{i}")


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"


# ============================================================
# TRAINING DATA
# ============================================================

def load_training_data(dataset: str = "FD001") -> pd.DataFrame:
    """
    Load NASA C-MAPSS training dataset.

    Parameters
    ----------
    dataset : str

        One of:
        - FD001
        - FD002
        - FD003
        - FD004

    Returns
    -------
    pandas.DataFrame
    """

    dataset = dataset.upper()

    filename = f"train_{dataset}.txt"

    filepath = RAW_DATA_PATH / filename

    if not filepath.exists():
        raise FileNotFoundError(
            f"Training dataset not found:\n{filepath}"
        )

    df = pd.read_csv(
        filepath,
        sep=r"\s+",
        header=None,
        names=COLUMN_NAMES,
    )

    return df


# ============================================================
# TEST DATA
# ============================================================

def load_test_data(dataset: str = "FD001") -> pd.DataFrame:
    """
    Load NASA C-MAPSS test dataset.
    """

    dataset = dataset.upper()

    filename = f"test_{dataset}.txt"

    filepath = RAW_DATA_PATH / filename

    if not filepath.exists():
        raise FileNotFoundError(
            f"Test dataset not found:\n{filepath}"
        )

    df = pd.read_csv(
        filepath,
        sep=r"\s+",
        header=None,
        names=COLUMN_NAMES,
    )

    return df


# ============================================================
# TRUE RUL
# ============================================================

def load_rul(dataset: str = "FD001") -> pd.DataFrame:
    """
    Load true Remaining Useful Life values for the test dataset.
    """

    dataset = dataset.upper()

    filename = f"RUL_{dataset}.txt"

    filepath = RAW_DATA_PATH / filename

    if not filepath.exists():
        raise FileNotFoundError(
            f"RUL file not found:\n{filepath}"
        )

    rul = pd.read_csv(
        filepath,
        header=None,
        names=["RUL"]
    )

    return rul