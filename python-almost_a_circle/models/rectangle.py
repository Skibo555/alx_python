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
        Get the value of the width attribute.

        Returns:
            None
        """
        return self.__width

    @get_width.setter
    def set_width(self, width):
        """
        Set the value of the width attribute.

        Args:
            width: The new width value.

        Returns:
            None
        """
        self.__width = width

    @property
    def get_height(self):
        """
        Get the value of the height attribute.

        Returns:
            None
        """
        return self.__height

    @get_height.setter
    def set_height(self, height):
        """
        Set the value of the height attribute.

        Args:
            height: The new height value.

        Returns:
            None
        """
        self.__height = height

    @property
    def get_x(self):
        """
        Get the value of the x attribute.

        Returns:
            None
        """
        return self.__x

    @get_x.setter
    def set_x(self, x):
        """
        Set the value of the x attribute.

        Args:
            x: The new x value.

        Returns:
            None
        """
        self.__x = x

    @property
    def get_y(self):
        """
        Get the value of the y attribute.

        Returns:
            None
        """
        return self.__y

    @get_y.setter
    def set_y(self, y):
        """
        Set the value of the y attribute.

        Args:
            y: The new y value.

        Returns:
            None
        """
        self.__y = y
