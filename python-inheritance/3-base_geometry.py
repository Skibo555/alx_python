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
empty_instance = EmptyClass()

# Get the list of attributes using dir()
attributes = dir(empty_instance)

# Filter out magic attributes
magic_attributes = [attr for attr in attributes if attr.startswith('__') and attr.endswith('__')]

print(magic_attributes)
