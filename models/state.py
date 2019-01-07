#!/usr/bin/python3
"""This is the state class"""
from models import storage
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)

    @property
    def cities(self):
        """returns list of City instances with state_id equal to the current
        State.id"""
        city_instances = []
        objects = storage.all()
        for k, v in objects.items():
            class_name = k.split(".")[0]
            if class_name == "City":
                if v["state_id"] == self.id:
                    city_instances.append(v)
        return city_instances

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="states")
