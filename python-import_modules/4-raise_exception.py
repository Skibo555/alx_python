class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def raise_exception():
    if 10 % 2 == 0:
        raise CustomError("You got it.")