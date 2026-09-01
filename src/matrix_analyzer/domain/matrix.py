from __future__ import annotations

import numpy as np


class Matrix:
    """Represents a numerical matrix with optional missing values."""

    def __init__(self, data: list[list[float | None]]) -> None:
        if not data:
            raise ValueError("Matrix cannot be empty")

        if not all(data):
            raise ValueError("Matrix rows cannot be empty")

        column_count = len(data[0])

        if any(len(row) != column_count for row in data):
            raise ValueError("All matrix rows must have the same length")

        if any(
            value is not None and not isinstance(value, float)
            for row in data
            for value in row
        ):
            raise TypeError("Matrix values must be numbers or None")

        self._data = np.array(data, dtype=float)

    @property
    def shape(self) -> tuple[int, int]:
        return self._data.shape

    @property
    def rows(self) -> int:
        return self._data.shape[0]

    @property
    def columns(self) -> int:
        return self._data.shape[1]

    @property
    def valid_count(self) -> int:
        return int(np.count_nonzero(~np.isnan(self._data)))

    def __getitem__(self, index: tuple[int, int]) -> float:
        return float(self._data[index])

    @property
    def data(self) -> np.ndarray:
        return self._data.copy()
