#!/usr/bin/python3
"""storage module for find artisan"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .user import Base, User
from .artisan import Artisan
from .review import Review


class Storage:
    """storage class with attributes __engine and __session"""
    __engine = None
    __session = None
    def __init__(self):
        """initiate attributes"""
        db_user = "root"
        db_name = "find_artisan"
        db_password = ""
        db_host = "localhost"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(db_user, db_password,
                                             db_host, db_name))
    
    def load_db(self):
        """establish session with database"""
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session

    def add_new(self, cls_obj):
        """add new entry to table"""
        self.__session.add(cls_obj)
    
    def save(self):
        """execute queries and commit changes"""
        self.__session.commit()
    
    def get_obj(self, cls, email):
        """get a record from a table in the database"""
        if cls is not None:
            obj = self.__session.query(cls).filter_by(email=email).first()
        return obj
    
    def get_artisan(self, a_id):
        """get artisan object from database"""
        obj = self.__session.query(Artisan).filter_by(a_id=a_id).first()
        return obj
    
    def get_by_city(self, city, service):
        """get certain artisans in a city based on their service"""
        artisans = self.__session.query(Artisan).filter_by(city=city, service=service).all()
        return artisans
    
    def get_by_state(self, state, service):
        """get all artisans in a state rendering a service"""
        artisans = self.__session.query(Artisan).filter_by(state=state, service=service).all()
        return artisans
    
    def get_by_country(self, country, service):
        """get all artisans in a country rendering a service"""
        artisans = self.__session.query(Artisan).filter_by(country=country, service=service).all()
        return artisans

    def get_reviews(self, a_id):
        """get all reviews for an artisan"""
        reviews = self.__session.query(Review).filter_by(a_id=a_id).all()
        return reviews
    
    def get_services(self, input):
        """Select all services that match a string"""
        querystr = "%{}%".format(input)
        services = self.__session.query(Artisan).filter(Artisan.service.like(querystr)).all()
        if services is None:
            return None
        return services
    
    def delete(self, obj):
        """delete an object from database"""
        self.__session.delete(obj)
    
    def close(self):
        """close all connections to the database"""
        self.__session.close()