from matrix_analyzer.domain.matrix import Matrix


class MatrixCollection:
    """Collection of named matrices."""

    def __init__(self) -> None:
        self._matrices: dict[str, Matrix] = {}

    def add(self, name: str, matrix: Matrix) -> None:
        if name in self._matrices:
            raise ValueError(f"Matrix '{name}' already exists")

        self._matrices[name] = matrix

    def get(self, name: str) -> Matrix:
        return self._matrices[name]

    def contains(self, name: str) -> bool:
        return name in self._matrices

    @property
    def count(self) -> int:
        return len(self._matrices)
