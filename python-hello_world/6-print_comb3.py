#!/usr/bin/python3
for i in range(9):
    print("{:d}".format(i), end="")
    for j in range(10):
        if i < j or i == 8 and j == 9:
        print("{:d}, ".format(j), end="")
        print("{:d}{:d}".format(i,j))