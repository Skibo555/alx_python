"""
Documentation for this file.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database_name = sys.argv[3]

    route = 'mysql+mysqldb://{}: {}@localhost/{}' \
        .format(mysql_username,
                mysql_password,
                mysql_database_name)

    engine = create_engine(route)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
