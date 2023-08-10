#!/usr/bin/python3

def no_c(my_string):
    if not ('[c]') in my_string:
        new_string = my_string
        return new_string
    if not ('[C]') in my_string:
        new_string = my_string
        return new_string
    if not ('[o]') in my_string:
        new_string = my_string
        return new_string
    if not ('[O]') in my_string:
        new_string = my_string
        return new_string