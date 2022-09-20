#!/usr/bin/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix that contains elements
    """
    msg1 = 'matrix must be a matrix (list of lists) of integers/floats'
    msg2 = 'Each row of the matrix must have the same size'
    if div == 0:
        raise(TypeError("division by zero"))
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif len(matrix) < 2:
        raise TypeError(msg1)
    else:

        length = len(matrix[0])
        new_matrix = [matrix[:] for matrix in matrix]
        for x in range(0, len(matrix)):
            if isinstance(matrix[x], list) is False:
                raise TypeError(msg1)
            elif len(matrix[x]) != length:
                raise(TypeError(msg2))
            else:
                for y in range(0, len(matrix[x])):
                    if type(matrix[x][y]) == int or\
                       type(matrix[x][y]) == float:
                        new_matrix[x][y] = round((matrix[x][y]/div), 2)
                    else:
                        raise TypeError(msg1)
    return new_matrix
