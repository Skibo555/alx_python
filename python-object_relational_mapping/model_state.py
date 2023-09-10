"""
This is a state model.
"""
from sqlalchemy import create_engine, Column, Integer, String


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This is a good practice just as ALX has thought us.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoinrement=True, nullable=False)
    name = Column(String, Integer(128), nullable=False)
