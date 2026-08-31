from pathlib import Path

import pytest

from matrix_analyzer.infrastructure.json_loader import JSONLoader


EXAMPLE_MATRIX = Path("examples/matrix/conveyor_01.json")


def test_load_matrix_from_json() -> None:
    loader = JSONLoader()

    matrix = loader.load(EXAMPLE_MATRIX)

    assert matrix.rows == 4
    assert matrix.columns == 5
    assert matrix[0, 0] == pytest.approx(0.1704)
    assert matrix[1, 2] == pytest.approx(0.1245)
