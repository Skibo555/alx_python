#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument_lenth = len(sys.argv) - 1
    print("{:d} argument:".format(argument_lenth))
    for i in range(1, len(sys.argv)):
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
            if argument_lenth < 1:
                print("{:d} argument.".format(argument_lenth))