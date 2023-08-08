#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument_lenth = len(sys.argv) - 1
    print("{:d} argument:".format(argument_lenth))
    for arg in sys.argv[1:]:
        argument_lenth = len(sys.argv)
        print("{}: {}".format(arg, argument_lenth))
    if argument_lenth > 0:
        print(".")