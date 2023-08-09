#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        sum = a / b
    except ZeroDivisionError:
        return (sum)
    finally:
        return ("Inside result: {}".format(sum))