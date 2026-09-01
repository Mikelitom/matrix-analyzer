import pytest

from matrix_analyzer.domain.comparison import compare_matrices
from matrix_analyzer.domain.matrix import Matrix


def test_identical_matrices_have_zero_difference() -> None:
    matrix_a = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    matrix_b = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    result = compare_matrices(matrix_a, matrix_b)

    assert result == [
        [0.0, 0.0],
        [0.0, 0.0],
    ]


def test_difference_is_calculated_for_valid_values() -> None:
    matrix_a = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    matrix_b = Matrix(
        [
            [1.5, 1.0],
            [2.0, 6.0],
        ]
    )

    result = compare_matrices(matrix_a, matrix_b)

    assert result == [
        [0.5, 1.0],
        [1.0, 2.0],
    ]


def test_none_values_are_ignored_when_both_are_none() -> None:
    matrix_a = Matrix(
        [
            [1.0, None, 3.0],
            [None, 5.0, None],
        ]
    )

    matrix_b = Matrix(
        [
            [2.0, None, 4.0],
            [None, 7.0, None],
        ]
    )

    result = compare_matrices(matrix_a, matrix_b)

    assert result == [
        [1.0, None, 1.0],
        [None, 2.0, None],
    ]


def test_none_and_value_are_incompatible() -> None:
    matrix_a = Matrix(
        [
            [1.0, None],
        ]
    )

    matrix_b = Matrix(
        [
            [1.0, 2.0],
        ]
    )

    with pytest.raises(ValueError, match="incompatible"):
        compare_matrices(matrix_a, matrix_b)


def test_matrices_with_different_dimensions_are_incompatible() -> None:
    matrix_a = Matrix(
        [
            [1.0, 2.0],
        ]
    )

    matrix_b = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    with pytest.raises(ValueError, match="dimensions"):
        compare_matrices(matrix_a, matrix_b)
