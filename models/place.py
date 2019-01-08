#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    
    
    city_id = Column(
            'city_id',
            String(60),
            ForeignKey('cities.id'),
            nullable=False
        )
    user_id = Column(
            'users_id',
            String(60),
            ForeignKey('users.id'),
            nullable=False
        )
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024), nullable=False)
    number_rooms = Column('number_rooms', Integer, nullable=False, default=0)
    number_bathrooms = Column(
            'number_bathrooms',
            Integer,
            nullable=False,
            default=0
        )
    max_guest = Column(
            'max_guest',
            Integer,
            nullable=False,
            default=0
        )
    price_by_night = Column(
            'price_by_night',
            Integer,
            nullable=False,
            default=0
        )
    latitude = Column(
            'latitude',
            Float,
            nullable=False
        )
    longitude = Column(
            'longitude',
            Float,
            nullable=False
        )
    amenity_ids = []
