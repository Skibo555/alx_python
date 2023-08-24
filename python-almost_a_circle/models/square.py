"""
Module: Square

This module represents a square.

Classes:
    - Rectangle: it represents a base class.
    - Square: My acutual class.
"""

from models.rectangle import rectangle

class Square(Rectangle):

"""
    This is a class that defines a square.
    Attributes:
        size (int): I don't like this.
        x (int): I don't know.
        y (int): I don't know seh.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        A getter that gives access for calling
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
