#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument_lenth = len(sys.argv) - 1
    print("{:d} argument:".format(argument_lenth))
    for arg in sys.argv[1:]:
        for i in sys.argv:
            print("{}: {}".format(int(i), arg))
    if argument_lenth > 0:
        print(".")