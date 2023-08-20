"""
Square Module

This is a function that calculates squares using size as a parameter.
"""
def is_same_class(obj, a_class):
    """
    This is a docstring for is_same_class.

    Args:
        obj (int): The Object to be tested.
        a_class (string): The input.

    Returns:
        bool: if the object is a class returns True else it returns False.
    """
    return type(obj) is a_class
