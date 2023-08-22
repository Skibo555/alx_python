"""
This is a module documentation.
Though it is an empty one for now.
"""

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        """
        A module that's the constructor.
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += id
