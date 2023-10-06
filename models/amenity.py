#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

class Amenity(BaseModel}
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = ""
    place_amenities = ""
