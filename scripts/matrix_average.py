import json
from pathlib import Path

import numpy as np


MATRIX_DIR = Path("examples/matrix")

FILES = [
    MATRIX_DIR / "matrix_01.json",
    MATRIX_DIR / "matrix_02.json",
    MATRIX_DIR / "matrix_03.json",
    MATRIX_DIR / "matrix_04.json",
    MATRIX_DIR / "matrix_05.json",
]

OUTPUT_FILE = MATRIX_DIR / "average.json"


def load_matrix(path: Path) -> np.ndarray:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return np.array(data["data"], dtype=float)


def main() -> None:
    matrices = np.array([load_matrix(path) for path in FILES])

    print(f"Matrices cargadas: {len(matrices)}")
    print(f"Dimensiones: {matrices.shape}")

    # Promedio por celda ignorando NaN.
    average = np.nanmean(matrices, axis=0)

    # Cantidad de valores válidos usados para cada promedio.
    valid_counts = np.sum(~np.isnan(matrices), axis=0)

    # Si ninguna matriz tiene dato en una posición, conservar null.
    average = np.where(valid_counts == 0, np.nan, average)

    # Convertir NaN nuevamente a None para poder guardarlo como JSON.
    average_json = [
        [None if np.isnan(value) else round(float(value), 6) for value in row]
        for row in average
    ]

    result = {
        "name": "conveyor_dark_pixel_average",
        "type": "conveyor_dark_pixel_average",
        "source_matrices": [path.name for path in FILES],
        "data": average_json,
    }

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2, ensure_ascii=False)

    print(f"Promedio generado: {OUTPUT_FILE}")

    print("\nCantidad de valores usados por celda:")
    print(valid_counts)


if __name__ == "__main__":
    main()
