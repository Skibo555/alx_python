#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix = [[1] + 1 for i in range(10)]
    for i in range(10):
        for j in range(10):
            matrix[i][j] = "{:d} {:d}".format(i, j)

    for i in range(10):
        for j in range(10):
            print(matrix[i][j], end='')
        print()