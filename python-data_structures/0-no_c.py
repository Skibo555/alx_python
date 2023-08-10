#!/usr/bin/python3

def no_c(my_string):
    if not ('[c-C]') in my_string:
        new_string = my_string
        return new_string
    if not ('[o-O]') in my_string:
        new_tuple = my_string
        return new_tuple