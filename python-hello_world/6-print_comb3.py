#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i < j:
            print("{:d}, {:d}".format(i,j))
        else:
            print("{:d}{:d}".format(i,j))