#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        matrix[i] = range(1, 4)
        print("{:d}",str.format(matrix[i]))