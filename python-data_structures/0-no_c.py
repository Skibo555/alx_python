#!/usr/bin/python3

def no_c(my_string):
    if not ('[c-C]') or ('[o-O]') in my_string:
        new_string = my_string
        return new_string