import json
from pathlib import Path

from matrix_analyzer.domain.matrix import Matrix


class JSONLoader:
    """Loads Matrix objects from JSON files."""

    def load(self, path: Path) -> Matrix:
        with path.open("r", encoding="utf-8") as file:
            payload = json.load(file)

        if "data" not in payload:
            raise ValueError("JSON must contain a 'data' field")

        return Matrix(payload["data"])
