"""
Module: models.base

This module defines the Base class.

Classes:
- Base: Represents the base class with an ID attribute.
"""

class Base:
    """
    Base class with an ID attribute.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of object count.
        id (int): Public instance attribute representing the object's ID.

    Methods:
        __init__(self, id=None): Constructor to initialize the object's ID.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id
instance = Base()
