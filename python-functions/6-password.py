#!/usr/bin/python
def validate_password(password):
    if len(password) > 7:
        if not any(char.isupper() for char in password):
            if not any(char.islower() for char in password):
                if ' ' in password:
                    return True

    else:
        return False