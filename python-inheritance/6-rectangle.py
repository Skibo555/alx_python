"""
Your module documentation goes here
"""


class MetaClass(type):
    """
    documentation
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=MetaClass):
    """
    documentation for class goes here
    """

    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """
        Calculates the area and raises an exception.

        Raises:
            Exception: Always raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    
     """
     class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
     Private instance attributes:
        width
        height
        Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        A subclass that represent a Rectangle inheriting from BaseGeometry.
        Attribute:
             width (int): An integer value.
             height (int): An integer value.

        Methods:
             It takes no method for now.
        """
        super().__init__("Rectangle")
        self.__width = width
        self.__height = height
