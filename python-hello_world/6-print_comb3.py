#!/usr/bin/python3
for i in range(9):
    print("{:d}".format(i) end=)
    for j in range(10):
        print("{:d}, ".format(j) end=)
        if i < j or i == 8 and j == 9:
            print("{:d}{:d}".format(i,j))