#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix is None:
        matrix = list()
    for num in matrix:
        print("{:d}".format(num))
    print(matrix)