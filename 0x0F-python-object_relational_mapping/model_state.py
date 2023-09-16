#!/usr/bin/python3
"""
the State class using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class representing the states table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
