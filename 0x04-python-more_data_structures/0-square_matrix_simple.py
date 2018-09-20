#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    b = []
    for i in range(len(matrix)):
        a = list(map(lambda x: x * x, matrix[i]))
        b.append(a)
    return b
