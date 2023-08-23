"""
Module: models.base

This module defines the Base class.

Classes:
- Base: Represents the base class with an ID attribute.
"""

from base import Base

class Rectangle(Base):
    """
    Base class with an ID attribute.

    Attributes:
        __width (int): Private class attribute that represents the width of the rectangle.
        __height (int): Private class.
        __x (int):
        __y (int):
        id (int): Public instance attribute representing the object's ID.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Constructor to initialize the object's attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiating the attributes
        """
        super().__init__("Base")
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
        def set_width(self):
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
        def set_height(self):
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
        def set_x(self):
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
        def set_y(self):
            """
            A setter for the y attribute
            """
            pass
