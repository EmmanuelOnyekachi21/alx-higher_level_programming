#!/usr/bin/python3


"""
This module defines a State class and an instance Base usin g SQLAlchemy ORM.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine
import sys
from relationship_city import City

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = (
            relationship("City", backref="state",
                         cascade="all, delete")
            )
