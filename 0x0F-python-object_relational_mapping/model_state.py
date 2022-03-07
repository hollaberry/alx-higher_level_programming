#!/usr/bin/python3
"""File that contains the class definition
of a state and an instance Base = declaration_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key =True, nullable=False, unique=True)
    name = Column(String(128), nullable=False) 
