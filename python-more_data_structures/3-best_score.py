#!/usr/bin/python3

def best_score(a_dictionary):
    largest_value = None
    for value in a_dictionary:
        if isinstance(value, int):
            if largest_value is None or value > largest_value:
                largest_value = value
    
    return largest_value