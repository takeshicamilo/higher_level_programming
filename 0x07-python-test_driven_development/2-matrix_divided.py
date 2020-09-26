#!/usr/bin/python3
"""Matrix divided"""


def matrix_divided(matrix, div):
    """Matrix divided"""

    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (type(div)is not int and type(div)is not float):
        raise TypeError("div must be a number")

    x_row = len(matrix[0])

    for row in range(len(matrix)):
        temp_row = len(matrix[row])

        if (temp_row is not x_row):
            raise TypeError("Each row of the matrix must have the same size")
        x_row = temp_row
        for x in range(len(matrix[row])):
            if (type(matrix[row][x]) is not int and
                    type(matrix[row][x]) is not float):
                raise TypeError('matrix must be a matrix'
                                ' (list of lists) of integers/floats')
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
