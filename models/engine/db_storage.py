#!/usr/bin/python3
"""Module for the Database Storage Engine
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base
from os import environ


class DBStorage:
    """Used to store data in the database
    """
    __engine = None
    __session = None
    __metadata = None
    __classes = [
        Amenity,
        City,
        Place,
        Review,
        State,
        User
    ]

    def __init__(self):
        """Instantiates a new instance of DBStorage
        """
        # Environment variables
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')

        connection_string = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, db)

        self.__engine = create_engine(connection_string, pool_pre_ping=True)
        self.__metadata = MetaData()

        if env == "test":
            # Drop all tables if in test environment
            self.__metadata.drop_all(self.__engine)

    def all(self, cls=None):
        results = {}
        classes_to_get = []

        # We get all classes if none has been specified
        # If one has been specified, we get that
        if cls is None:
            classes_to_get = self.__classes
        else:
            classes_to_get = [cls]

        for _cls in classes_to_get:
            query = self.__session.query(_cls)
            query_results = query.all()

            for result in query_results:
                results[_cls.__name__ + "." + result.id] = result

        return results

    def new(self, obj):
        self.__session.add(obj)

    def delete(self, obj):
        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
