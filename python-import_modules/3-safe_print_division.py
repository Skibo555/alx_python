#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        a = a / b
    except ZeroDivisionError:
        return("None")
    finally:
        print("Inside result: {}".format(a))