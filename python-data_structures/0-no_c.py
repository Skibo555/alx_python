#!/usr/bin/python3

import re

def no_c(my_string):
    if not re.search(r'[c-C]', my_string):
        new_string = my_string
        return new_string