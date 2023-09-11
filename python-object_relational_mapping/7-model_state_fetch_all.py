"""
Documentation for this file.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def func(self, id, name):
    id = self.id
    name = self.name
    """
    The function I was asked to create for the marks!
    """
    if len(sys.argv) != 3:
        exit
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        mysql_database_name = sys.argv[3]

    route = 'mysql+mysqldb://{}:{}@localhost?{}' \
            .format(mysql_username,
                    mysql_password,
                    mysql_database_name)
    engine = create_engine(route)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for session in session.query(State).order_by(State.id).all():
        print("{}: {}".format(self.id, self.name))

    session.close()


if __name__ == '__main__':
    func()
