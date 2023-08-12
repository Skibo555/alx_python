#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
   if matrix is None:
        matrix = []
        for i in range(0, 9, 3):
            sublist = [j for j in range(i + 1, i + 4)]
        matrix.append(sublist)
    
        for row in matrix:
            print(row[".format(", "{:d}"])
   