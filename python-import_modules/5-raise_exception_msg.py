#!/usr/bin/python3
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def raise_exception_msg(message=""):
    if message == int:
        raise NameError
    print(message)