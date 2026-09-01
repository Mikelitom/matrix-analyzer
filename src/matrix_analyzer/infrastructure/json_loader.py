import json
from pathlib import Path

from matrix_analyzer.domain.matrix import Matrix
from matrix_analyzer.infrastructure.exceptions import MatrixLoadError


class JSONLoader:
    """Loads Matrix objects from JSON files."""

    def load(self, path: Path) -> Matrix:
        try:
            with path.open("r", encoding="utf-8") as file:
                payload = json.load(file)
        except FileNotFoundError as error:
            raise MatrixLoadError(f"File not found: {path}") from error
        except json.JSONDecodeError as error:
            raise MatrixLoadError(f"Invalid JSON: {path}") from error

        if "data" not in payload:
            raise ValueError("JSON must contain a 'data' field")

        try:
            return Matrix(payload["data"])
        except (TypeError, ValueError) as error:
            raise MatrixLoadError("Invalid matrix data") from error
