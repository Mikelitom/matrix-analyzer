from pathlib import Path

import pytest

from matrix_analyzer.infrastructure.exceptions import MatrixLoadError
from matrix_analyzer.infrastructure.json_loader import JSONLoader

EXAMPLE_MATRIX = Path("examples/matrix/conveyor_01.json")


def test_load_matrix_from_json() -> None:
    loader = JSONLoader()

    matrix = loader.load(EXAMPLE_MATRIX)

    assert matrix.rows == 4
    assert matrix.columns == 5
    assert matrix[0, 0] == pytest.approx(0.1704)
    assert matrix[1, 2] == pytest.approx(0.1245)


def test_file_not_found() -> None:
    loader = JSONLoader()

    with pytest.raises(MatrixLoadError, match="File not found"):
        loader.load(Path("does_not_exist.json"))


def test_missing_data_field() -> None: ...


def test_invalid_json(tmp_path: Path) -> None:
    file = tmp_path / "invalid.json"
    file.write_text("{ invalid json", encoding="utf-8")

    loader = JSONLoader()

    with pytest.raises(MatrixLoadError, match="Invalid JSON"):
        loader.load(file)


def test_inconsistent_row_lengths(tmp_path: Path) -> None:
    file = tmp_path / "matrix.json"

    file.write_text(
        """
        {
            "data": [
                [1.0, 2.0, 3.0],
                [4.0, 5.0]
            ]
        }
        """,
        encoding="utf-8",
    )

    loader = JSONLoader()

    with pytest.raises(MatrixLoadError, match="Invalid matrix data"):
        loader.load(file)


def test_invalid_matrix_value() -> None: ...
