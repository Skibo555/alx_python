#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        sum = a / b
    except ZeroDivisionError:
        return("{} / {}".format(a,b))
    finally:
        print("Inside result: {}".format(sum))