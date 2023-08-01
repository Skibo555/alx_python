#!/usr/bin/python3
for i in range(101):
    print("{i:d}", end="0x{i:x}".format(i, i))