"""
BaseGeometry

This is a empty class
"""

class BaseGeometry:
    """
    This is an empty class of Geometry.

    Args:
        There are no agruments as of now

    Return:
        It does not return anything for now but it will in future.
    """
    pass

    magic_attributes = [attr for attr in dir(BaseGeometry) if attr.startswith('__')]
    print( magic_attributes)

