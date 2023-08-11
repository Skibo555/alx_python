#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):  # Iterate over the indices of rows in the matrix
        matrix[i] = list(range(1, 4))  # Replace each row with [1, 2, 3]
        print("{:d}",str.format(matrix[i]).join(map(str, matrix[i])))  # Print the modified row