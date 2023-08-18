class Square:
    """
    This class represents a square shape.

    Attributes:
    - size (int): The length of each side of the square.

    Methods:
    - __init__(self, __size): Constructs a Square instance with a given side length.
    - perimeter(self): Calculates and returns the perimeter of the square.
    """

    def __init__(self, __size):
        """
         Initializes a Square instance with the given size.

         Args:
         - __size (int): The length of each side of the square.
         """
        self.__size = __size
