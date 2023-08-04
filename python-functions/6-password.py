#!/usr/bin/python
def validate_password(password):
    for i in password:
        if any(i.isupper()) and any(i.isspace) and any(i.islower) and i > 7:
            return True
        else:
            return False