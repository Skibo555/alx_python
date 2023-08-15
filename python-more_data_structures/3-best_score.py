#!/usr/bin/python3

def best_score(a_dictionary):
    for v in a_dictionary:
        biggest_value = max(a_dictionary.values)
        return biggest_value