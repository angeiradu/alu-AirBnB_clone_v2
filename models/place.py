#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if environ["HBNB_TYPE_STORAGE"] == "db":
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            # Get reviews from filestorage
            from models import storage
            from models.review import Review
            reviews = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
