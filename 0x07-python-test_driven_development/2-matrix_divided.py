#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(j/div, 2) for j in i] for i in matrix]
