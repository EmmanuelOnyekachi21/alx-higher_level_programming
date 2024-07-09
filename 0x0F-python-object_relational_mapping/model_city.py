#!/usr/bin/python3


"""
This module defines a City class and an instance Base using SQLAlchemy ORM.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
     class that links to the MySQL table city.
    """
    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True, autoincrement=True, nullable=False,
             unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
