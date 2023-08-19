"""
Square Module

This is a function that calculates squares using size as a parameter.
"""


class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): The size of the square's sides.

    Methods:
    - __init__(self, size): Initializes a Square instance with the given size.

    Example usage:
    >>> square = Square(5)
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
        - size (int): The size of the square's sides.
        """
        self.__size = size
