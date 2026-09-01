import math

from matrix_analyzer.domain.matrix import Matrix


def compare_matrices(
    matrix_a: Matrix,
    matrix_b: Matrix,
) -> list[list[float | None]]:
    if matrix_a.rows != matrix_b.rows or matrix_a.columns != matrix_b.columns:
        raise ValueError("Matrix dimensions are incompatible")

    result: list[list[float | None]] = []

    for row in range(matrix_a.rows):
        result_row: list[float | None] = []

        for column in range(matrix_a.columns):
            value_a = matrix_a[row, column]
            value_b = matrix_b[row, column]

            is_missing_a = math.isnan(value_a)
            is_missing_b = math.isnan(value_b)

            if is_missing_a and is_missing_b:
                result_row.append(None)
                continue

            if is_missing_a or is_missing_b:
                raise ValueError(
                    "Matrix values are incompatible: "
                    f"cell ({row}, {column}) contains a null value "
                    "in only one matrix"
                )

            result_row.append(abs(value_a - value_b))

        result.append(result_row)

    return result
