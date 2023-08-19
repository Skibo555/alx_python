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

    def __init__(self, size=0):
        """
        Initializes a Square instance with the given size.

        Args:
        - size (int): The size of the square's sides.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        return self.__size * self.__size
