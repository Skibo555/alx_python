#!/usr/bin/python
def validate_password(password):
    for i in password:
        if i.isupper() and i.isspace and i.islower and i > 7:
            return True
        else:
            return False