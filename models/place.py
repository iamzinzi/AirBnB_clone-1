#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60),
            ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60),
            ForeignKey('amenities.id'), primary_key=True, nullable=False)
    )

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
            'user_id',
            String(60),
            ForeignKey('users.id'),
            nullable=False
        )
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024), nullable=True)
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
            nullable=True
        )
    longitude = Column(
            'longitude',
            Float,
            nullable=True
        )
    amenity_ids = []

    @property
    def reviews(self):
        """return list of Review instances with place_id equal to the current
        Place.id"""
        review_instances = []
        objects = storage.all()
        for k, v in objects.items():
            class_name = k.split(".")[0]
            if class_name == "Review":
                if v["place_id"] == self.id:
                    review_instances.append(v)
        return review_instances

    @property
    def amenities(self):
        """return list of Amenity instances with place_id equal to the current
        Place.id"""
        amenity_instances = []
        for k, v in objects.items():
            class_name, instance_id = k.split(".")
            if class_name == "Amenity":
                if v["place_id"] == self.id and instance_id in amenity_ids:
                    amenity_instances.append(v)
        return amenity_instances

    @amenities.setter
    def amenities(self, obj):
        """append id of amenity objects into amenity_ids
        """
        class_dict = obj.__dict__
        if class_name["__class___"] == "Amenity":
            obj_id = class_name["id"]
            amenity_ids.append(obj_id)
            

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review',
                cascade='all, delete',
                backref='place'
            )
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                viewonly=False,
                backref='place'
            )
