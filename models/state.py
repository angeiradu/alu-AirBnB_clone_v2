#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
from models import storage


class State(BaseModel, Base):
    """State class
    """
    __tablename__ = 'states'
    name = Column(
        String(128), nullable=False)

    @property
    def cities(self):
        storage_type = environ['HBNB_TYPE_STORAGE']
        if storage_type == "db":
            return relationship(
                'City', back_populates='states', cascade='all, delete')
        else:
            return storage.all(State)
