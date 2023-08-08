#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_lenth = len(sys.argv) - 1
    for i in argument_lenth:
        if argument_lenth > 0:
            print("{:d} argument:".format(i))
        else:
            print(".")
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(i, arg))