#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary = {key: [value]}
    key_to_append = key
    value_to_append = value
    if key_to_append in a_dictionary:
        a_dictionary[key_to_append].append(value_to_append)
    else:
        a_dictionary[key_to_append] = [value_to_append]