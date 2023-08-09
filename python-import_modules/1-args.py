#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argument_length = len(sys.argv) - 1

if argument_length == 1:
    print("{:d} argument:".format(argument_length))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
if argument_length == 0:
    print("{:d} arguments.".format(argument_length))
elif argument_length > 1:
    print("{:d} arguments:".format(argument_length))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))