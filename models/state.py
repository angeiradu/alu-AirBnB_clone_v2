#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from os import environ


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', backref='states',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
