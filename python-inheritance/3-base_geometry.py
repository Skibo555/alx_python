"""
A module that have an empty class with override to dir() method
"""

class MetaClass(type):
    """
    Override dir() method to exclude __init__subclass__
    """
    def dir(cls):
        return [attribute for attribute in super().__dir()__ if attribute != 'init_subclass']


class BaseGeometry(metaclass=MetaClass):
    """
    BaseGeometry class that uses the overriden dir() method.
    """

    def dir(cls):
        return [attribute for attribute in super().__dir()__ if attribute != 'init_subclass']
