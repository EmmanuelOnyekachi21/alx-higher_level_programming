#!/usr/bin/python3


"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa.
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == '__main__':
    # Get MySQL credentials and database name from the command line arguments
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

    # Create a session
    session = Session()

    # Create a table using sqlalchemy ORM
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)
