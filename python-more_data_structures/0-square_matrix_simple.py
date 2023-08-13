#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for row in matrix:
        for index, element in enumerate(row):
            newMatrix = element[index ** 2]
            return newMatrix
            #print("{:d}".format(newMatrix), end="")