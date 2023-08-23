"""
Module: models.rectangle

This module defines the Rectangle class, which inherits from the Base class.

Classes:
- Rectangle: Represents a rectangle with width, height, x, and y attributes.
"""

from models.base import Base

class Rectangle(Base)

     """
    Represents a rectangle with width, height, x, and y attributes.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes a Rectangle instance.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The unique identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self_x = x
        self.y = y
