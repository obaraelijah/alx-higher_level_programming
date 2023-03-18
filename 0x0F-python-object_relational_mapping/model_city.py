#!/usr/bin/python3

"""sqlalchemy"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """state object"""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key = True,
        nullable = False
    )
    name = Columns(String(128), nullable = False)
    state_id = Column(Integer, ForeignKey('states.id', nullable=False))
