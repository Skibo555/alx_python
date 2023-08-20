"""
Your module documentation goes here
"""


class MetaClass(type):
    """
    documentation
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != 'init_subclass']


class BaseGeometry(metaclass=MetaClass):
    """
    documentation for class goes here
    """

    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != 'init_subclass']
