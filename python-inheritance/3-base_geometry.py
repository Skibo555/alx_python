"""
BaseGeometry

This is a empty class
"""

class BaseGeometry:
    """
    This is an empty class of Geometry.

    Args:
       It does not take any arguments!

    Return:
        It does not return anything for now but it will in future.
    """
    pass

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
