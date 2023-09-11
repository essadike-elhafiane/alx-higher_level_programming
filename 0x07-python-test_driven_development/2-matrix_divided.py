#!/usr/bin/python3

"""
Module: 2-matrix_divided
Contents: function used to divide matrix of integers
"""


def matrix_divided(matrix, div):
    """
    The matrx_divided function is used to divide a
    matrix of integers or float

    The matrix being divided must have row with equal
    sizes.

    Return value is a new matrix
    """
    new_matrix = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_of_row1 = len(matrix[0])
    for row_num in range(len(matrix)):
        if len_of_row1 != len(matrix[row_num]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for col_num in range(len_of_row1):
            if (type(matrix[row_num][col_num]) is not int and
               type(matrix[row_num][col_num]) is not float):
                raise TypeError(message)
            new_matrix[row_num].append(round(matrix[row_num][col_num]
                                             / div, 2))

    return new_matrix
