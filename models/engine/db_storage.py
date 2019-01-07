#!/usr/bin/python3
"""This is the database storage class for AirBnB"""
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DBStorage:
    """class Database Storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes an instance of class DBStorage.
        """
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST") # should be localhost
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        Base = declarative_base()

        # Drop all tables if HBNB_ENV is equal to test
        if HBNB_ENV == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Query on the current database session all objects depending
        on the class name parameter. If cls=None, query all types of objects.
        """
        found_objects = {}
        if cls is not None:
            for instance in self.__session.query(cls):
                key = "{}.{}".format(type(instance).__name__, instance.id)
                found_objects[key] = instance
            return found_objects
        else:
            #TODO: query all types of objects (User, State, City, Amenity,
            # Place and Review) and return.


    def new(self, obj):
        """Add the object to the current database session (self.__session)
        """
        self.__session.add(obj)
#        This line may not be needed
#        self.__session.commit()

    def save(self):
        """Commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None.
        """
        # TODO

    def reload(self):
        """Create all tables in the database. Then create the current
        database session from the engine (self.__session).
        """
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
