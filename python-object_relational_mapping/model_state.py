from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# The class documentations

"""
The class documentation.
"""


class State(Base):
    """
    A class that models the table 'states', inherited from Base

    Attributes:

        id(int): unique identity number a state

        name(string): name of state
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True,
                primary_key=True,
                autoinrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
