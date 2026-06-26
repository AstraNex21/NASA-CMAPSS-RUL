"""
sequence_generator.py

Version : 1.0
Project : NASA-CMAPSS-RUL
Author  : Sarthak Thapliyal

Generate sliding-window sequences for Remaining Useful Life prediction.
"""

from __future__ import annotations

import pandas as pd

from src import utils


class SequenceGenerator:
    """
    Generate fixed-length sequences from time-series data.

    Parameters
    ----------
    window_size : int
        Number of consecutive cycles in each input sequence.

    stride : int
        Step size between consecutive windows.
    """

    def __init__(
        self,
        window_size: int = 30,
        stride: int = 1
    ) -> None:

        self.window_size = window_size
        self.stride = stride

    def _validate_inputs(
        self,
        df: pd.DataFrame
    ) -> None:
        """
        Validate input dataframe.
        """

        utils.validate_dataframe(df)

        utils.validate_required_columns(
            df,
            [
                "engine_id",
                "cycle",
                "RUL"
            ]
        )

        if self.window_size <= 0:
            raise ValueError(
                "window_size must be greater than zero."
            )

        if self.stride <= 0:
            raise ValueError(
                "stride must be greater than zero."
            )

    def transform(
        self,
        df: pd.DataFrame
    ):
        """
        Placeholder for sequence generation.

        Version 1.0 only validates inputs.
        """

        self._validate_inputs(df)

        print("Input validation successful.")
        print("Sequence generation will be implemented in Version 1.1.")

        return None