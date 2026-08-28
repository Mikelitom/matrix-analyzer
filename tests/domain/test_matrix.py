import numpy as np
import pytest

from matrix_analyzer.domain.matrix import Matrix


def test_matrix_shape():
    matrix = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
    ])

    assert matrix.shape == (2, 3)
    assert matrix.rows == 2
    assert matrix.columns == 3


def test_none_values_become_nan():
    matrix = Matrix([
        [1.0, None],
        [3.0, 4.0],
    ])

    assert matrix[0, 0] == 1.0
    assert np.isnan(matrix[0, 1])


def test_valid_count():
    matrix = Matrix([
        [1.0, None, 3.0],
        [None, 5.0, 6.0],
    ])

    assert matrix.valid_count == 4


def test_empty_matrix_is_rejected():
    with pytest.raises(ValueError):
        Matrix([])


def test_empty_row_is_rejected():
    with pytest.raises(ValueError):
        Matrix([
            [],
            [],
        ])


def test_inconsistent_rows_are_rejected():
    with pytest.raises(ValueError):
        Matrix([
            [1.0, 2.0],
            [3.0],
        ])


def test_non_numeric_values_are_rejected():
    with pytest.raises(TypeError):
        Matrix([
            [1.0, "invalid"],
        ])
