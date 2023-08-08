#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        argument_lenth = len(sys.argv)
        if argument_lenth > 0:
            print("{:d} argument:".format(argument_lenth))
        else:
            print(".")