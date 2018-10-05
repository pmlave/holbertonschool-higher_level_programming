#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divide every element of a matrix by a certain number

    Args:

        matrix: The given matrix to divide

        div: The number by which to divide

    Returns: New matrix with divided values

    """
    if not isinstance(matrix, list) or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError("matrix must be a matrix (list of lists) of"
                            " integers/floats")
        if len(lists) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of"
                            " integers/floats")
        for value in lists:
            if not isinstance(value, int or float):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
    length = len(matrix[0])
    if any(len(list) != length for list in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int or float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(value / div, 2) for value in i]for i in matrix]
