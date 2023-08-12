#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = " ".join("{:d}".format(item) for item in row)
        print(formatted_row)