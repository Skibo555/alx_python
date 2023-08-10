#!/usr/bin/python3

def no_c(my_string):
    if ('[c]', '[C]', '[o]', '[O]') in my_string:
        del 'c', 'C', 'O', 'o'
        my_tuple = my_string
        return my_tuple