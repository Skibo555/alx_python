#!/usr/bin/python3

def no_c(my_string):
    new_string = ""  # Initialize an empty string to store the modified result
    
    for char in my_string:
        # Check if the character is a lowercase or uppercase 'c'
        if char not in ['c', 'C']:
            new_string += char  # Add the character to the modified string
    
    return new_string  # Return the modified string