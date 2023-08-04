#!/usr/bin/python
def validate_password(password):
    string = str(password)
    if len(str(password)) >= 8:
        if any(char.issupper() for char in str(password)):
            if any(char.islower() for char in str(password)):
                if any(char.isspace() for char in str(password)):
                    return True
    else:
        return False