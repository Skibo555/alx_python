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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return f"{self.size}"
