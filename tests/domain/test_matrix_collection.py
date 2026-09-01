import pytest

from matrix_analyzer.domain.matrix import Matrix
from matrix_analyzer.domain.matrix_collection import MatrixCollection


def test_collection_starts_empty() -> None:
    collection = MatrixCollection()

    assert collection.count == 0


def test_add_matrix() -> None:
    collection = MatrixCollection()
    matrix = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    collection.add("matrix_01", matrix)

    assert collection.count == 1


def test_get_matrix_by_name() -> None:
    collection = MatrixCollection()
    matrix = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    collection.add("matrix_01", matrix)

    result = collection.get("matrix_01")

    assert result is matrix


def test_collection_contains_matrix() -> None:
    collection = MatrixCollection()
    matrix = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    collection.add("matrix_01", matrix)

    assert collection.contains("matrix_01")
    assert not collection.contains("matrix_02")


def test_add_duplicate_name_raises_error() -> None:
    collection = MatrixCollection()

    matrix_a = Matrix(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    matrix_b = Matrix(
        [
            [5.0, 6.0],
            [7.0, 8.0],
        ]
    )

    collection.add("matrix_01", matrix_a)

    with pytest.raises(ValueError, match="already exists"):
        collection.add("matrix_01", matrix_b)


def test_get_unknown_name_raises_error() -> None:
    collection = MatrixCollection()

    with pytest.raises(KeyError, match="matrix_01"):
        collection.get("matrix_01")
