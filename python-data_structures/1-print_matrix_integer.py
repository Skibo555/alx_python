#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in matrix:
            matrix[i].append(j)
            return matrix
        print("{:d}".format(matrix), end="")