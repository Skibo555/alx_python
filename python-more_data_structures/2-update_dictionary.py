#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
        return a_dictionary
    if value in a_dictionary == str:
        a_dictionary[key] = str
        return a_dictionary