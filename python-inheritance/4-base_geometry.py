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
