"""
Geometry Module

This module is used to calculate Geometry.

Example:
    >>> import module_name
    >>> instance = Rectangle.BaseGeomerty()
    >>> instance.method()
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
"""
Geometry Module

This module is used to calculate Geometry.

Example:
    >>> import module_name
    >>> instance = Rectangle.BaseGeomerty()
    >>> instance.method()
"""
class Rectangle(BaseGeometry):
    
     """
     Documentation
     """
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.__width = width
        self.__height = height
