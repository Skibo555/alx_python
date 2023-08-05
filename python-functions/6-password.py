#!/usr/bin/python

import re

def validate_password(password):
    if not re.search(r'[A-z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if ' ' in password:
        return False
    if len(password) < 8:
        return False
    return True