#!/usr/bin/python3

def best_score(a_dictionary):
        biggest_key = max(a_dictionary)
        if a_dictionary == "":
                return None
        else:
            return biggest_key