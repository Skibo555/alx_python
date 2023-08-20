"""
Your module documentation goes here
"""


class MetaClass(type):
    """
    documentation
    """
    def dir(cls):
        return [attribute for attribute in super().dir() if attribute != 'init_subclass']


class BaseGeometry(metaclass=MetaClass):
    """
    documentation for class goes here
    """

    def dir(cls):
        return [attribute for attribute in super().dir() if attribute != 'init_subclass']
