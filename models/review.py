#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = 'reviews'
    place_id = Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            nullable=False
        )
    user_id = Column(
            'user_id',
            String(60),
            ForeignKey('users.id'),
            nullable=False
        )
    text = Column('text', String(1024), nullable=False)
