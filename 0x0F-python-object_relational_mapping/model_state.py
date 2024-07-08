#!/usr/bin/python3


"""
This module defines a State class and an instance Base usin g SQLAlchemy ORM.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
import sys

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/"
            f"{database}", pool_pre_ping=True
            )

    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(engine)
