#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        i = a / b
    except ZeroDivisionError as e:
        print("Inside result: {}".format(e))
    except NameError as k:
        print("Inside result: {}".format(k))
    finally:
        print("Inside result: {}".format(i))
        return(i)