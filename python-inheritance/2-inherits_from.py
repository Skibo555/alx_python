"""
Square Module

This is a function that calculates squares using size as a parameter.
"""
def inherits_from(obj, a_class):
    """
    This is a docstring for is_same_class.

    Args:
        obj (int): The Object to be tested.
        a_class (string): The input.

    Returns:
        bool: if the object is a class of the object returns True else it returns False.
    """
    return issubclass(type(obj), a_class)
