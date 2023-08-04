#!/usr/bin/python
def validate_password(password):
    if len(password) == 8 and any(char.issupper() for char in password) and any(char.islower() for char in password) and any(char.isspace() for char in password):
        return True
    else:
        return False