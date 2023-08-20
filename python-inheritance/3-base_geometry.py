"""
BaseGeometry Module

This module prints the names of the magic attributes.
"""
class MetaClass(type):
    "
    This is a documentation for an obj.

    Agrs:
        cls: this is the only arguement it takes.
    
    Return:
        It returns a value in a variable.
    """
    def dir(cls):
        return [attribute for attribute in super().dir() if attribute != 'init_subclass']


class BaseGeometry(metaclass=MetaClass):
    """
    This is a class inside of a class.

    Args:
        metaclass: The only argument.

    Return: attribute
    """

    def dir(cls):
        return [attribute for attribute in super().dir() if attribute != 'init_subclass'])
