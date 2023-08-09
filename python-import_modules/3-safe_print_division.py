#!/usr/bin/python3

def safe_print_division(a, b):
    sum = a / b
    try:
        a / b
    except ZeroDivisionError:
        print(sum)
    finally:
        print("Inside result: {}".format(sum))