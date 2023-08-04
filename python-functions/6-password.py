#!/usr/bin/python
def validate_password(password):
    if len(password) > 8:
        if any(char.issupper() for char in password):
            if any(char.islower() for char in password):
                if any(char.isspace() for char in password):
                    return True
    else:
        return False