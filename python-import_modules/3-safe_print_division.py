#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        sum = a / b
    except ZeroDivisionError:
        print("None")
    finally:
        ("{} // {} = {}".format(a, b, sum))
        print("Inside result: {}".format(sum))