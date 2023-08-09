#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        i = a / b
    except ZeroDivisionError as e:
        print("Inside result: {}".format(e))
    except ValueError as k:
        return k
    finally:
        if 'i' in locals():
            print("Inside result: {}".format(i))
    return i