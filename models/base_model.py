#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone
"""
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import func
from models import storage
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models
    """
    id = Column(String(60), primary_key=True, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    updated_at = Column(DateTime(timezone=True),
                        server_onupdate=func.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model
        """
        now = datetime.now()

        if 'id' not in kwargs:
            self.id = str(uuid4())

        if 'created_at' not in kwargs:
            self.created_at = now

        if 'updated_at' not in kwargs:
            self.updated_at = now

        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            if key != '__class__':
                setattr(self, key, value)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}

        for key, value in self.__dict__.items():
            # Converting dates to isoformat strings
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()

            # Adding all keys that are not '_sa_instance_state'
            if key != '_sa_instance_state':
                dictionary[key] = value

        # Adding the class attribute
        dictionary['__class__'] = self.__class__.__name__

        return dictionary

    def __str__(self):
        """Returns a string representation of the instance
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
