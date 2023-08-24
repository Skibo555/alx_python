"""
Module: Rectangle

This module defines the Rectangle class, which inherits from the Base class.

Classes:
- Base - Represents bass class for rest of classes.
- Rectangle: Represents a rectangle with width, height, x, and y attributes.
"""

from models.base import Base

class Rectangle(Base):
    """
    Represents a rectangle with width, height, x, and y attributes.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance with width, height, x and y.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The unique identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        """
        A getter for width
        """
        pass
    @width.setter
    def set_width(self, width):
        """
        A setter for the width attribute
        """
        pass

    @property
    def get_height(self):
        """
        A getter for height
        """
        pass
    @height.setter
    def set_height(self, height):
        """
        A setter for the height attribute
        """
        pass

    @property
    def get_x(self):
        """
        A getter for x
        """
        pass

    @x.setter
    def set_x(self, x):
        """
        A setter for the x attribute
        """
        pass
    @property
    def get_y(self):
        """
        A getter for y
        """
        pass
    @y.setter
    def set_y(self, y):
        """
        A setter for the y attribute
        """
        pass
