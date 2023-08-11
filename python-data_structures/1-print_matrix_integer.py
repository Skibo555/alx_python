#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}".format(row) end=" ")  # Adjust the formatting as needed
        print()  # Move to the next line after each row