#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        i = a / b
    except ZeroDivisionError:
        come = i
    finally:
        print("Inside result: {}".format(come))