#!/usr/bin/python3
for i in range(9):
    print("{:d}".format(i))
    for j in range(10):
        print("{:d}{:d}".format(j))
        if i < j:
            print("{:d}, {:d}".format(i,j))