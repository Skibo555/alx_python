#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    largest_value = None
    largest_key = None

    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if largest_value is None or value > largest_value:
                largest_value = value
                largest_key = key

    return largest_key