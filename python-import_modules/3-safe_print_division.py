#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        i = a / b
    except ZeroDivisionError:
        i = None
        print("Inside result: {}".format(i))
    finally:
        print("Inside result: {}".format(i))
        return (i)
