#!/usr/bin/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix that contains elements
    """
    new_matrix=[]
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for x in range(len(matrix)):
        if len(matrix[0]) != len(matrix[x]):
            raise TypeError(msg2)
        new_matrix.append([])
        for y in range(len(matrix[x])):
            if type(matrix[x][y]) != int and type(matrix[x][y]) != float:
                raise TypeError(msg1)
            new_matrix[x].append(round(matrix[x][y] / div, 2))
    return new_matrix
