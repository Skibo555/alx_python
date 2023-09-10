"""
Documentation for this file.
"""
import sys
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine


def func():
    """
    The function I was asked to create for the marks!
    """
    if len(sys.argv) != 3:
        exit
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        mysql_database_name = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}'.format("mysql_username",
                               "mysql_password", "mysql_database_name"), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        for session in session.query(State).order_by(State.id).all():
            print("{}: {}".format(states.id, states.name))

        session.close()
