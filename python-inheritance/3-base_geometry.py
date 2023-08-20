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
    def __init__(self):
        pass

    def print_magic_attributes(self):
        attributes = dir(self)
        magic_attributes = [attr for attr in attributes if attr.startswith('__') and attr.endswith('__')]
        for attr in magic_attributes:
            print(attr)
