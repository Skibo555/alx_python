#!/usr/bin/python3

def no_c(my_string):
    filtered_string = ""
    for char in my_string:
        if char not in ['[o]', '[O]', '[C]', '[c]']:
            filtered_string = my_string
        elif  char not in ['[C]', '[c]']:
            filtered_string = my_string
        return filtered_string