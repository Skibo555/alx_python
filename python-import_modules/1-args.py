#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_lenth = len(sys.argv) - 1
    for arg in int(argument_lenth):
        print("{:d}: {}".format(argument_lenth, arg))
    if argument_lenth > 0:
        print("{:d} argument:".format(argument_lenth))
    else:
        print(".")