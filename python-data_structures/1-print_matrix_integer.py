#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    for i in range(1, 10, 3):
        row = ' '.join(str(num) for num in range(i, i + 3))
        print("{:d}".format(row))