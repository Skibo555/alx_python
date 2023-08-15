#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
        return a_dictionary
    def string_literal(a_dictionary, key value):
        a_dictionary[key] = update_dictionary(a_dictionary, key, value)
        if value in a_dictionary == string_literal:
            return a_dictionary[key]
    return a_dictionary