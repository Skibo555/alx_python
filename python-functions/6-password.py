#!/usr/bin/python
def validate_password(password):
    if len(password) >= 8:
        return True
    for char in password:
        if any(char.issupper()):
            return True
    for char in password:
        if any(char.islower()):
            return True
    for char in password:
        if any(char.isspace()):
            return True
    else:
        return False