#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        i = a / b
    except ZeroDivisionError as a:
        print("None")
        return (a)
    except TypeError as b:
        print("None")
        return (b)
    finally:
        print("Inside result: {}".format(i))
        return (i)
