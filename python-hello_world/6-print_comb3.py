#!/usr/bin/python3
for i in range(9):
    print("{:d}".format(i), end="")
    for j in range(1, 10):
        while i < j:
            print("{:d}{:d}, ".format(i,j), end="")
        else:
            print("{:d}{:d}".format(i,j))