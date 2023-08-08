#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_lenth = len(sys.argv)
    if argument_lenth > 0:
        print("{:d} argument:".format(argument_lenth))
    else:
        print(".")
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(argument_lenth, arg))