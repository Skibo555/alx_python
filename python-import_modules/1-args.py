#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument_lenth = len(sys.argv) - 1
    print("{:d} argument:".format(argument_lenth))
    argument_lenth = len(sys.argv)
    print("{:d}: {}".format(argument_lenth, sys.argv))
    if argument_lenth > 0:
        print(".")