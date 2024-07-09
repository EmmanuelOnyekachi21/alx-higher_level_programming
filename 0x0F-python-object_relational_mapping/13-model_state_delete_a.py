#!/usr/bin/python3


"""
delete all State objects with a name containing the letter 'a' from the
database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/"
        f"{database_name}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for the State objects with names containing 'a'
    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state found
    for state in state_to_delete:
        session.delete(state)

    session.commit()

    # Close the session
    session.close()
