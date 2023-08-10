#!/usr/bin/python3

def no_c(my_string):
    if ('[c]') not in my_string or ('[C]') not in my_string or ('[o]') not in my_string or ('[O]') not in my_string:
        my_tuple = my_string
        return my_tuple