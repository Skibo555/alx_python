#!/usr/bin/python3

def safe_print_division(a, b):
    sum = a / b
    try:
        print("Inside result: {}".format(sum))
    except ZeroDivisionError:
        print(sum)
    finally:
        print("Inside result: {}".format(sum))