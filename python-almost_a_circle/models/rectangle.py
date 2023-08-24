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
        self.validate_width()
        self.validate_height()
        self.validate_x()
        self.validate_y()

    def validate_width(self):
        """
        validates the arguments passed into the object
        """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

    def validate_height(self):
        """
        validates the arguments passed into the object
        """
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

    def validate_x(self):
        """
        validates the arguments passed into the object
        """
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    def validate_y(self):
        """
        validates the arguments passed into the object
        """
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """
        Get the value of the width attribute.

        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the value of the width attribute.

        Args:
            width: The new width value.

        Returns:
            value
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @property
    def height(self):
        """
        Get the value of the height attribute.

        Returns:
            None
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the value of the height attribute.

        Args:
            height: The new height value.

        Returns:
            None
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Get the value of the x attribute.

        Returns:
            None
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the value of the x attribute.

        Args:
            x: The new x value.

        Returns:
            None
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Get the value of the y attribute.

        Returns:
            None
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set the value of the y attribute.

        Args:
            y: The new y value.

        Returns:
            None
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0".format(y))
        self.__y = y


    def area(self):
        """
        This module calculates the area of a rectangle.

        Arg:
            self.__height: It represents height attribute of a rectangle.
            self.__width: It represents the breath/width of a rectangle.

        Returns:
            The multiplication of these two attributes.
        """

        return self.__height * self.__width

    def display(self):
        """
        This module prints the inputs into the stdout.

        Arg:
            No args.

        Return:
            Rectangle.
        """

        for a in range(0, self.__y):
                print()
        for b in range(0, self.__height):
            for c in range(0, self.__x):
                print(" ", end="")
            for d in range(0, self.__width):
                print("#", end="")
            print()


    def __str__(self):
        """
        This is a module overrides the strings.

        Arg:
            None.

        Return:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectange] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
